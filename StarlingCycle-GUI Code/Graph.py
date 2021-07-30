# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:30:14 2021

@author: lucas
"""
import re
import random

from Function import Function

class Graph():
    def __init__(self, equation, xi, yi, xf, yf, frec, typegraph, linecolor, label, linewidth):
        '''Clase para almacenar todos los datos ingresados relevantes de un grafico particular'''
        
        #creamos objeto function
        self.eq = Function(equation)
        #creamos la función 
        self.f = self.eq.createFunc()

        #almacenamos los datos de entrada evitando valores en blanco o valores no numéricos
        try:
            if not self.emptyValue(xi):
                self.xi = int(xi)
            else: 
                self.xi = 0
                
            if not self.emptyValue(yi):
                self.yi = int(yi)
            else: 
                self.yi = 0
            
            if not self.emptyValue(xf):
                self.xf = int(xf)
            else: 
                self.xf = 100
            
            if not self.emptyValue(yf):
                self.yf = int(yf)
            else: 
                self.yf = 0
            
            if not self.emptyValue(frec):
                self.frec = int(frec)
            else: 
                self.frec = 100
                
            if not self.emptyValue(typegraph):
                self.tipeGraph = typegraph
            else: 
                self.tipeGraph = "Lineal"

        except ValueError as e:
            self.xi = 0
            self.xf = 100
            self.yi = 0
            self.yf = 100
            self.frec = 100
     
        self.checkColor(linecolor)
        self.checkLabel(label)
        self.checkLineWidth(linewidth)

    def checkColor(self, color):
        '''Valida el color ingresado, en caso de no ser correcto, elige uno al azar'''
        if color != None:
            match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)
        else:
            match = False
        
        if match: 
            self.lineColor = color
        else:
            self.lineColor = self.lineColorRandom()
        
    def lineColorRandom(self):
        '''Genera un color random en hexadecimal'''
        rand = lambda: random.randint(100, 255)
        return '#%02X%02X%02X' % (rand(), rand(), rand())
        
    def checkLabel(self, label):
        '''Valida el label de entrada, si es una cadena vacia deja la ecuación por defecto'''
        if label == "":
            self.label = self.eq.eq
        else:
            self.label = label
    
    def checkLineWidth(self, width):
        '''Valida en ancho de línea'''
        if width == "0":
            self.lineWidth = 2
        else:
            self.lineWidth = width
    
    def emptyValue(self, value):
        '''método auxiliar empleado para evitar valores de entrada que afecten el funcionamiento
        del programa'''
        empty = [None, "", '0']
        
        if value in empty:
            return True
        else:
            return False
