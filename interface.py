# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:07:41 2019

@author: jingxia
"""
"""
TODO:
    -use polyfit to enable trendlines
    -figure out how to implement linestyle property
    -enable .txt and .xlsx file types
    -change scrollers to self.
    -(maybe) change save system
"""
import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter import ttk
import os.path
from Grapher import make_graph, getdata, make_trendline, m_params, params
    
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
        self.listbox_xlabel = ttk.Label(self.frame_x, text = 'x data (load from file)')
        self.listbox_xlabel.grid(column = 0, row = 1)
        self.listbox_x = tk.Listbox(self.frame_x, width = 30, height = 10, bd = 3, relief = 'groove')
        self.listbox_x.grid(column = 0, row = 2)
        #x listbox scrollbar
        scrollx = tk.Scrollbar(self.frame_x, orient = 'horizontal')
        scrollx.grid(column = 0, row = 3, sticky = 'EW')
        scrollx.config(command = self.listbox_x.xview)
        self.listbox_x.config(xscrollcommand = scrollx.set)
        #del x button
        self.del_button_x = ttk.Button(self.frame_x, text = 'Delete x data', command = self.del_x)
        self.del_button_x.grid(column = 0, row = 4)
        self.frame_x.grid(column = 0, row = 0, padx = (10, 10))
        

        #frame_Y (listbox + scrollbar)
        self.frame_y = tk.Frame(window)
        #ydata
        self.file_button_y = ttk.Button(self.frame_y, text = 'Load y data', command = self.add_y)
        self.file_button_y.grid(column = 0, row = 0) 
        self.listbox_ylabel = ttk.Label(self.frame_y, text = 'y data (load from file)')
        self.listbox_ylabel.grid(column = 0, row = 1)
        #listbox
        self.listbox_y = tk.Listbox(self.frame_y, width = 30, height = 10, bd = 3, relief = 'groove')
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
        self.frame_y.grid(column = 1, row = 0, padx = (10, 10))
        
        #self entry data
        self.frame_data_entry = tk.Frame(window)
        self.data_entry_bool = tk.IntVar()
        self.data_entry_bool.set(0)
        self.data_entry_cb = ttk.Checkbutton(self.frame_data_entry, text = 'Input Data', variable = self.data_entry_bool, command = self.data_entry_switch)
        self.data_entry_cb.grid(column = 0, row = 0)
        self.xdata_entry_label = ttk.Label(self.frame_data_entry, text = 'x data')
        self.xdata_entry_label.grid(column = 0, row = 1)
        self.xdata_entry = tk.Text(self.frame_data_entry, width = 10, height = 10, bd = 3, relief = 'groove', state = 'disabled')
        self.xdata_entry.grid(column = 0, row = 2)
        self.scroll_x_entry = tk.Scrollbar(self.frame_data_entry, orient = 'vertical')
        self.scroll_x_entry.grid(column = 1, row = 2, sticky = 'NS')
        self.scroll_x_entry.config(command = self.xdata_entry.yview)
        self.xdata_entry.config(yscrollcommand = self.scroll_x_entry.set)
        
        self.ydata_entry_label = ttk.Label(self.frame_data_entry, text = 'y data')
        self.ydata_entry_label.grid(column = 2, row = 1)
        self.ydata_entry = tk.Text(self.frame_data_entry, width = 10, height = 10, bd = 3, relief = 'groove', state = 'disabled')
        self.ydata_entry.grid(column = 2, row = 2)
        self.scroll_y_entry = tk.Scrollbar(self.frame_data_entry, orient = 'vertical')
        self.scroll_y_entry.grid(column = 3, row = 2, sticky = 'NS')
        self.scroll_y_entry.config(command = self.ydata_entry.yview)
        self.ydata_entry.config(yscrollcommand = self.scroll_y_entry.set)
        
        self.frame_data_entry.grid(column = 3, row = 0)
                
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
        self.entry_xmin = ttk.Entry(self.frame_entry_boxes, width = 10)
        self.entry_xmin.grid(column = 1, row = 3, padx = (1, 1))
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'x max')
        self.title_label.grid(column = 2, row = 2)
        self.entry_xmax = ttk.Entry(self.frame_entry_boxes, width = 10)
        self.entry_xmax.grid(column = 2, row = 3, padx = (1, 1))
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'y min')
        self.title_label.grid(column = 1, row = 4)
        self.entry_ymin = ttk.Entry(self.frame_entry_boxes, width = 10)
        self.entry_ymin.grid(column = 1, row = 5, padx = (1, 1))
        self.title_label = ttk.Label(self.frame_entry_boxes, text = 'y max')
        self.title_label.grid(column = 2, row = 4)
        self.entry_ymax = ttk.Entry(self.frame_entry_boxes, width = 10)
        self.entry_ymax.grid(column = 2, row = 5, padx = (1, 1))
        #legend
        self.legend_label = ttk.Label(self.frame_entry_boxes, text = 'Legend')
        self.legend_label.grid(column = 1, row = 6, columnspan = 2)
        self.entry_legend = ttk.Entry(self.frame_entry_boxes)
        self.entry_legend.grid(column = 1, row = 7, columnspan = 2)
        #savename
        self.savename_label = ttk.Label(self.frame_entry_boxes, text = 'Save as:')
        self.savename_label.grid(column = 1, row = 8, columnspan = 2)
        self.entry_savename = ttk.Entry(self.frame_entry_boxes)
        self.entry_savename.grid(column = 1, row = 9, columnspan = 2, pady = (0, 2))
        #xsize ysize
        self.xsize_label = ttk.Label(self.frame_entry_boxes, text = 'width')
        self.xsize_label.grid(column = 3, row = 1)
        self.entry_xsize = ttk.Entry(self.frame_entry_boxes)
        self.entry_xsize.grid(column = 3, row = 2)
        self.ysize_label = ttk.Label(self.frame_entry_boxes, text = 'height')
        self.ysize_label.grid(column = 4, row = 1)
        self.entry_ysize = ttk.Entry(self.frame_entry_boxes)
        self.entry_ysize.grid(column = 4, row = 2)
        #graph type
        self.graph_type = tk.StringVar()
        self.graph_type.set('L')
        self.graph_menu_L = tk.Radiobutton(self.frame_entry_boxes, text = 'Linear', variable = self.graph_type, value = 'L')
        self.graph_menu_L.grid(column = 3, row = 3)
        self.graph_menu_S = tk.Radiobutton(self.frame_entry_boxes, text = 'Scatter', variable = self.graph_type, value = 'S')
        self.graph_menu_S.grid(column = 3, row = 4)
        #axis type
        self.logx_bool = tk.IntVar()
        self.logx_bool.set(0)
        self.logy_bool = tk.IntVar()
        self.logy_bool.set(0)
        self.logx_cb = tk.Checkbutton(self.frame_entry_boxes, text = 'x axis log', variable = self.logx_bool)
        self.logx_cb.grid(column = 4, row = 3)
        self.logy_cb = tk.Checkbutton(self.frame_entry_boxes, text = 'y axis log', variable = self.logy_bool)
        self.logy_cb.grid(column = 4, row = 4)
        #trendline options
        self.tl_line_bool = tk.IntVar()
        self.tl_line_bool.set(0)
        self.tl_eq_bool = tk.IntVar()
        self.tl_eq_bool.set(0)
        self.tl_y_bool = tk.IntVar()
        self.tl_y_bool.set(0)
        self.tl_line_cb = tk.Checkbutton(self.frame_entry_boxes, text = 'Show trendline', variable = self.tl_line_bool)
        self.tl_line_cb.grid(column = 3, row = 6, sticky = 'W')
        self.tl_line_cb = tk.Checkbutton(self.frame_entry_boxes, text = 'Show Equation', variable = self.tl_eq_bool)
        self.tl_line_cb.grid(column = 3, row = 7, sticky = 'W')
        self.tl_y_cb = tk.Checkbutton(self.frame_entry_boxes, text = 'Force y(0) = 0', variable = self.tl_y_bool)
        self.tl_y_cb.grid(column = 3, row = 8, sticky = 'W')
        
        self.frame_entry_boxes.grid(column = 0, row = 4, columnspan = 2)
        
        #getxy
        self.getxy_button = ttk.Button(window, text = 'get all', command = self.get_graphs)
        self.getxy_button.grid(column = 5, row = 1)
    def data_entry_switch(self):
        if self.xdata_entry['state'] == 'disabled':
            self.xdata_entry['state'] = 'normal'
            self.ydata_entry['state'] = 'normal'
        elif self.xdata_entry['state'] == 'normal':
            self.xdata_entry['state'] = 'disabled'
            self.ydata_entry['state'] = 'disabled'
        
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
        if self.listbox_y.size() <= 10:
            self.filename_y = filedialog.askopenfilename(initialdir = self.cur_loc, title = "Select file")
            self.listbox_y.insert(tk.END, self.filename_y)
            self.cur_loc = os.path.dirname(self.filename_y)
        
    def del_y(self):
        try:
            self.listbox_y.delete(self.listbox_y.curselection())
        except tk.TclError:
            pass
        
    def add_cp(self):
        if(self.cp_bool.get() == 1 and self.listbox_y.curselection() != ()):
            self.color = askcolor()
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
        #if load data is used
        if self.data_entry_bool.get() == 0:
            self.xfilename = self.listbox_x.get(0, tk.END)
            self.yfilename = self.listbox_y.get(0, tk.END)
            self.ycolours = []
            if(self.cp_bool.get() == 1):
                for i in range(0, self.listbox_y.size()):
                    if self.listbox_y.itemcget(i, option = 'foreground') == '':
                        self.ycolours.append('#000000')
                    else:
                        self.ycolours.append(self.listbox_y.itemcget(i, option = 'foreground'))
            self.data = getdata(list(self.xfilename) + list(self.yfilename))
            
        #if data entry is used    
        elif self.data_entry_bool.get() == 1:
            #too lazy to learn regex, so .replace() it is
            self.ycolours = []
            self.xdata_e = [float(val) for val in self.xdata_entry.get('1.0', 'end-1c').replace('\r', ' ').replace('\n', ' ').replace(',', ' ').split()]
            self.ydata_e = [float(val) for val in self.ydata_entry.get('1.0', 'end-1c').replace('\r', ' ').replace('\n', ' ').replace(',', ' ').split()]
            self.data = [self.xdata_e, self.ydata_e]
        """
        for i in range(1, len(self.data)):
            self.trendline = make_trendline(self.data[0], self.data[i])
            self.data
        """
        
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
        self.logx = self.logx_bool.get()
        self.logy = self.logy_bool.get()
        self.graph = self.graph_type.get()
        
        cur_params = params(self.xlabel, self.ylabel, self.ycolours, self.xmin, self.xmax, self.ymin, self.ymax, self.xsize, self.ysize, self.title, self.legend, self.savename)
        cur_m_params = m_params(self.logx, self.logy, self.graph)
        make_graph(self.data, cur_m_params, cur_params)
        
root = tk.Tk()
gui = interface(root)
root.mainloop()