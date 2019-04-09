# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:07:41 2019

@author: jingxia
"""

import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import *
from tkinter import ttk
import os.path
from Grapher import make_graph, getdata

class interface:
    def __init__(self, window):
        self.window = window
        self.filename = ''
        self.cur_loc = '/'
        window.title('Interface')
        window.geometry('1000x500')
        #frame_x ( listbox + scrollbar )
        self.frame_x = tk.Frame(window)
        #xdata
        self.file_button_x = ttk.Button(self.frame_x, text = 'Load x data', command = self.add_x)
        self.file_button_x.grid(column = 0, row = 0)
        #x listbox
        self.listbox_xlabel = ttk.Label(self.frame_x, text = 'x data')
        self.listbox_xlabel.grid(column = 0, row = 1)
        self.listbox_x = tk.Listbox(self.frame_x, width = 40, height = 10)
        self.listbox_x.grid(column = 0, row = 2)
        #x listbox scrollbar
        scrollx = tk.Scrollbar(self.frame_x, orient = 'horizontal')
        scrollx.grid(column = 0, row = 3, sticky = 'EW')
        scrollx.config(command = self.listbox_x.xview)
        self.listbox_x.config(xscrollcommand = scrollx.set)
        #del x button
        self.del_button_x = ttk.Button(self.frame_x, text = 'Delete x data', command = self.del_x)
        self.del_button_x.grid(column = 0, row = 4)
        self.frame_x.grid(column = 0, row = 0)
        

        #frame_Y (listbox + scrollbar)
        self.frame_y = tk.Frame(window)
        #ydata
        self.file_button_y = ttk.Button(self.frame_y, text = 'Load y data', command = self.add_y)
        self.file_button_y.grid(column = 0, row = 0) 
        self.listbox_ylabel = ttk.Label(self.frame_y, text = 'y data')
        self.listbox_ylabel.grid(column = 0, row = 1)
        #listbox
        self.listbox_y = tk.Listbox(self.frame_y, width = 40, height = 10)
        self.listbox_y.grid(column = 0, row = 2)
        #listbox scrollbar
        scrolly = tk.Scrollbar(self.frame_y, orient = 'horizontal')
        scrolly.grid(column = 0, row = 3, sticky = 'EW')
        scrolly.config(command = self.listbox_y.xview)
        self.listbox_y.config(xscrollcommand = scrolly.set)
        #del y
        self.del_button_y = ttk.Button(self.frame_y, text = 'Delete y data', command = self.del_y)
        self.del_button_y.grid(column = 0, row = 4)
        self.frame_y.grid(column = 1, row = 0)
        
        #color picker frame
        self.frame_cp = tk.Frame(window)
        self.cp_button = ttk.Button(self.frame_cp, text = 'Choose Colour', command = self.add_cp)
        self.cp_button.grid(column = 0, row = 0)
        self.cp_label = ttk.Label(self.frame_cp, text = 'Colour')
        self.cp_label.grid(column = 0, row = 1)
        self.listbox_cp = tk.Listbox(self.frame_cp, width = 40, height = 10)
        self.listbox_cp.grid(column = 0, row = 2)
        self.del_cp_button = ttk.Button(self.frame_cp, text = 'Delete Colour', command = self.del_cp)
        self.del_cp_button.grid(column = 0, row = 3)
        self.frame_cp.grid(column = 2, row = 0)
                
        #Entry boxes
        self.frame_entry_boxes = tk.Frame(window)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'Title')
        self.title_label.grid(column = 0, row = 1)
        self.entry_title = ttk.Entry(self.frame_entry_boxes)
        self.entry_title.grid(column = 0, row = 2)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'X label')
        self.title_label.grid(column = 0, row = 3)
        self.entry_xlabel = ttk.Entry(self.frame_entry_boxes)
        self.entry_xlabel.grid(column = 0, row = 4)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'Y label')
        self.title_label.grid(column = 0, row = 5)
        self.entry_ylabel = ttk.Entry(self.frame_entry_boxes)
        self.entry_ylabel.grid(column = 0, row = 6)
        self.frame_entry_boxes.grid(column = 0, row = 4)
        #getxy
        self.getxy_button = ttk.Button(window, text = 'get all', command = self.get_graphs)
        self.getxy_button.grid(column = 5, row = 1)
        
    def add_x(self):
        self.filename_x = filedialog.askopenfilename(initialdir = self.cur_loc, title = "Select file")
        self.listbox_x.delete(0)
        self.listbox_x.insert(0, self.filename_x)
        self.cur_loc = os.path.dirname(self.filename_x)
        
    def del_x(self):
        try:
            self.listbox_x.delete(self.listbox_x.curselection())
        except tk.TclError:
            pass
        
    def add_y(self):
        self.filename_y = filedialog.askopenfilename(initialdir = self.cur_loc, title = "Select file")
        self.listbox_y.insert(tk.END, self.filename_y)
        self.cur_loc = os.path.dirname(self.filename_y)
        
    def del_y(self):
        try:
            self.listbox_y.delete(self.listbox_y.curselection())
        except tk.TclError:
            pass
        
    def add_cp(self):
        self.color = tk.colorchooser.askcolor()
        self.listbox_cp.insert(tk.END, self.color[1])
        try:
            self.listbox_cp.itemconfig(tk.END, {'fg': self.color[1]})
        except tk.TclError:
            pass
        
    def del_cp(self):
        try:
            self.listbox_cp.delete(self.listbox_cp.curselection())
        except tk.TclError:
            pass
        
    def get_graphs(self):
        self.xfilename = self.listbox_x.get(0, tk.END)
        self.yfilename = self.listbox_y.get(0, tk.END)
        self.xlabel = self.entry_xlabel.get()
        self.ylabel = self.entry_ylabel.get()

        #self.data = getdata(list(self.xfilename) + list(self.yfilename))
        #make_graph(self.data)
    
    
root = tk.Tk()
root.resizable(False, False)
gui = interface(root)
root.mainloop()