:: nucax2025
@echo off
echo Installing required packages...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python first.
    pause
    exit /b
)

:: Upgrade pip first
python -m pip install --upgrade pip

:: Install required packages
python -m pip install psutil pyautogui pyperclip winshell comtypes pycaw screen_brightness_control requests keyboard

echo All packages installed!
pause