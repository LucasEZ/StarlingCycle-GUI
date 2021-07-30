# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:50:24 2021

@author: lucas
"""

from MainApp import *


def Main():
    '''función de entrada al programa '''    
    
    root = tk.Tk()
    root.title("StarlingCycle GUI")
    root.state("zoomed")
    root.iconbitmap('ButtonImagen/logo.ico')
    window = MainApp(root)

    root.mainloop()
    
    
if __name__ == '__main__':
    Main()
    
    
    