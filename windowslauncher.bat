@echo off
REM Windows launcher for main.py with custom terminal size

REM Change directory to the script's folder
cd /d "%~dp0"

REM Set terminal size (columns x lines)
mode con: cols=120 lines=30

REM Launch the Python script
python main.py

REM Pause so the window stays open after the script finishes
pause
