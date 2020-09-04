#!/usr/bin/python
#This Server will only run on a linux environment

import socket, thread, sys, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

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
	while 1:
		client_data  = clientSocket.recv(2048)
		if client_data :
			print client_data			
			clientSocket.send(client_data)
			password = Fernet.generate_key()
			print "Password is: " + password
			secret = keygen(password, addr[0])
			print "Key is: " + secret
			clientSocket.send(secret)
			
			print clientSocket.recv(2048)
			print "Chiffrement des données en cours..."
			clientSocket.close()
			break
		else :
			clientSocket.close()
			return

echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoServer.bind((sys.argv[1], int(sys.argv[2])))
echoServer.listen(10)

while 1:
	cSock, addr = echoServer.accept()
	# start a new thread to service 
	print "En attente de nouvelle connexion \n"
	print "Nouvelle connexion de %s: %s "%(addr)
	thread.start_new_thread(EchoClientHandler, (cSock, addr))
	


