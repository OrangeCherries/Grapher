# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:07:41 2019

@author: jingxia
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os.path
from Grapher import make_graph, getdata

class interface:
    def __init__(self, window):
        self.window = window
        self.filename = ''
        self.cur_loc = '/'
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
        #getxy
        self.getxy_button = ttk.Button(window, text = 'get all', command = self.get_xy)
        self.getxy_button.grid(column = 2, row = 1)
        
    def add_x(self):
        self.filename_x = filedialog.askopenfilename(initialdir = self.cur_loc, title = "Select file")
        self.listbox_x.delete(0)
        self.listbox_x.insert(0, os.path.basename(self.filename_x))
        self.cur_loc = os.path.dirname(self.filename_x)
        
    def del_x(self):
        try:
            self.listbox_x.delete(self.listbox_x.curselection())
        except tk.TclError:
            pass
        
    def add_y(self):
        self.filename_y = filedialog.askopenfilename(initialdir = self.cur_loc, title = "Select file")
        self.listbox_y.insert(tk.END, os.path.basename(self.filename_y))
        self.cur_loc = os.path.dirname(self.filename_y)
        
    def del_y(self):
        try:
            self.listbox_y.delete(self.listbox_y.curselection())
        except tk.TclError:
            pass
        
    def get_xy(self):
        self.xfilename = self.listbox_x.get(0, tk.END)
        self.yfilename = self.listbox_y.get(0, tk.END)
        self.data = getdata(list(self.xfilename) + list(self.yfilename))
        make_graph(self.data)
    
    
root = tk.Tk()
gui = interface(root)
root.mainloop()