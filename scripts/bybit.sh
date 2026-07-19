#!/usr/bin/env bash
# Bybit Spot API wrapper. All trading API calls go through here.
# Usage: bash scripts/bybit.sh <subcommand> [args...]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

: "${BYBIT_API_KEY:?BYBIT_API_KEY not set in environment}"
: "${BYBIT_SECRET_KEY:?BYBIT_SECRET_KEY not set in environment}"

BASE="${BYBIT_BASE_URL:-https://api.bybit.com}"
RECV_WINDOW=5000

_sign() {
  echo -n "$1" | openssl dgst -sha256 -hmac "$BYBIT_SECRET_KEY" | awk '{print $2}'
}

_auth_get() {
  local path="$1"
  local params="${2:-}"
  local ts
  ts=$(date +%s%3N)
  local sig
  sig=$(_sign "${ts}${BYBIT_API_KEY}${RECV_WINDOW}${params}")
  local url="${BASE}${path}"
  [[ -n "$params" ]] && url="${url}?${params}"
  curl -fsS \
    -H "X-BAPI-API-KEY: $BYBIT_API_KEY" \
    -H "X-BAPI-SIGN: $sig" \
    -H "X-BAPI-SIGN-TYPE: 2" \
    -H "X-BAPI-TIMESTAMP: $ts" \
    -H "X-BAPI-RECV-WINDOW: $RECV_WINDOW" \
    "$url"
}

_auth_post() {
  local path="$1"
  local body="${2:-{}}"
  local ts
  ts=$(date +%s%3N)
  local sig
  sig=$(_sign "${ts}${BYBIT_API_KEY}${RECV_WINDOW}${body}")
  curl -fsS -X POST \
    -H "X-BAPI-API-KEY: $BYBIT_API_KEY" \
    -H "X-BAPI-SIGN: $sig" \
    -H "X-BAPI-SIGN-TYPE: 2" \
    -H "X-BAPI-TIMESTAMP: $ts" \
    -H "X-BAPI-RECV-WINDOW: $RECV_WINDOW" \
    -H "Content-Type: application/json" \
    -d "$body" \
    "${BASE}${path}"
}

cmd="${1:-}"
shift || true

case "$cmd" in

  account)
    _auth_get "/v5/account/wallet-balance" "accountType=SPOT"
    ;;

  balance)
    asset="${1:?usage: balance ASSET}"
    _auth_get "/v5/account/wallet-balance" "accountType=SPOT" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
for account in data['result']['list']:
    for coin in account['coin']:
        if coin['coin'] == '$asset':
            print(json.dumps(coin, indent=2))
            sys.exit(0)
print(json.dumps({'coin': '$asset', 'walletBalance': '0', 'locked': '0'}, indent=2))
"
    ;;

  positions)
    _auth_get "/v5/account/wallet-balance" "accountType=SPOT" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
positions = []
for account in data['result']['list']:
    for coin in account['coin']:
        if float(coin.get('walletBalance', '0')) > 0:
            positions.append(coin)
print(json.dumps(positions, indent=2))
"
    ;;

  quote)
    sym="${1:?usage: quote SYMBOL}"
    curl -fsS "${BASE}/v5/market/orderbook?category=spot&symbol=${sym}&limit=1"
    ;;

  price)
    sym="${1:?usage: price SYMBOL}"
    curl -fsS "${BASE}/v5/market/tickers?category=spot&symbol=${sym}" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
ticker = data['result']['list'][0]
print(json.dumps({'symbol': ticker['symbol'], 'price': ticker['lastPrice']}, indent=2))
"
    ;;

  orders)
    sym="${1:-}"
    if [[ -n "$sym" ]]; then
      _auth_get "/v5/order/realtime" "category=spot&symbol=${sym}"
    else
      _auth_get "/v5/order/realtime" "category=spot"
    fi
    ;;

  order)
    # Usage: order '{"category":"spot","symbol":"BTCUSDT","side":"Buy","orderType":"Market","qty":"2000","marketUnit":"quoteCoin"}'
    body="${1:?usage: order '{...json...}'}"
    _auth_post "/v5/order/create" "$body"
    ;;

  cancel)
    sym="${1:?usage: cancel SYMBOL ORDER_ID}"
    oid="${2:?usage: cancel SYMBOL ORDER_ID}"
    _auth_post "/v5/order/cancel" \
      "{\"category\":\"spot\",\"symbol\":\"${sym}\",\"orderId\":\"${oid}\"}"
    ;;

  cancel-all)
    sym="${1:?usage: cancel-all SYMBOL}"
    _auth_post "/v5/order/cancel-all" \
      "{\"category\":\"spot\",\"symbol\":\"${sym}\"}"
    ;;

  close)
    sym="${1:?usage: close SYMBOL (e.g. BTCUSDT)}"
    base_asset=$(python3 -c "
sym = '$sym'
for quote in ['USDT','BTC','ETH','USDC']:
    if sym.endswith(quote):
        print(sym[:-len(quote)])
        import sys; sys.exit(0)
print(sym)
")
    free_qty=$(_auth_get "/v5/account/wallet-balance" "accountType=SPOT" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for account in data['result']['list']:
    for coin in account['coin']:
        if coin['coin'] == '$base_asset':
            wallet = float(coin.get('walletBalance', '0'))
            locked = float(coin.get('locked', '0'))
            print(str(wallet - locked))
            sys.exit(0)
print('0')
")
    if python3 -c "import sys; sys.exit(0 if float('$free_qty') > 0 else 1)"; then
      _auth_post "/v5/order/create" \
        "{\"category\":\"spot\",\"symbol\":\"${sym}\",\"side\":\"Sell\",\"orderType\":\"Market\",\"qty\":\"${free_qty}\"}"
    else
      echo "No free balance found for $base_asset" >&2
      exit 1
    fi
    ;;

  close-all)
    _auth_get "/v5/account/wallet-balance" "accountType=SPOT" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
for account in data['result']['list']:
    for coin in account['coin']:
        if coin['coin'] != 'USDT' and float(coin.get('walletBalance', '0')) > 0:
            wallet = float(coin.get('walletBalance', '0'))
            locked = float(coin.get('locked', '0'))
            free = wallet - locked
            if free > 0:
                print(coin['coin'] + 'USDT ' + str(free))
" | while IFS=' ' read -r pair qty; do
        echo "Closing $pair qty=$qty"
        bash "$0" close "$pair"
      done
    ;;

  *)
    echo "Usage: bash scripts/bybit.sh <account|balance|positions|quote|price|orders|order|cancel|cancel-all|close|close-all> [args]" >&2
    exit 1
    ;;
esac

echo
