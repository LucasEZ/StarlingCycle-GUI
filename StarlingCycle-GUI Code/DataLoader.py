# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:58:15 2021

@author: lucas

TreeView code idea base it from RamonWill/DataFrameSearch.py
"""

import tkinter as tk
from tkinter import ttk
from Wigets import Wiget
import pandas as pd
import os
import re

class TreeView():
    def __init__(self, frame):
        '''Estructura de treeView para cargar el dataFrame dentro de la aplicaciòn'''
        for widgets in frame.winfo_children():
             widgets.destroy()

        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
                        foreground='white', 
                        background="black")
        
    
        ## Treeview Widget
        self.tv1 = ttk.Treeview(frame)
        # seteamos la altura y el ancho del wiget al 100% del frame
        self.tv1.place(relheight=1, relwidth=1) 
        
        # Creamos scrollbars para el eje x e y
        treescrolly = tk.Scrollbar(frame, orient="vertical", command=self.tv1.yview) 
        treescrollx = tk.Scrollbar(frame, orient="horizontal", command=self.tv1.xview) 
        
        # incorporamos las scrollbar al frame
        self.tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) 
        treescrollx.pack(side="bottom", fill="x") 
        treescrolly.pack(side="right", fill="y")

    def chargeData(self, df):
        
        #cargamos los datos en el treeview
        self.tv1["column"] = list(df.columns)
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            self.tv1.heading(column, text=column) 
    
        df_rows = df.to_numpy().tolist() 
        for row in df_rows:
            self.tv1.insert("", "end", values=row) 



class DataLoader():
    def __init__(self, mainWindow):
        '''Clase con GUI para cargar archivo csv o xlxs'''
        self.tableFrame = tk.Frame(mainWindow)
        self.tableFrame.place(relheight=0.5, relwidth=1) 
    
        self.panelFrame = tk.Frame(mainWindow)
        self.panelFrame.place(rely=0.5, relheight=0.5, relwidth=1)
        
        
        self.wigets = { 
            'path': Wiget(self.panelFrame,
                             "Path",
                             (20, 10),
                             "entry",
                             (150, 10), 
                             width=40,
                             need_path=True,
                             where="before"),
            
             'head': Wiget(self.panelFrame, 
                           "Headers", 
                           (20, 70), 
                           "check", 
                           (100, 70),
                           text="Set column names manually"),
             
             "head_names": Wiget(self.panelFrame,
                             "Head Names",
                             (20, 120),
                             "entry",
                             (100, 120), 
                             width=45),
                
             "na": Wiget(self.panelFrame,
                             "NA Values",
                             (20, 160),
                             "entry",
                             (100, 160), 
                             width=45),
            
            "sheet": Wiget(self.panelFrame,
                           "Sheet Name",
                           (20, 200),
                           "entry",
                           (100, 200), 
                           width=45),
            
            "delimiter": Wiget(self.panelFrame,
                             'Delimiter',
                             (20, 240),
                             "box",
                             (100, 240), 
                             width=2,
                             values=[",", ";", ".", "'", ":", "/"])   
            }
        

    def load(self):
        '''carga el data frame para trabajar en el sistema. Devuelves el DataFrame.'''
        
        path = self.get_path()
        
        ext = self.findExtension(path)
        
        delimiter = self.wigets["delimiter"].get_value()
        
        sheet = self.wigets["sheet"].get_value()
        
        head = self.wigets["head"].get_value()
        
        if head == 1:
            cols = self.splitString(self.wigets["head_names"].get_value())
        else:
            cols = None
        
        
        na_values = self.wigets["na"].get_value()
        if na_values != "":
            naValues = self.splitString(na_values)
        else:
            naValues = None
        
        if ext == ".csv":
            self.df = pd.read_csv(path, delimiter=delimiter, names=cols, na_values=naValues)
            if naValues != None:
                self.cleanNA(head)
            self.rowIndex()
            
            
        if ext == ".xls" or ext == ".xlsx":
            self.df = pd.read_excel(path, sheet_name=sheet, delimiter=delimiter, names=cols, na_values=naValues )
            if naValues != None:
                self.cleanNA(head)
            self.rowIndex()

            
        return self.df
    
    def chargeTreeView(self, df):
        '''carga el dataFrame en de trabajo en un treeview'''
        tv = TreeView(self.tableFrame)
        tv.chargeData(df)  
    
    def cleanNA(self, head):
        '''Elimina los valores pasados como NA'''
        if head == 0:
            patron1 = re.compile('Unnamed: \d')
            values1=[name for name in self.df.columns if patron1.search(name) == None]
            self.df.dropna(axis=0, how='any', inplace=True, subset=values1)
        else:
            patron2 = re.compile('False\d')
            values2=[name for name in self.df.columns if patron2.search(name) == None]
            self.df.dropna(axis=0, how='any', inplace=True, subset=values2)
        
        self.df.reset_index(drop=True, inplace=True)
        
    def update(self, frame):
        '''Actualia el dataLoader'''
        self.__init__(frame)
        
                    
    def rowIndex(self):
        '''Agrega una columna al Df con un índice'''
        self.df['Index'] = range(0, len(self.df))
    

    def get_path(self):    
        '''devuelve la ruta del archivo del cual se cargan los datos (string)'''
        path = str(self.wigets["path"].get_value())
        
        if os.path.isfile(path):
            return path           
        
    def findExtension(self, path):
        '''Obtiene la extensión de un archivo. Devuelve un string con la extensión.'''
        index = path.find(".")
        ext = path[index::]
        
        return ext           
    
    def splitString(self, stringVar):
        '''Separa el contenido de un string a partir de comas. DEvuelve una lista de con las partes
        del string original'''
        name = str(stringVar)
        cols = name.split(",")
        
        return cols
        
