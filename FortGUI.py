#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:48:59 2019

@author: ami
"""


try:
    # This will work in Python 2.7
    import Tkinter as tkinter
except ImportError:
    # This will work in Python 3.5
    import tkinter 
    
    
root = tkinter.Tk() #Create a window
mainLabel = tkinter.Label(text = "Fort Weather Data")
#mainLabel.pack()
root.mainloop()

