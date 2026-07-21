#!/usr/bin/env bash
# MEXC Spot API wrapper. All trading API calls go through here.
# Usage: bash scripts/mexc.sh <subcommand> [args...]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

: "${MEXC_API_KEY:?MEXC_API_KEY not set in environment}"
: "${MEXC_SECRET_KEY:?MEXC_SECRET_KEY not set in environment}"

BASE="${MEXC_BASE_URL:-https://api.mexc.com}"

_sign() {
  echo -n "$1" | openssl dgst -sha256 -hmac "$MEXC_SECRET_KEY" | awk '{print $2}'
}

_json_to_params() {
  echo "$1" | python3 -c "
import json, sys, urllib.parse
data = json.loads(sys.stdin.read())
print(urllib.parse.urlencode(data))
"
}

_auth_get() {
  local path="$1"
  local params="${2:-}"
  local ts; ts=$(date +%s%3N)
  local full
  if [[ -n "$params" ]]; then full="${params}&timestamp=${ts}"; else full="timestamp=${ts}"; fi
  local sig; sig=$(_sign "$full")
  curl -fsS \
    -H "X-MEXC-APIKEY: $MEXC_API_KEY" \
    "${BASE}${path}?${full}&signature=${sig}"
}

_auth_post() {
  local path="$1"
  local params="${2:-}"
  local ts; ts=$(date +%s%3N)
  local full
  if [[ -n "$params" ]]; then full="${params}&timestamp=${ts}"; else full="timestamp=${ts}"; fi
  local sig; sig=$(_sign "$full")
  curl -fsS -X POST \
    -H "X-MEXC-APIKEY: $MEXC_API_KEY" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "${full}&signature=${sig}" \
    "${BASE}${path}"
}

_auth_delete() {
  local path="$1"
  local params="${2:-}"
  local ts; ts=$(date +%s%3N)
  local full
  if [[ -n "$params" ]]; then full="${params}&timestamp=${ts}"; else full="timestamp=${ts}"; fi
  local sig; sig=$(_sign "$full")
  curl -fsS -X DELETE \
    -H "X-MEXC-APIKEY: $MEXC_API_KEY" \
    "${BASE}${path}?${full}&signature=${sig}"
}

cmd="${1:-}"
shift || true

case "$cmd" in

  account)
    _auth_get "/api/v3/account"
    ;;

  balance)
    asset="${1:?usage: balance ASSET}"
    _auth_get "/api/v3/account" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
for b in data.get('balances', []):
    if b['asset'] == '$asset':
        print(json.dumps(b, indent=2))
        sys.exit(0)
print(json.dumps({'asset': '$asset', 'free': '0', 'locked': '0'}, indent=2))
"
    ;;

  positions)
    _auth_get "/api/v3/account" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
positions = [b for b in data.get('balances', [])
             if float(b.get('free', 0)) + float(b.get('locked', 0)) > 0]
print(json.dumps(positions, indent=2))
"
    ;;

  quote)
    sym="${1:?usage: quote SYMBOL}"
    curl -fsS "${BASE}/api/v3/ticker/bookTicker?symbol=${sym}"
    ;;

  price)
    sym="${1:?usage: price SYMBOL}"
    curl -fsS "${BASE}/api/v3/ticker/price?symbol=${sym}"
    ;;

  orders)
    sym="${1:-}"
    if [[ -n "$sym" ]]; then
      _auth_get "/api/v3/openOrders" "symbol=${sym}"
    else
      _auth_get "/api/v3/openOrders"
    fi
    ;;

  order)
    # Usage: order '{"symbol":"BTCUSDT","side":"BUY","type":"MARKET","quoteOrderQty":"2000"}'
    body_json="${1:?usage: order '{...json...}'}"
    params=$(_json_to_params "$body_json")
    _auth_post "/api/v3/order" "$params"
    ;;

  cancel)
    sym="${1:?usage: cancel SYMBOL ORDER_ID}"
    oid="${2:?usage: cancel SYMBOL ORDER_ID}"
    _auth_delete "/api/v3/order" "symbol=${sym}&orderId=${oid}"
    ;;

  cancel-all)
    sym="${1:?usage: cancel-all SYMBOL}"
    _auth_delete "/api/v3/openOrders" "symbol=${sym}"
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
    free_qty=$(_auth_get "/api/v3/account" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for b in data.get('balances', []):
    if b['asset'] == '$base_asset':
        print(b.get('free', '0'))
        sys.exit(0)
print('0')
")
    if python3 -c "import sys; sys.exit(0 if float('$free_qty') > 0 else 1)"; then
      params=$(_json_to_params "{\"symbol\":\"${sym}\",\"side\":\"SELL\",\"type\":\"MARKET\",\"quantity\":\"${free_qty}\"}")
      _auth_post "/api/v3/order" "$params"
    else
      echo "No free balance found for $base_asset" >&2
      exit 1
    fi
    ;;

  close-all)
    _auth_get "/api/v3/account" \
      | python3 -c "
import json, sys
data = json.load(sys.stdin)
for b in data.get('balances', []):
    if b['asset'] != 'USDT' and float(b.get('free', 0)) > 0:
        print(b['asset'] + 'USDT ' + b['free'])
" | while IFS=' ' read -r pair qty; do
        echo "Closing $pair qty=$qty"
        bash "$0" close "$pair"
      done
    ;;

  *)
    echo "Usage: bash scripts/mexc.sh <account|balance|positions|quote|price|orders|order|cancel|cancel-all|close|close-all> [args]" >&2
    exit 1
    ;;
esac

echo
