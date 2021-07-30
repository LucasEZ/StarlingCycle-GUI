# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:33:36 2021

@author: lucas
"""

import tkinter as tk

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit 

from Function import Function
from Wigets import ConfigFitPanel, CanvasFrame
from Grid import  DataGrid
from Legends import DataLegend
from Plot import Plot


class PanelFit():
    def __init__(self, root, fitNotebook, fitFrame, df):
        
        self.root = root
        self.fitNotebook = fitNotebook
        self.fitFrame = fitFrame
        
        #Inicializacción de variables y clases 
        self.df = df
        self.dataGrid = DataGrid(0,0,0,0,0,0,0,0)
        self.dataLegend = DataLegend(0,0,0,0,0,0,0)
        self.dataGraph = [] 
        
        
        panel = ConfigFitPanel(self.fitNotebook, self.df, self.dataGrid, self.dataLegend)
        
        self.btn_fit = tk.Button(panel.fitLabel, text="Curve Fit", width= 70, command = lambda: self.curveFit(panel))
        self.btn_fit.place(bordermode="outside", x=10, y=250)
        
    def read_variables(self, panel):
        '''Función para leer los inputs y inicializar variables que los contendrán'''
        
        #generamos el objeto función con el input ecuación
        eq = panel.eq.get_value()
        self.f = Function(eq)
    
        
        #Cargamos datos para seleccionar los archivos
        self.xCol = panel.x.get_value()
        self.yCol = panel.y.get_value()
        self.xfrom = int(panel.xfrom.get_value())
        self.xto = int(panel.xto.get_value())
        self.yfrom = int(panel.yfrom.get_value())
        self.yto = int(panel.yto.get_value())
        
        #tipo de datos en x e y
        self.xtype = panel.xtype.get_value()
        self.ytype = panel.ytype.get_value()
        
        #formato del tipo de datos de x e y
        self.xformat = panel.xformat.get_value()
        self.yformat = panel.yformat.get_value()
        
        #número de variables en la ecuación de ajusste
        self.nv = int(panel.nvar.get_value())
        
        #Valores semillas
        self.seed = self.seedTreatment(panel.seed.get_value(), self.nv)        
        #intentos de fiteo para obtener la curva más óptima
        self.attempts =  self.checkAttemps(panel.attemps.get_value())
        
        
        #variables relacionadas al estilo del gráfico
        #color linea y de punto
        self.color = panel.color.get_value()
        self.markerColor = panel.marketColor.get_value()
        #tipo de marcador
        self.marker = panel.market.get_value()
        #nombre de la series
        self.labelPoint = panel.labelPoint.get_value()
        self.labelFit = panel.labelFit.get_value()
       
        
    def curveFit(self, panel):
        '''Funcion que se ejecuta al apretar boton fit'''
        #leer datos inputs por usuario
        self.read_variables(panel)
        
        #detecta el número de variables en la ecuación
        nv = self.f.detectVariables()
        
        if len(nv) == self.nv:
            
            #crea la funcion de n variables
            ff =  self.f.createFunc()
            
            #array de datos en x
            x, xflag = self.dataTreatment(self.xCol, self.xfrom, self.xto, self.xtype, self.xformat)
            
            #array de datos en y
            y, yflag = self.dataTreatment(self.yCol, self.yfrom, self.yto, self.ytype, self.yformat)
            
            if xflag == False or yflag == False:
                panel.plotLabel.destroy()
                panel.fitLabel.destroy()
                self.__init__(self.root, self.fitNotebook, self.fitFrame, self.df)
                
            else:
                if len(x)==len(y):
                    
                    #ajuste la función
                    p, er = curve_fit(ff, x, y, p0=self.seed, maxfev=self.attempts)              
                    
                    self.f.chargeFitParameters(p, er)
                    
                    #reemplaza en la ecuación las variables ajustados por los parámetros óptimos del ajuste
                    self.f.replaceVariables()         
        
                    #evalua la función ajustada en una grilla de valores de x teóricos
                    x_grid, y_grid = self.f.getFitData(x)
                
                    #muestra en pantalla resultados
                    self.show_fit_frame(panel, x_grid, y_grid, x, y)
                
                else:
                    #evita el error de datos incompletos
                    panel.plotLabel.destroy()
                    panel.fitLabel.destroy()
                    self.__init__(self.root, self.fitNotebook, self.fitFrame, self.df)
    

    def show_fit_frame(self, panel, x_grid, y_grid, x_exp, y_exp):
        
        #objeto gráfico
        plot = Plot(self.dataGrid, self.dataLegend)
        
        #Crear figura con los datos
        plot.graphicFit(x_exp, y_exp, x_grid, y_grid, 
                        color=self.color, 
                        c_marker=self.markerColor, 
                        label=self.labelPoint, 
                        label_fit=self.labelFit,
                        marker=self.marker)
        
        #Visualizar figura en fitFrame 
        c = CanvasFrame(self.fitFrame, self.f, plot.fig, x_grid, y_grid, x_exp, y_exp)
        
        
    def seedTreatment(self, seeds, nv):
        '''verificacion de valores semillas'''
        #separamos valores en lista por comas
        seedList = str(seeds).split(',')
    
        try:
            seed = [int(i) for i in seedList]
            #si el número de variables es igual a la cant de valores semillas
            if len(seed) == nv:
                return seed
            #si hay más valores semillas que variables deja como semilla de todos 1
            elif len(seed) > nv:
                return [ 1 for i in range(len(seed)+1)]
            #si hay menos valores semillas que variables completa con 1
            else:
                for i in range(nv-len(seed)):
                    seed.append(1)     
                return seed
            
        except ValueError:
            self.fitNotebook.destroy()
            self.__init__(self.root, self.fitNotebook, self.fitFrame, self.df)
        
    def dataTreatment(self, column, from_, to, type_, format_):
        
        #variable bandera
        flag = True
        #lista con el indice de filas 
        fil = [i for i in range(from_, to+1, 1)]
        #seleccionar las filas de la columna en el dataFrame
        v = self.df.loc[fil, column]    

        #análisis de formato de dato
        if type_ == "value":
            try:
                #probar con int
                if format_ == "int":
                    v.to_numpy(dtype=int)                 
                    v = v.astype(int)
                else:                
                    v = v.astype(float)
                
                return list(v), flag
            
            except ValueError as e:
                v = v.str.replace(',', ".")
                v = v.astype(float)
                
                return list(v), flag
        #si es dato de tiempo
        elif type_ == "datetime":
            try:
                v = pd.to_datetime(v, format=format_)
                return list(v), flag
            except:
                print("Please verify that the entered data format is correct")
                flag = False
                return None, flag
            
        
    def checkAttemps(self, attemps):
        '''define el número de intentos de ajuste, chequea que el valor cargado no sea cero'''
        if  attemps == 0:
            fev = 1000
        else:
            fev = int(attemps)
            
        return fev
    
