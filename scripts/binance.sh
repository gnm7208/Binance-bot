#!/usr/bin/env bash
# Binance Spot API wrapper. All trading API calls go through here.
# Usage: bash scripts/binance.sh <subcommand> [args...]
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="$ROOT/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

: "${BINANCE_API_KEY:?BINANCE_API_KEY not set in environment}"
: "${BINANCE_SECRET_KEY:?BINANCE_SECRET_KEY not set in environment}"

BASE="${BINANCE_BASE_URL:-https://api.binance.com}"

_sign() {
  echo -n "$1" | openssl dgst -sha256 -hmac "$BINANCE_SECRET_KEY" | awk '{print $2}'
}

_auth_get() {
  local path="$1"
  local params="${2:-}"
  local ts
  ts=$(date +%s%3N)
  local query="timestamp=${ts}"
  [[ -n "$params" ]] && query="${params}&timestamp=${ts}"
  local sig
  sig=$(_sign "$query")
  curl -fsS \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "${BASE}${path}?${query}&signature=${sig}"
}

_auth_delete() {
  local path="$1"
  local params="${2:-}"
  local ts
  ts=$(date +%s%3N)
  local query="timestamp=${ts}"
  [[ -n "$params" ]] && query="${params}&timestamp=${ts}"
  local sig
  sig=$(_sign "$query")
  curl -fsS -X DELETE \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    "${BASE}${path}?${query}&signature=${sig}"
}

_auth_post_order() {
  local params="$1"
  local ts
  ts=$(date +%s%3N)
  local body="${params}&timestamp=${ts}"
  local sig
  sig=$(_sign "$body")
  curl -fsS -X POST \
    -H "X-MBX-APIKEY: $BINANCE_API_KEY" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "${body}&signature=${sig}" \
    "${BASE}/api/v3/order"
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
for b in data['balances']:
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
positions = [b for b in data['balances'] if float(b['free']) > 0 or float(b['locked']) > 0]
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
    # Usage: order 'symbol=BTCUSDT&side=BUY&type=MARKET&quoteOrderQty=100'
    params="${1:?usage: order 'param1=val1&param2=val2'}"
    _auth_post_order "$params"
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
import re, sys
sym = '$sym'
for quote in ['USDT','BTC','ETH','BNB','BUSD']:
    if sym.endswith(quote):
        print(sym[:-len(quote)])
        sys.exit(0)
print(sym)
")
    free_qty=$(_auth_get "/api/v3/account" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for b in data['balances']:
    if b['asset'] == '$base_asset':
        print(b['free'])
        sys.exit(0)
print('0')
")
    if python3 -c "import sys; sys.exit(0 if float('$free_qty') > 0 else 1)"; then
      _auth_post_order "symbol=${sym}&side=SELL&type=MARKET&quantity=${free_qty}"
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
for b in data['balances']:
    if b['asset'] != 'USDT' and float(b['free']) > 0:
        print(b['asset'] + 'USDT ' + b['free'])
" | while IFS=' ' read -r pair qty; do
        echo "Closing $pair qty=$qty"
        bash "$0" close "$pair"
      done
    ;;

  *)
    echo "Usage: bash scripts/binance.sh <account|balance|positions|quote|price|orders|order|cancel|cancel-all|close|close-all> [args]" >&2
    exit 1
    ;;
esac

echo
