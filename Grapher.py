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
    
def make_graph(args, params = float('nan')):
    x = args[0]
    ydata = []
    for i in range(1, len(args)):
        ydata.append(args[i])  
    fig1 = plt.figure()
    ax1 = fig1.add_subplot('111')
    for y in ydata:
        ax1.plot(x, y)
    ax1.grid()
    if(False):
        ax1.set_xlabel(params.xlabel)
        ax1.set_ylabel(params.ylabel)
        ax1.grid()
        ax1.legend(params.legend)
        if(params.xlim == params.xlim and params.xlim != ''):
            ax1.set_xlim(params.xlim)   
        if(params.ylim == params.ylim and params.ylim != ''):
            ax1.set_ylim(params.ylim)
        if params.xsize > 0 and params.ysize > 0 and params.xsize != '' and params.ysize != '':
            fig1.set_size_inches(params.xsize, params.ysize)
        if params.title != '':
            ax1.set_title(params.title)
        if params.savename != '':
            fig1.savefig(params.savename, bbox_inches = 'tight')
    
    