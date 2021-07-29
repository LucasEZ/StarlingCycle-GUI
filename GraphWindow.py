# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:56:15 2021

@author: lucas

version 2 de GraphWindow

"""

import tkinter as tk
from tkinter import ttk

from Plot import Plot
from Graph import Graph
from Grid import DataGrid
from Legends import DataLegend
from Wigets import EqEntry, StyleEntry, SettingGrid, SettingLegend, Canvas

class GraphWindow():
    def __init__(self, root, windowNote):
        '''Clase principal de la funcionalidad graficar. Cuenta con dos paneles: uno de 
        configuracion para setear todo lo relativo a la función y el estilo de gráfico y
        otro de visualización'''
        
        #inicializamos la raiz
        self.root = root
        
        #Inicializamos las clases donde se almacenan todas las variables para los gráficos
        self.dataGrid = DataGrid(0,0,0,0,0,0,0,0)
        self.dataLegend = DataLegend(0,0,0,0,0,0,0)
        self.dataGraph = [] 
        
        
        #Generate the workframe in which we will set and made the graphics
        self.graphWindow = tk.Frame(windowNote, height=700, width=1000)
        windowNote.add(self.graphWindow, text='Graph')
        
        #Panel de configuración para el ploteo
        self.panelFrame = tk.Frame(self.graphWindow,height=600, width=500)
        self.panelFrame.pack(side='left',expand=False, fill="both",anchor="nw")
    
        #Agregamos label frame para ingresar todo lo relacionado a la función
        eqPanel = EqEntry(self.panelFrame, height=200, width=420, x=50, y=20)        
        
        #Agregamos label frame para ingresar todo lo relacionado al estilo de gráfico
        stylePanel = StyleEntry(self.panelFrame, height=200, width=420, x=50, y=225)
        
        #agrega boton para configurar lo relativo a grilla y el color
        SettingGrid(self.panelFrame, self.dataGrid, width=20)
        
        #agrega boton para configurar lo relativo a legendas
        SettingLegend(self.panelFrame, self.dataLegend, width=20, x=200, y=500)    
        
        #Creamos el panel de visualización
        self.panelGraph = tk.Frame(self.graphWindow,height=700, width=500, bg="white")
        self.panelGraph.pack(side='right',expand=True, fill="both")
        
        
        self.buttons = {
            "btnOther" : (tk.Button(self.panelFrame, text="Others", width= 10, command = self.setOther), 400, 500),
            "btnSave" : (ttk.Button(self.panelFrame, text="Save to graph", width= 75, command = lambda: self.saveDataPlot(eqPanel, stylePanel)),22,550),
            "btnGraph": (ttk.Button(self.panelFrame, text="Graph", width= 75, command = self.plotGraphics),22,580)
            }
        
        
        for btn in self.buttons:
            
            x = self.buttons[btn][1]
            y = self.buttons[btn][2]
            
            self.buttons[btn][0].place(bordermode="outside", x=x, y=y)
            

    def saveDataPlot(self, eqPanel, stylePanel):
        '''acción al cliquear sobre save to graph, toma los valores de eq entry y stylePanel
        creando la clase Graph para luego poder graficar'''
        
        
        graph = Graph(eqPanel.eq.get_value(),
                      eqPanel.xi.get_value(),
                      eqPanel.yi.get_value(),
                      eqPanel.xf.get_value(),
                      eqPanel.yf.get_value(),
                      eqPanel.frec.get_value(),
                      stylePanel.type.get_value(),
                      stylePanel.color.get_value(),
                      stylePanel.label.get_value(),
                      stylePanel.lw.get_value())
        
        #existe variable x
        if graph.eq.checkEq:
            #agrega a la lista de plots los datos del gráfico
            self.dataGraph.append(graph)
        
        
    def plotGraphics(self):
        '''Acción al apretar el boton Graph, crea un objeto plot donde estan graficados todos
        los graficos de la lista dataGraph'''
        
        #limpia el panel
        self.closeGraphZone()
      
        #crea el objeto plot
        plot = Plot(self.dataGrid, self.dataLegend)
        
        #metodo graphic para obtener la figura
        fig = plot.graphic(self.dataGraph)
        
        #incorporar figura al frame de vista panelGraph
        Canvas(self.panelGraph, fig, data = self.dataGraph)
        
    def setOther(self):
        
        self.buttons["btnOther"][0]["state"] = "disabled"
    

    def closeGraphZone(self):
        for widgets in self.panelGraph.winfo_children():
            widgets.destroy()
    