@echo off
setlocal
cd /d "%~dp0"

call setup_bert_demo.bat --no-pause
if errorlevel 1 exit /b 1

call start_bert_demo.bat
