#!/usr/bin/python
#coding:utf-8
import os, sys
# Variable ENVIRONMENT
u = os.environ["USERNAME"]
# Function to kill a process with force option (this function used in the main program)
def exp():
    try:
        killed = "\\Windows\\System\\c.exe /c \\Windows\\System32\\taskkill.exe /IM explorer.exe /f"
        os.system(killed)
    except Exception:
        killed = 0
    return killed

exp()
