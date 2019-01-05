#!/usr/bin/env python3.7

from tkinter import *
from tkinter import font
from tkiner import ttk
import time
import datetime

def quit(*args):
    root.destroy()

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000, clock_time)

