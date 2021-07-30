# -*- coding: utf-8 -*-
"""
Created on Sat May 15 16:34:03 2021

@author: lucas
"""

class DataLegend():
    def __init__(self, legendOn, loc, shadow, xLabel, yLabel, fontSize, sizeBox):
        
        self.legendOn = legendOn
        if self.legendOn == None:
            self.legendOn = 0
        
        if not self.emptyValue(loc):
            self.loc = loc
        else: 
            self.loc = 'best'
        
        if not self.emptyValue(shadow):
            self.shadow = shadow
        else: 
            self.shadow = False
        
        if not self.emptyValue(xLabel):
            self.xLabel = xLabel
        else: 
            self.xLabel = 'x'
        
        if not self.emptyValue(yLabel):
            self.yLabel = yLabel
        else: 
            self.yLabel = 'y'
        
        if not self.emptyValue(fontSize):
            self.fontSize = fontSize
        else: 
            self.fontSize = 10
            
        if not self.emptyValue(sizeBox):
            self.sizeBox = float(sizeBox)
        else:
            self.sizeBox = 11
        

    
    def update_data(self, legendOn, loc, shadow, xLabel, yLabel, fontSize, sizeBox):
        self.__init__(legendOn, loc, shadow, xLabel, yLabel, fontSize, sizeBox)

    def emptyValue(self, value):
        
        nan = ["", 0, None]
        
        if value in nan:
            return True
        else:
            return False


