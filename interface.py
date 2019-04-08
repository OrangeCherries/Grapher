# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:07:41 2019

@author: jingxia
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os.path

class interface:
    def __init__(self, window):
        self.window = window
        self.filename = ''
        window.title('Interface')
        window.geometry('350x400')
        
        #xdata
        self.file_button_x = ttk.Button(window, text = 'Load x data', command = self.add_x)
        self.file_button_x.grid(column = 0, row = 0)
        self.listbox_xlabel = ttk.Label(window, text = 'x data')
        self.listbox_xlabel.grid(column = 0, row = 1)
        self.listbox_x = tk.Listbox(window)
        self.listbox_x.grid(column = 0, row = 2)
        self.del_button_x = ttk.Button(window, text = 'Delete x data', command = self.del_x)
        self.del_button_x.grid(column = 0, row = 3)
        #ydata
        self.file_button_y = ttk.Button(window, text = 'Load y data', command = self.add_y)
        self.file_button_y.grid(column = 1, row = 0)
        self.listbox_ylabel = ttk.Label(window, text = 'y data')
        self.listbox_ylabel.grid(column = 1, row = 1)
        self.listbox_y = tk.Listbox(window)
        self.listbox_y.grid(column = 1, row = 2)
        self.del_button_y = ttk.Button(window, text = 'Delete y data', command = self.del_y)
        self.del_button_y.grid(column = 1, row = 3)
        
    def add_x(self):
        self.filename_x = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        self.listbox_x.delete(0)
        self.listbox_x.insert(0, os.path.basename(self.filename_x))
        
    def del_x(self):
        try:
            self.listbox_x.delete(self.listbox_x.curselection())
        except tk.TclError:
            pass
        
    def add_y(self):
        self.filename_y = filedialog.askopenfilename(initialdir = "/", title = "Select file")
        self.listbox_y.insert(tk.END, os.path.basename(self.filename_y))
        
    def del_y(self):
        try:
            self.listbox_y.delete(self.listbox_y.curselection())
        except tk.TclError:
            pass
        
    
        
root = tk.Tk()
gui = interface(root)
root.mainloop()