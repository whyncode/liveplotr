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

plt.style('dark_background')

def animation(list_files):
    for file in list_files:      
        plot = FuncAnimation(plt.gcf(),plotting(file), interval=0000.1)
        plt.show()

def plotting(file):
    df = pd.read_excel(file)
    print(df.columns)
    index = str(input("Input the name of the desired column to plot: ")) 
    yaxis = df.loc[:,index] 
    xaxis = np.arange(0,len(yaxis),1)
    plt.cla()
    plt.plot(xaxis,yaxis)
    plt.tight_layout()
    plt.grid()

