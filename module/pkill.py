#!/usr/bin/python
#coding:utf-8
import os, sys, traceback

def kill_proc(process_name):
    try:
        killed = os.system('tskill ' + process_name)
    except Exception:
        killed = 0
    return killed

proc = ['calculator', 'iexplore', 'cmd', 'chrome', 'firefox', 'opera', 'explorer', 'winlogon', 'wininit', ]

try:
    for prg in proc:
        kill_proc(prg)
except Exception:
    print("Error not proc found")
