@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  python -m venv .venv
)

".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install -r requirements.txt

if not exist "models\bert-tiny\config.json" (
  ".venv\Scripts\python.exe" scripts\download_model.py --model prajjwal1/bert-tiny --out models\bert-tiny
)

".venv\Scripts\python.exe" server.py --model models\bert-tiny
