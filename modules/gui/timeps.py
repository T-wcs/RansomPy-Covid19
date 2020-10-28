#!/usr/bin/python3
#coding:utf-8
import time
from datetime import datetime
import timeit
import sys

class ErrorTimeException(Exception):
    def __init__(self, error=None):
        self.error = error

def set_time(hours, minutes, secondes):
    if(hours > 24):
        raise ErrorTimeException("Error hours set!")
    if(minutes > 60):
        raise ErrorTimeException("Error minutes set!")
    if(secondes > 60):
        raise ErrorTimeException("Error secondes set!")

    restart_secondes  = 60
    restart_minutes   = 60

    while True:
        secondes = int(secondes) - 1
        if(secondes == -1):
            minutes = int(minutes) - 1
            secondes = int(restart_secondes) - 1
            if(minutes == -1):
                hours = int(hours) - 1
                minutes = int(restart_minutes) - 1
        # add the values "0"
        hours = int(hours)
        if(hours < 10):
            hours = "0%d" %(hours)
        # add the values "0"
        minutes = int(minutes)
        if(minutes < 10):
            minutes = "0%d" %(minutes)
        # add the values "0"
        secondes = int(secondes)
        if(secondes < 10):
            secondes = "0%d" %(secondes)
        # To return iterator type
        yield "%s:%s:%s" %(hours, minutes, secondes)
