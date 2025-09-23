@echo off
chcp 65001 >nul

REM ============================
REM   Startscript voor QR-CodeGen
REM ============================

:: Zet titel van venster
title Gezinsbond Hulptools aangeboden door CyNiT

:: Kleuren
set "RESET=[0m"
set "GREEN=[92m"
set "WHITE=[97m"

:: Brede lijn
set "LINE=%GREEN%============================================================%RESET%"
set "TITLE=%WHITE%------  Gezinsbond Hulptools aangeboden door CyNiT  --------%RESET%"

:: Zoek virtuele omgeving in root of gbw-map
set VENV_DIR=
if exist venv\Scripts\activate.bat set VENV_DIR=venv
if exist gbw\venv\Scripts\activate.bat set VENV_DIR=gbw\venv

if "%VENV_DIR%"=="" (
    echo [FOUT] Virtuele omgeving niet gevonden!
    echo Maak eerst een virtualenv met: python -m venv venv
    pause
    exit /b
)

:: Activeer virtuele omgeving
call %VENV_DIR%\Scripts\activate.bat

:MENU
cls
echo %LINE%
echo %TITLE%
echo %LINE%
echo.
echo [1] QR Generators
echo [2] Aftelklokken
echo [3] Tools
echo %LINE%
echo [q] afsluiten
echo %LINE%
set /p keuze="Maak je keuze: "

if "%keuze%"=="1" goto QR_MENU
if "%keuze%"=="2" goto CLOCK_MENU
if "%keuze%"=="3" goto TOOLS_MENU
if /I "%keuze%"=="q" exit

goto MENU

:QR_MENU
cls
echo %LINE%
echo %TITLE%
echo %LINE%
echo %WHITE%                          QR Generators Menu%RESET%
echo %LINE%
echo.
echo [1] QR Generator (qrgbw.py)
echo [2] QR Generator met Afdeling (qrkoko.py)
echo %LINE%
echo [t] terug
echo [q] afsluiten
echo %LINE%
set /p keuze="Maak je keuze: "

if "%keuze%"=="1" python gbw\qrgbw.py
if "%keuze%"=="2" python gbw\qrkoko.py
if /I "%keuze%"=="t" goto MENU
if /I "%keuze%"=="q" exit

pause
goto QR_MENU

:CLOCK_MENU
cls
echo %LINE%
echo %TITLE%
echo %LINE%
echo %WHITE%                          Aftelklokken Menu%RESET%
echo %LINE%
echo.
echo [1] Aftelklok 1 (aftelklok.py)
echo [2] Aftelklok 2 (aftelklok1.py)
echo [3] Aftelklok 3 (aftelklok2.py)
echo %LINE%
echo [t] terug
echo [q] afsluiten
echo %LINE%
set /p keuze="Maak je keuze: "

if "%keuze%"=="1" python gbw\aftelklok.py
if "%keuze%"=="2" python gbw\aftelklok1.py
if "%keuze%"=="3" python gbw\aftelklok2.py
if /I "%keuze%"=="t" goto MENU
if /I "%keuze%"=="q" exit

pause
goto CLOCK_MENU

:TOOLS_MENU
cls
echo %LINE%
echo %TITLE%
echo %LINE%
echo %WHITE%                             Tools Menu%RESET%
echo %LINE%
echo.
echo [1] Auto Commit naar GitHub (git_auto_commit.py)
echo [2] Setup Dependencies (setup.bat)
echo %LINE%
echo [t] terug
echo [q] afsluiten
echo %LINE%
set /p keuze="Maak je keuze: "

if "%keuze%"=="1" python gbw\git_auto_commit.py
if "%keuze%"=="2" call setup.bat
if /I "%keuze%"=="t" goto MENU
if /I "%keuze%"=="q" exit

pause
goto TOOLS_MENU
