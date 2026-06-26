@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  python -m venv .venv
)

".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt

if not exist "models\bert-small-en\config.json" (
  ".venv\Scripts\python.exe" scripts\download_model.py --model google/bert_uncased_L-4_H-256_A-4 --out models\bert-small-en
)

".venv\Scripts\python.exe" server.py --model models\bert-small-en
