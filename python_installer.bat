:: tung tung tung tung sahur
:: is it ok to do vbs and batch script in visual studio?
@echo off
echo Checking for Python...

python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed.
    pause
    exit /b
)

echo Python not found. Please choose your system architecture:
echo 1. 64-bit
echo 2. 32-bit
set /p ARCH="Enter your choice (1 or 2): "

if "%ARCH%"=="1" (
    set "PYTHON_URL=https://www.python.org/ftp/python/3.13.7/python-3.13.7-amd64.exe"
) else if "%ARCH%"=="2" (
    set "PYTHON_URL=https://www.python.org/ftp/python/3.13.7/python-3.13.7.exe"
) else (
    echo Invalid choice. Exiting.
    pause
    exit /b
)

set "INSTALLER=%TEMP%\python_installer.exe"

echo Downloading Python installer...
powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%INSTALLER%'"

echo Running Python installer...
"%INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Installation complete. Cleaning up...
del "%INSTALLER%"

echo Python 3.13.7 installed successfully!
pause