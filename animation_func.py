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

def animation_plt(list_files):
    nplot = 0
    for file in list_files:
        same_plot=1
        while same_plot:
            nplot+=1
            ani = FuncAnimation(plt.gcf(),plotting(file,nplot), interval=1000)
            plt.show()
            wrong_key=1
            while wrong_key:        
                ch_plt=str(input("Do you want to plot another dataframe in the same file: [y/n] "))
                if ch_plt == 'y':
                    wrong_key=0
                    same_plot=1
                elif ch_plt =='n':
                    wrong_key=0
                    same_plot=0
                else:
                    wrong_key=1
            


def plotting(file,nplot):
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
    plt.plot(xaxis,yaxis,color='#ffa500')
    plt.tight_layout()
    plt.xlabel('{}'.format(xlabel))
    plt.ylabel('{}'.format(ylabel))
    plt.grid(color='#39ff14',linestyle=(0, (3, 10)))
    plt.savefig("figure{}.png".format(nplot))
