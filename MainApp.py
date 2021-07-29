# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:36:33 2021

@author: lucas
"""
from tkinter import ttk
import tkinter as tk

from Wigets import ButtonBar
from GraphWindow import GraphWindow
from FitWindow import EquationFitWindow
from MlWindow import MlWindow


class MainApp():
    '''Clase principal de la aplicación. Consta de tres botones para abrir las diferentes
    funcionalidades de la aplicación (graficador, ajustes y algoritmos de ML) y una ventana 
    donde se permite al usuario trabajar'''
    
    def __init__(self, root):
        self.root = root
        
        #importamos la barra de botones y le damos funcionalidades
        self.buttonBar = ButtonBar(self.root, self.graphPanel, self.fitPanel, self.mlPanel)
        
        #ventana de trabajo
        self.mainWindow = tk.Frame(root)
        self.mainWindow.pack(side='right',fill=tk.BOTH,expand=True)
        
    def graphPanel(self):
        '''Carga sobre la ventana de trabajo toda la funcionalidades asociadas al graficador.
        Se ejecuta al clickear sobre el boton graficador.'''
        
        #deshbilitamos boton graficador de la barra de botones y habilitamos el resto
        self.buttonBar.btnGraph["state"] = "disabled"
        self.buttonBar.btnFit["state"] = "normal"
        self.buttonBar.btnMl["state"] = "normal"
        
        #limpiamos previamente la ventana de trabajo
        self.cleanWindow()
        
        #Cargamos clase GraphWindow sobre un notebook en la ventana de trabajo
        self.windowNote = ttk.Notebook(self.mainWindow)
        self.graphWindow = GraphWindow(self.mainWindow , self.windowNote)
        self.windowNote.pack(side='left',fill=tk.BOTH,expand=True)
        
    def fitPanel(self):
        '''Carga sobre la ventana de trabajo toda la funcionalidades asociadas al ajuste de datos.
        Se ejecuta al clickear sobre el boton ajustes.'''
        
        #deshbilitamos boton ajustes de la barra de botones
        self.buttonBar.btnGraph["state"] = "normal"
        self.buttonBar.btnFit["state"] = "disabled"
        self.buttonBar.btnMl["state"] = "normal"
        
        #limpiamos previamente la ventana de trabajo
        self.cleanWindow()
        
        #Cargamos clase EquationFitWindow sobre un notebook en la ventana de trabajo
        self.windowNote = ttk.Notebook(self.mainWindow)
        self.graphWindow = EquationFitWindow(self.mainWindow , self.windowNote)
        self.windowNote.pack(side='left',fill=tk.BOTH,expand=True)
        
    def mlPanel(self):
        '''Carga sobre la ventana de trabajo toda la funcionalidades asociadas al ajuste de datos.
        Se ejecuta al clickear sobre el boton ajustes.'''
        
        #deshbilitamos boton ajustes de la barra de botones
        self.buttonBar.btnGraph["state"] = "normal"
        self.buttonBar.btnFit["state"] = "normal"
        self.buttonBar.btnMl["state"] = "disabled"
        
        #limpiamos previamente la ventana de trabajo
        self.cleanWindow()
        
        #Cargamos clase MlWindow sobre un notebook en la ventana de trabajo
        self.windowNote = ttk.Notebook(self.mainWindow)#, width=1000, height=700)
        self.mlWindow =MlWindow(self.mainWindow , self.windowNote)
        
        self.windowNote.pack(side='left',fill=tk.BOTH,expand=True)
        
    def cleanWindow(self):
        '''metodo de la clase Mainapp para limpiar la ventana principal de trabajo'''
        for widgets in self.mainWindow.winfo_children():
            widgets.destroy()
