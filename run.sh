#!/bin/zsh

BASE_DIR="$(dirname "$0")"
VENV="$BASE_DIR/venv"
SCRIPT="$BASE_DIR/main.pyw"

source "$VENV/bin/activate"
nohup python "$SCRIPT" > /dev/null 2>&1 &
