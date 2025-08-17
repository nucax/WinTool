:: bichtass i wanna do a screenshot but i am not at home so i am gonna do it on winlator and this bitchass thing does not allow me to do input like tf
@echo off
echo Checking for Python...

python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed.
    exit /b
)

echo Python not found. Downloading Python 3.13.7 64-bit installer...

set "PYTHON_URL=https://www.python.org/ftp/python/3.13.7/python-3.13.7-amd64.exe"
set "INSTALLER=%TEMP%\python_installer.exe"

powershell -Command "Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%INSTALLER%'"

echo Running Python installer silently...
"%INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo Cleaning up installer...
del "%INSTALLER%"

echo Python 3.13.7 (64-bit) installed successfully!