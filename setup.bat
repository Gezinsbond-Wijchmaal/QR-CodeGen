@echo off
echo ============================
echo 🚀 QR-CodeGen Setup Script
echo ============================

echo Activating virtual environment...
call gbw\venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt
python -m pip install --upgrade --extra-index-url https://PySimpleGUI.net/install PySimpleGUI

echo ✅ Setup completed!
pause
