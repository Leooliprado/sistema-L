#!/bin/bash

# Diretório onde o script está
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"

# Ativa o virtualenv
source "$BASE_DIR/venv/bin/activate"

# Executa o Python
python3 "$BASE_DIR/sistema-l.py"

