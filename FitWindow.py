# -*- coding: utf-8 -*-

"""
Created on Fri Apr 23 22:47:49 2021

@author: lucas
"""

import pandas as pd
import tkinter as tk
from tkinter import ttk


from FitPanel import PanelFit
from DataLoader import DataLoader

class EquationFitWindow():
    def __init__(self, root, windowApp):
        self.root = root
        
        #frame madre
        self.fitWindow = tk.Frame(windowApp)
        windowApp.add(self.fitWindow, text="Equation Fit")
        
        #agrega frame sobre frame madre a la derecha
        self.dataFrame = tk.Frame(self.fitWindow)
        self.dataFrame.pack(side='left', expand=True, fill="both")
        
        #agrega frame sobre frame madre a la izquierda
        self.prmFrame = tk.Frame(self.fitWindow)
        self.prmFrame.pack(side='right',expand=True, fill="both")
        
        #Cargamos la estructura de lectura de datos en el frame izquierdo
        self.dataLoader = DataLoader(self.prmFrame)
        
        #creamos un boton para ejecutar las funciones de dataLoader
        load_btn = tk.Button(self.dataLoader.panelFrame, width=50, text="Load data", command=lambda: self.load_and_charge())
        load_btn.place(bordermode="outside", x=10, y=280)
    

    def load_and_charge(self):
        '''Acción que ocurre al presionar el boton load data. Se abre un tree view para visualizar 
        datos cargados sobre el frame izquierdo, y sobre el derecho panel parra configuar el ajuste
        y los datos a emplear'''
    
        #Frame que contendrá el plot
        self.fitFrame = tk.Frame(self.dataFrame)                            
        self.fitFrame.place(relheight=0.5, relwidth=1)
        
        self.fitLabel = ttk.Notebook(self.dataFrame)
        self.fitLabel.place(rely=0.5, relheight=0.5, relwidth=1)
        
        #devuelve el dataFrame obtenido de la lectura del archivo externo
        df = self.dataLoader.load()
        
        self.dataLoader.chargeTreeView(df)
    
        #carga el panel de configuración de ajuste de funciones sobre el panel fitLabel
        pan = PanelFit(self.root, self.fitLabel, self.fitFrame, df)
        
        
    