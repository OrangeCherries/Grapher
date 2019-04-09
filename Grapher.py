# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:04:27 2019

@author: jingxia
"""

import matplotlib.pyplot as plt
import pandas as pd

def getdata(filenames):
    data = []
    for file in filenames:
        df = pd.read_csv(file, header = None)
        df = df.squeeze().tolist()
        data.append(df)
    print(data)
    return data
    
def make_graph(args, xlabel = '', ylabel = '', legend = '', xlim = float('nan'), ylim = float('nan'), xsize = 0, ysize = 0, title = '', savename = '', params = float('nan')):
    x = args[0]
    ydata = []
    for i in range(1, len(args)):
        ydata.append(args[i])  
    fig1 = plt.figure()
    ax1 = fig1.add_subplot('111')
    for y in ydata:
        ax1.plot(x, y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.grid()
    ax1.legend(legend)
    if(xlim == xlim):
        ax1.set_xlim(xlim)   
    if(ylim == ylim):
        ax1.set_ylim(ylim)
    if xsize > 0 and ysize > 0:
        fig1.set_size_inches(xsize, ysize)
    if title != '':
        ax1.set_title(title)
    if savename != '':
        fig1.savefig(savename, bbox_inches = 'tight')
    
    