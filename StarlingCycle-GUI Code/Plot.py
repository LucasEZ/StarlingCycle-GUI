# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 18:25:37 2021

@author: lucas
"""


import numpy as np
import matplotlib.pyplot as plt 
from tkinter import messagebox



class Plot():
    def __init__(self, dataGrid, dataLegend):    
        '''Clase generadora de figuras y gráficos'''
        
        self.dataGrid = dataGrid
        self.dataLegend = dataLegend
        
        self.fig, self.ax = plt.subplots()
    
        try:
            self.ax.set_facecolor(dataGrid.bgColor)
        except ValueError:
            self.ax.set_facecolor("white")

    def graphic(self, dataGraph):
        '''método para graficar data guardada en dataGraph (funcionalidad graficar)'''
        for graph in dataGraph:
            #generamos plantilla de x a evaluar
            x = np.linspace(graph.xi, graph.xf, num=graph.frec)
            try:
                #tomamos la función
                f = graph.f 
                #evaluamos plantilla de x en f
                fx = f(x)
                
                #generamos plot
                if graph.tipeGraph == "Lineal":
                    self.ax.plot(x, fx, color=graph.lineColor, label=graph.label, linewidth=graph.lineWidth)
                if graph.tipeGraph == "Scatter":
                    self.ax.scatter(x, fx, color=graph.lineColor, label=graph.label, linewidth=graph.lineWidth )
            except SyntaxError or ValueError or ZeroDivisionError as e:
                messagebox.showerror("Alert", f"Error : {graph.eq}:\n {e}")
            
            #si se dejan igual los límites, se ajusta solo el eje y
            if graph.yi != graph.yf:
                self.ax.set_ylim(graph.yi, graph.yf)
                
            #seteamos labels
            self.ax.set_xlabel(self.dataLegend.xLabel)
            self.ax.set_ylabel(self.dataLegend.yLabel)
             

        #configuración grilla
        if self.dataGrid.gridOn == 1:
            self.grid()
        
        #configuración leyendas
        if self.dataLegend.legendOn == 1:
            self.legend()
        
        #devuelve figura
        return self.fig
    
    
    def graphicFit(self, x_exp, y_exp, x_grid, y_grid, color="orange", c_marker="black", label="Data", label_fit="Fit", marker="o"):
        '''método para graficar ajustes de datos con sus respectivos datos experimentales. Funcionalidad
        ajuste de datos'''
        
        self.fig.figsize=(5,5) 
        self.fig.dpi=100
        
        #genera scatter de datos exp
        self.ax.scatter(x_exp, y_exp, c=c_marker, label=label, marker=marker)
        #línea continua de funcion ajustada
        self.ax.plot(x_grid, y_grid, color=color ,label=label_fit)
        
        #configuración grilla
        if self.dataGrid.gridOn == 1:
            self.grid()
        
        #configuración leyendas
        if self.dataLegend.legendOn == 1:
            self.legend()
            
    def grid(self):
        '''método para configurar grilla'''
        self.ax.grid(b=True,
                     which= self.dataGrid.wg, 
                     axis= self.dataGrid.ag, 
                     color= self.dataGrid.gridColor, 
                     linewidth= self.dataGrid.lwg,
                     linestyle= self.dataGrid.lsg,
                     alpha= float(self.dataGrid.alpha))
        
    def legend(self):
        '''método para configurar leyenda'''
        self.ax.legend(loc=self.dataLegend.loc,
                       prop={'size':self.dataLegend.sizeBox},
                       shadow = self.dataLegend.shadow,
                       fontsize = self.dataLegend.fontSize)
    
        self.ax.set_xlabel(self.dataLegend.xLabel)
        self.ax.set_ylabel(self.dataLegend.yLabel)
  