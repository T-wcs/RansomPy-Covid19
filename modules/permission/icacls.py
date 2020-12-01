#!/usr/bin/python
#coding:utf-8
import os
# VARIABLE ENVIRONMENT
letter_drive_path = os.environ["SystemDrive"]
get_usr_path      = os.environ["USERNAME"]

class GetPermission():
    """ Classe définissant les permissions de lecture, écriture sur les processus et répertoire"""
    def __init__(self):
        self.powershell_command = ['powershell.exe', 'powershell_ise.exe']
        self.windows_processus  = ['explorer.exe', 'notepad.exe']
        self.grant_permission   = "/grant {}:F".format(get_usr_path)
        self.grant_processus    = ['cmd.exe', 'taskmgr.exe', 'smartscreen.exe']
        self.directory_check    = ["{} \\Perflogs {}", "{} \\Perflogs\\* {}", "{} \\Perflogs\\gui_counter\\* {}", "{} \\Windows\\System {}"]
        self.processus_exec     = "START /MIN {}\\Windows\\System32\\icacls.exe".format(letter_drive_path)
        self.directory3         = "{}\\Windows\\System32\\WindowsPowerShell\\v1.0\\".format(letter_drive_path)
        self.directory2         = "{}\\Windows\\System32\\".format(letter_drive_path)
        self.directory          = "{}\\Windows\\".format(letter_drive_path)
    # Function to get full permission on the powershell, cmd and the taskmanager
    def proc(self):
        for proc in self.powershell_command:
            self.powershell_command = proc
            self.command_execute = "{} {}{} {}".format(self.processus_exec, self.directory3, self.powershell_command, self.grant_permission)
            os.system(self.command_execute)

        for proc in self.grant_processus:
            self.grant_processus = proc
            self.command_execute = "{} {}{} {}".format(self.processus_exec, self.directory2, self.grant_processus, self.grant_permission)
            os.system(self.command_execute)

        for proc in self.windows_processus:
            self.windows_processus = proc
            self.command_execute = "{} {}{} {}".format(self.processus_exec, self.directory, self.windows_processus, self.grant_permission)
            os.system(self.command_execute)
    # Function to gell full permission on the directory
    def dir(self):
        for i in self.directory_check:
            self.new_var = i.format(self.processus_exec, self.grant_permission)
            os.system(self.new_var)
