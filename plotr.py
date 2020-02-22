#!/usr/bin/env python3

"""
Authors
Santiago Guiral
Email: santiagoguiralwe@gmail.com
Emmanuel Gómez
Email: egoego2509@gmail.com
"""

#Plotting live data

import argparse
import animation_func as af

def main():
    parser = argparse.ArgumentParser(description="Plots live data from an excel file")
    parser.add_argument('-f','--files',nargs='+',help="List of files to be plotted",required=True)
    args = parser.parse_args()
    print(args.files)
    af.animation(args.files)

if __name__ == "__main__":
    main()


