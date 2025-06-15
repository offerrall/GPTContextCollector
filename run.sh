#!/bin/zsh

BASE_DIR="$(dirname "$0")"
VENV="$HOME/.venvs/global"

if [[ -f "$BASE_DIR/main.pyw" ]]; then
  SCRIPT="$BASE_DIR/main.pyw"
  BACKGROUND=true
elif [[ -f "$BASE_DIR/main.py" ]]; then
  SCRIPT="$BASE_DIR/main.py"
  BACKGROUND=false
else
  echo "❌ No se encontró main.py ni main.pyw en $BASE_DIR"
  exit 1
fi

source "$VENV/bin/activate"

if [[ $BACKGROUND == true ]]; then
  nohup python "$SCRIPT" > /dev/null 2>&1 &
else
  python "$SCRIPT"
fi