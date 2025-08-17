import os
import sys
import subprocess
import platform
import socket
import psutil
import requests
import ctypes
import shutil
import pyperclip
import pyautogui
import tempfile
import winshell
from datetime import datetime

# Lock workstation
def lock_workstation():
    ctypes.windll.user32.LockWorkStation()

# 1
def print_custom_text():
    msg = input("Enter text: ")
    count = int(input("Repeat how many times?: "))
    print(msg * count)

# 13
def show_windows_info():
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Architecture:", platform.machine())
    print("Hostname:", socket.gethostname())

# 14
def show_hardware_info():
    print("CPU cores:", psutil.cpu_count(logical=True))
    print("CPU usage:", psutil.cpu_percent(), "%")
    print("RAM total:", round(psutil.virtual_memory().total/1e9,2), "GB")
    print("RAM used:", round(psutil.virtual_memory().used/1e9,2), "GB")
    print("Disks:")
    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)
        print(f" {part.device} {round(usage.total/1e9,2)}GB total, {round(usage.used/1e9,2)}GB used")

# 16
def show_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        print("Public IP:", ip)
    except:
        print("Failed to fetch public IP")

# 25
def empty_recycle_bin():
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    print("Recycle Bin emptied.")

# 26
def take_screenshot():
    img = pyautogui.screenshot()
    path = os.path.join(os.getcwd(), f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    img.save(path)
    print("Saved screenshot to:", path)

# 27
def show_clipboard():
    print("Clipboard:", pyperclip.paste())

# 28
def clear_clipboard():
    pyperclip.copy("")
    print("Clipboard cleared.")

# 29
def quick_notepad():
    path = os.path.join(tempfile.gettempdir(), "quicknote.txt")
    with open(path, "w") as f:
        f.write(input("Write your note: "))
    os.system(f"notepad {path}")

# 30
def batch_file_ops():
    print("1. Copy file\n2. Move file\n3. Delete file\n4. Rename file")
    c = input("Choose: ")
    if c == "1":
        src = input("Source: ")
        dst = input("Destination: ")
        shutil.copy(src, dst)
    elif c == "2":
        src = input("Source: ")
        dst = input("Destination: ")
        shutil.move(src, dst)
    elif c == "3":
        path = input("File to delete: ")
        os.remove(path)
    elif c == "4":
        src = input("File: ")
        new = input("New name: ")
        os.rename(src, new)

# 32
def hotkey_manager():
    print("Simple hotkey system (press Ctrl+C to exit)")
    import keyboard
    keyboard.add_hotkey("ctrl+alt+h", lambda: print("Hotkey pressed!"))
    keyboard.wait()

# 33
def adjust_volume():
    vol = int(input("Volume (0-100): "))
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(vol/100, None)

# 34
def adjust_brightness():
    try:
        import screen_brightness_control as sbc
        val = int(input("Brightness (0-100): "))
        sbc.set_brightness(val)
    except Exception as e:
        print("Brightness control not supported:", e)

# 35
def open_launcher():
    apps = {
        "1": "notepad",
        "2": "calc",
        "3": "mspaint",
    }
    print("1. Notepad\n2. Calculator\n3. Paint")
    c = input("Choose: ")
    if c in apps:
        os.system(apps[c])

def main():
    while True:
        print("\nWintool v1 nucaxem :D")
        print("1. Print custom text")
        print("2. Shutdown PC")
        print("3. Restart PC")
        print("4. Log out user")
        print("5. Lock workstation")
        print("6. List all local users")
        print("7. Create local user")
        print("8. Rename local user")
        print("9. Delete local user")
        print("10. Change user password")
        print("11. Change current username")
        print("12. Run program as invoker")
        print("13. Show Windows info")
        print("14. Show hardware info")
        print("15. Show local IP")
        print("16. Show public IP")
        print("17. Show active connections")
        print("18. Open Task Manager")
        print("19. Open Control Panel")
        print("20. Open Device Manager")
        print("21. Open Services")
        print("22. Open Registry Editor")
        print("23. Open Event Viewer")
        print("24. Startup apps folder")
        print("25. Empty Recycle Bin")
        print("26. Take screenshot")
        print("27. Show clipboard")
        print("28. Clear clipboard")
        print("29. Quick notepad")
        print("30. Batch file ops")
        print("31. Scheduled tasks")
        print("32. Hotkey manager")
        print("33. Adjust volume")
        print("34. Adjust brightness")
        print("35. App launcher")
        print("Q. Quit")

        c = input("Choose: ").lower()
        if c == "q": break

        try:
            c = int(c)
        except: continue

        if c == 1: print_custom_text()
        elif c == 2: os.system("shutdown /s /t 0")
        elif c == 3: os.system("shutdown /r /t 0")
        elif c == 4: os.system("shutdown /l")
        elif c == 5: lock_workstation()
        elif c == 6: os.system("net user")
        elif c == 7:
            u = input("Username: "); p = input("Password: ")
            os.system(f'net user {u} {p} /add')
        elif c == 8:
            old = input("Old username: "); new = input("New username: ")
            os.system(f'wmic useraccount where name="{old}" rename "{new}"')
        elif c == 9:
            u = input("Username: ")
            os.system(f'net user {u} /delete')
        elif c == 10:
            u = input("Username: "); p = input("New password: ")
            os.system(f'net user {u} {p}')
        elif c == 11: print("Limited in Windows") 
        elif c == 12:
            prog = input("Program path: ")
            os.system(f'psexec -i -d -s "{prog}"')
        elif c == 13: show_windows_info()
        elif c == 14: show_hardware_info()
        elif c == 15: os.system("ipconfig")
        elif c == 16: show_public_ip()
        elif c == 17: os.system("netstat -ano")
        elif c == 18: os.system("taskmgr")
        elif c == 19: os.system("control")
        elif c == 20: os.system("devmgmt.msc")
        elif c == 21: os.system("services.msc")
        elif c == 22: os.system("regedit")
        elif c == 23: os.system("eventvwr")
        elif c == 24: os.system("shell:startup")
        elif c == 25: empty_recycle_bin()
        elif c == 26: take_screenshot()
        elif c == 27: show_clipboard()
        elif c == 28: clear_clipboard()
        elif c == 29: quick_notepad()
        elif c == 30: batch_file_ops()
        elif c == 31: os.system("taskschd.msc")
        elif c == 32: hotkey_manager()
        elif c == 33: adjust_volume()
        elif c == 34: adjust_brightness()
        elif c == 35: open_launcher()
        else: print("Invalid.")

if __name__ == "__main__":
    main()