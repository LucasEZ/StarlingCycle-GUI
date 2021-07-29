# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:27:12 2021

@author: lucas
"""


import tkinter as tk
from tkinter import ttk 
from Wigets import Wiget


class DataGrid():
    def __init__(self, gridOn, bgColor, gridColor, wg, ag, lwg, lsg, alpha):
        
        self.gridOn = gridOn
        if self.gridOn == None:
            self.gridOn = 0
        
        if not self.emptyValue(bgColor):
            self.bgColor = bgColor
        else:
            self.bgColor = "white"
            
        if not self.emptyValue(gridColor):
            self.gridColor = gridColor
        else:
            self.gridColor = "grey"
        
        if not self.emptyValue(wg):
            self.wg = wg
        else:
            self.wg = 'both'
        
        if not self.emptyValue(ag):
            self.ag = ag
        else: 
            self.ag = 'both'
            
        if not self.emptyValue(lwg):
            self.lwg = lwg
        else:
            self.lwg = 1
            
        if not self.emptyValue(lsg):
            self.lsg = lsg
        else:
            self.lsg = "--"
            
        if not self.emptyValue(alpha):
            self.alpha = alpha
        else:
            self.alpha = 0.5
            
        if not self.emptyValue(alpha):
            self.alpha = alpha
        else:
            self.alpha = 0.5    

    def update_data(self, gridOn, bgColor, gridColor, wg, ag, lwg, lsg, alpha):
        self.__init__(gridOn, bgColor, gridColor, wg, ag, lwg, lsg, alpha)

    def emptyValue(self, value):
        
        nan = ["", 0, None, '0']
        
        if value in nan:
            return True
        else:
            return False


'''
class SettingGrid(DataGrid):
    def __init__(self, frame, dataGrid, width=100, x=50, y=500, state=True):
        
        self.frame = frame
        
        self.btnGrid = tk.Button(frame, text="Color and Grid", width=width, command=lambda: self.openGridWindow(dataGrid))
        self.btnGrid.place(bordermode="outside", x=x, y=y)
        
    
    def openGridWindow(self, dataGrid):
        
        height = 500
        width = 520
        
        self.wg = tk.Toplevel(self.frame, height=height, width=width)
        
        self.wg.title("Color and grid parameters")
        self.wg.resizable(width=False, height=False)
        

        self.grid = Wiget(self.wg, 'Apply grid', (20, 10), "check", (190, 10))
            
        self.bgColor = Wiget(self.wg,'Background Color', (20, 60), "entry",
                         (190, 60), 
                         width=30,
                         need_color=True,
                         where="after")
                
        self.gridColor = Wiget(self.wg,'Grid Color', (20, 110), "entry",
                          (190, 110), 
                          width=30,
                          need_color=True,
                          where="after")
            
        self.whichGrid = Wiget(self.wg, 'Which Grid', (20, 160), "box",
                          (190, 160), 
                          width=25,
                          values=['major', 'minor', 'both'])
            
        self.axisGrid = Wiget(self.wg, 'Axis Grid', (20, 210), "box",
                         (190, 210), 
                         width=25,
                         values=['both', 'x', 'y'])
                
                
        self.lineStyleGrid = Wiget(self.wg,'Linestyle Grid', (20, 260), "box",
                        (190, 260), 
                        width=25,
                        values=['-', '--', '-.', ':', ''])
 
            
        self.lineWidthGrid = Wiget(self.wg,'Linewidth Grid', (20, 310), "spin",
                        (190, 310), 
                        width=10,
                        spin=[0, 100, 1])
                
            
        self.alphaGrid = Wiget(self.wg,'Alpha Grid', (20, 360),"spin",
                    (190, 360), 
                    width=10,
                    spin=[0, 1, 0.1])
            
        
        
        self.setGrid = ttk.Button(self.wg, text="Set and close", width=45, command=lambda: self.getValues(dataGrid))
        self.setGrid.place(bordermode="outside", x=20, y=400)
        
        
    def getValues(self, dataGrid):
        
        dataGrid.update_data(
                    self.grid.get_value(),
                    self.bgColor.get_value(),
                    self.gridColor.get_value(),
                    self.whichGrid.get_value(),
                    self.axisGrid.get_value(),
                    self.lineWidthGrid.get_value(),
                    self.lineStyleGrid.get_value(),
                    self.alphaGrid.get_value()
        )
    
    
        self.btnGrid["state"] = "normal"
        
        self.wg.destroy()
    
'''




