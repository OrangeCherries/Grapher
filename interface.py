# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:07:41 2019

@author: jingxia
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class interface:
    def __init__(self, window):
        self.window = window
        self.filename = ''
        window.title('Interface')
        window.geometry('350x200')
        
        self.file_button = ttk.Button(window, text = 'Load file', command = self.greet)
        self.file_button.grid(column = 0, row = 0)
        
    def greet(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        
root = tk.Tk()
gui = interface(root)
root.mainloop()