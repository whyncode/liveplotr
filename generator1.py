"""
Authors
-------
Emmanuel Gomez Ospina
egoego2509@gmail.com

Santiago Guiral
santiagoguiralwe@gmail.com

Description
-----------
This file is used to be a custom unit test
with the target of generate random numeric
cells in a async way so the liveplotr dis-
plays it.

"""
import threading as td
import pandas as pd
import numpy as np
from time import sleep

#unit test **constants**
TARGET_FILE="./targets/test1.xlsx"
UPDATE_DELAY=0.5
X_INCREMENT=UPDATE_DELAY*2.2

#initalizing dict to be exported as xlsx
l={"$x$":list(), "$y$":list()}

def random_stuff(x):
    #random number generation
    l["$y$"].append(10*np.random.randn())
    l["$x$"].append(x)

def write():
    x=0
    while(t_interact.is_alive()):
        random_stuff(x)
        x+=X_INCREMENT
        df=pd.DataFrame(l)
        df.to_excel(TARGET_FILE)
        print(f"{TARGET_FILE} updated")
        sleep(UPDATE_DELAY)

def interact():
    ans=input("type RETURN/ENTER/INTRO to stop.\n")

#starting functions in different threads:
t_write=td.Thread(target=write)
t_interact=td.Thread(target=interact)
t_interact.start()
t_write.start()
t_write.join()
t_interact.join()
t_write._stop()
t_interact._stop()
