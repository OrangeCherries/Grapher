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

class params:
    def __init__(self, xlabel, ylabel, xmin, xmax, ymin, ymax, xsize, ysize, title, legend, savename):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = [xmin, xmax]
        self.ylim = [ymin, ymax]
        self.xsize = xsize
        self.ysize = ysize
        self.title = title
        self.legend = legend
        self.savename = savename
    
    def get(self):
        print('xlabel ', self.xlabel)
        print('ylabel ', self.ylabel)
        print('xlim ', self.xlim)
        print('ylim ', self.ylim)
        print('xsize', self.xsize)
        print('ysize', self.ysize)
        print('title ', self.title)
        print('legend ', self.legend)
        print('savename', self.savename)
        
class interface:
    def __init__(self, window):
        self.window = window
        self.filename = ''
        self.cur_loc = '/'
        
        window.title('Interface')
        #frame_x ( listbox + scrollbar )
        self.frame_x = tk.Frame(window)
        #xdata
        self.file_button_x = ttk.Button(self.frame_x, text = 'Load x data', command = self.add_x)
        self.file_button_x.grid(column = 0, row = 0)
        #x listbox
        self.listbox_xlabel = ttk.Label(self.frame_x, text = 'x data')
        self.listbox_xlabel.grid(column = 0, row = 1)
        self.listbox_x = tk.Listbox(self.frame_x, width = 40, height = 10, bd = 3, relief = 'groove')
        self.listbox_x.grid(column = 0, row = 2)
        #x listbox scrollbar
        scrollx = tk.Scrollbar(self.frame_x, orient = 'horizontal')
        scrollx.grid(column = 0, row = 3, sticky = 'EW')
        scrollx.config(command = self.listbox_x.xview)
        self.listbox_x.config(xscrollcommand = scrollx.set)
        #del x button
        self.del_button_x = ttk.Button(self.frame_x, text = 'Delete x data', command = self.del_x)
        self.del_button_x.grid(column = 0, row = 4)
        self.frame_x.grid(column = 0, row = 0, sticky = 'N')
        

        #frame_Y (listbox + scrollbar)
        self.frame_y = tk.Frame(window)
        #ydata
        self.file_button_y = ttk.Button(self.frame_y, text = 'Load y data', command = self.add_y)
        self.file_button_y.grid(column = 0, row = 0) 
        self.listbox_ylabel = ttk.Label(self.frame_y, text = 'y data')
        self.listbox_ylabel.grid(column = 0, row = 1)
        #listbox
        self.listbox_y = tk.Listbox(self.frame_y, width = 40, height = 10, bd = 3, relief = 'groove')
        self.listbox_y.grid(column = 0, row = 2)
        #listbox scrollbar
        scrolly = tk.Scrollbar(self.frame_y, orient = 'horizontal')
        scrolly.grid(column = 0, row = 3, sticky = 'EW')
        scrolly.config(command = self.listbox_y.xview)
        self.listbox_y.config(xscrollcommand = scrolly.set)
        #colour picker
        self.cp_button = ttk.Button(self.frame_y, text = 'Choose Colour', command = self.add_cp)
        self.cp_button.grid(column = 1, row = 2)
        self.cp_bool = tk.IntVar()
        self.cp_bool.set(0)
        self.cp_cbox = ttk.Checkbutton(self.frame_y, text = 'Use choose colour', variable = self.cp_bool)
        self.cp_cbox.grid(column = 1, row = 1)
        #del y
        self.del_button_y = ttk.Button(self.frame_y, text = 'Delete y data', command = self.del_y)
        self.del_button_y.grid(column = 0, row = 4)
        self.frame_y.grid(column = 1, row = 0, sticky = 'N')
        
                
        #Entry boxes
        # title and labels
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
        
        # x y min max
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'Properties')
        self.title_label.grid(column = 1, row = 0, columnspan = 2)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'x min')
        self.title_label.grid(column = 1, row = 2)
        self.entry_xmin = ttk.Entry(self.frame_entry_boxes)
        self.entry_xmin.grid(column = 1, row = 3)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'x max')
        self.title_label.grid(column = 2, row = 2)
        self.entry_xmax = ttk.Entry(self.frame_entry_boxes)
        self.entry_xmax.grid(column = 2, row = 3)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'y min')
        self.title_label.grid(column = 1, row = 4)
        self.entry_ymin = ttk.Entry(self.frame_entry_boxes)
        self.entry_ymin.grid(column = 1, row = 5)
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'y max')
        self.title_label.grid(column = 2, row = 4)
        self.entry_ymax = ttk.Entry(self.frame_entry_boxes)
        self.entry_ymax.grid(column = 2, row = 5)
        #legend
        self.legend_label = ttk.Label(self.frame_entry_boxes, text = 'Legend')
        self.legend_label.grid(column = 1, row = 6, columnspan = 2)
        self.entry_legend = ttk.Entry(self.frame_entry_boxes)
        self.entry_legend.grid(column = 1, row = 7, columnspan = 2)
        #savename
        self.savename_label = ttk.Label(self.frame_entry_boxes, text = 'Save as:')
        self.savename_label.grid(column = 1, row = 8, columnspan = 2)
        self.entry_savename = ttk.Entry(self.frame_entry_boxes)
        self.entry_savename.grid(column = 1, row = 9, columnspan = 2)
        #xsize ysize
        self.xsize_label = ttk.Label(self.frame_entry_boxes, text = 'width')
        self.xsize_label.grid(column = 3, row = 1)
        self.entry_xsize = ttk.Entry(self.frame_entry_boxes)
        self.entry_xsize.grid(column = 3, row = 2)
        self.ysize_label = ttk.Label(self.frame_entry_boxes, text = 'height')
        self.ysize_label.grid(column = 4, row = 1)
        self.entry_ysize = ttk.Entry(self.frame_entry_boxes)
        self.entry_ysize.grid(column = 4, row = 2)
        
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
        if(self.cp_bool.get() == 1):
            self.color = tk.colorchooser.askcolor()
            try:
                self.listbox_y.itemconfig(self.listbox_y.curselection(), {'fg': self.color[1]})
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
        self.title = self.entry_title.get()
        self.savename = self.entry_savename.get()
        self.xmin = self.entry_xmin.get()
        self.xmax = self.entry_xmax.get()
        self.ymin = self.entry_ymin.get()
        self.ymax = self.entry_ymax.get()
        self.xsize = self.entry_xsize.get()
        self.ysize = self.entry_ysize.get()
        self.legend = self.entry_legend.get()
        cur_params = params(self.xlabel, self.ylabel, self.xmin, self.xmax, self.ymin, self.ymax, self.xsize, self.ysize, self.title, self.legend, self.savename)
        cur_params.get()
        
        self.data = getdata(list(self.xfilename) + list(self.yfilename))
        make_graph(self.data, cur_params)
    
    
root = tk.Tk()
gui = interface(root)
root.mainloop()