@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Python environment not found. Run setup_bert_demo.bat first.
  exit /b 1
)

if not exist "models\bert-small-en\config.json" (
  echo Local BERT model not found. Run setup_bert_demo.bat first.
  exit /b 1
)

".venv\Scripts\python.exe" server.py --model models\bert-small-en
