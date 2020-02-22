#!/usr/bin/env python3

"""
Authors
Santiago Guiral
Email: santiagoguiralwe@gmail.com
Emmanuel Gómez
Email: egoego2509@gmail.com
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

def animation(list_files):
    nplot = 0
    for file in list_files:
        nplot +=1
        ani = FuncAnimation(plt.gcf(),plotting(file), interval=1000)
        #ani.save('Plot_{}.mp4'.format(nplot))
        plt.show()

def plotting(file):
    df = pd.read_excel(file)
    print(df.columns)
    print('\n')
    print('Index the names of the columns to be plotted')
    print('If only one column is input, the plot is y-axis vs the sample lenght of the column')
    index = str(input("Input the name of the columns to be plotted (x-axis,y-axis): "))
    axis = index.split(',')
    print(axis)
    if len(axis) == 1:
        yaxis = df.loc[:,axis[0]]
        xaxis = np.arange(0,len(yaxis),1)
        xlabel, ylabel = "Sample",axis[0]
    else:
        xaxis = df.loc[:,axis[0]]
        yaxis = df.loc[:,axis[1]]
        xlabel, ylabel = axis[0],axis[1]
    plt.cla()
    #plt.ion()
    plt.plot(xaxis,yaxis,color='#ffa500')
    plt.tight_layout()
    plt.xlabel('{}'.format(xlabel))
    plt.ylabel('{}'.format(ylabel))
    plt.grid(color='#39ff14',linestyle=(0, (3, 10)))
