# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:04:27 2019

@author: jingxia
"""

import matplotlib.pyplot as plt
import pandas as pd

class m_params:
    def __init__(self, logx, logy, graph):
        self.logx = logx
        self.logy = logy
        self.graph = graph
        
class params:
    def __init__(self, xlabel, ylabel, colours, xmin, xmax, ymin, ymax, xsize, ysize, title, legend, savename):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.colours = colours
        self.xlim = [xmin, xmax]
        self.ylim = [ymin, ymax]
        self.xsize = xsize
        self.ysize = ysize
        self.title = title
        self.legend = legend
        self.savename = savename

def getdata(filenames):
    data = []
    for file in filenames:
        df = pd.read_csv(file, header = None)
        df = df.squeeze().tolist()
        data.append(df)
    return data
    
def make_graph(args, m_params = None, params = None):
    x = args[0]
    ydata = []
    for i in range(1, len(args)):
        ydata.append(args[i])  
    fig1 = plt.figure()
    ax1 = fig1.add_subplot('111')
    #plot data
    #scatter, linear
    if(m_params.graph == 'S'):
        ls = 'None'
        ms= 'o'
    else:
        ls = '-'
        ms = ''
    #logx, logy parameters
    if(m_params.logx == 1 and m_params.logy == 1):
        for i in range(0, len(ydata)):
            if(len(params.colours) != 0):
                ax1.loglog(x, ydata[i], color = params.colours[i], linestyle = ls, marker = ms)
            else:
                ax1.loglog(x, ydata[i], linestyle = ls, marker = ms)
    elif(m_params.logx == 1 and m_params.logy == 0):
        for i in range(0, len(ydata)):
            if(len(params.colours) != 0):
                ax1.semilogx(x, ydata[i], color = params.colours[i], linestyle = ls, marker = ms)
            else:
                ax1.semilogx(x, ydata[i], linestyle = ls, marker = ms)
    elif(m_params.logx == 0 and m_params.logy == 1):
        for i in range(0, len(ydata)):
            if(len(params.colours) != 0):
                ax1.semilogy(x, ydata[i], color = params.colours[i], linestyle = ls, marker = ms)
            else:
                ax1.semilogy(x, ydata[i], linestyle = ls, marker = ms)
    else:
        for i in range(0, len(ydata)):
            if(len(params.colours) != 0):
                ax1.plot(x, ydata[i], color = params.colours[i], linestyle = ls, marker = ms)
            else:
                ax1.plot(x, ydata[i], linestyle = ls, marker = ms)
    ax1.grid()
    #optional parameters (labels, title, etc...)
    if params is not None:
        ax1.set_xlabel(params.xlabel)
        ax1.set_ylabel(params.ylabel)
        ax1.legend(params.legend.split(','))
        if(params.xlim == params.xlim and params.xlim[0] != '' and params.ylim[1] != 0):
            ax1.set_xlim([float(params.xlim[0]), float(params.xlim[1])])   
        if(params.ylim == params.ylim and params.ylim[0] != '' and params.ylim[1] != 0):
            ax1.set_ylim([float(params.ylim[0]), float(params.ylim[1])])  
        if params.xsize != '' and params.ysize != '' and float(params.xsize) > 0 and float(params.ysize) > 0 :
            fig1.set_size_inches(float(params.xsize), float(params.ysize))
        if params.title != '':
            ax1.set_title(params.title)
        if params.savename != '':
            fig1.savefig(params.savename, bbox_inches = 'tight')
    
    