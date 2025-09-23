@echo off
REM ============================
REM Startscript voor QR-CodeGen
REM ============================

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting main script...
python gbw\start.py

pause
