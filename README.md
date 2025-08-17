## WinTool

WinTool is a multifunctional Windows utility tool written in Python.
It provides a menu-driven interface to quickly access system information, perform maintenance tasks, and manage basic Windows operations — all from the command line.

Features

System & User Management

Shutdown, restart, log out, or lock the workstation

List, create, rename, delete, and manage local users

Change user passwords

Run programs with system privileges (via PsExec)


System Information

Show Windows version, architecture, and hostname

Display hardware info (CPU, RAM, disk usage)

View local and public IP addresses

List active network connections


## Utilities & Tools

Open Task Manager, Control Panel, Device Manager, Services, Registry Editor, Event Viewer, Startup folder, Scheduled Tasks

Empty Recycle Bin

Take screenshots

View and clear clipboard

Quick notepad for instant notes

Batch file operations (copy, move, delete, rename)

Hotkey manager

Adjust system volume

Adjust screen brightness (if supported)

Simple app launcher (Notepad, Calculator, Paint)



## Requirements

Windows OS

Python 3.8+

The following Python packages:

psutil

requests

pyperclip

pyautogui

winshell

keyboard

pycaw

comtypes

screen_brightness_control



## Install dependencies via pip:

```bash
pip install psutil requests pyperclip pyautogui winshell keyboard pycaw comtypes screen-brightness-control
```

Some features (like running as system) require PsExec to be installed and available in your PATH.

## Usage

Run the script in a terminal:

python wintool.py

You will see a numbered menu. Enter the corresponding number to execute a function, or Q to quit.

## Example:

Wintool v1 nucaxem :D
1. Print custom text
2. Shutdown PC
3. Restart PC
...
Q. Quit
Choose:

## Notes

Certain features may require administrator privileges.

Brightness control is only supported on compatible hardware.

Some utilities rely on Windows built-in tools (like Task Manager, Control Panel, etc.).


## License

This project is licensed under the MIT License. See the LICENSE file for details.
