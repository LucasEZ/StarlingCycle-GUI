# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:57:30 2021

@author: lucas
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import colorchooser

import os
import csv
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)  

from Auxiliars import Imagen


class Wiget():
    def __init__(self, frame, label, coord_label, wiget ,coord_wiget, text ="Yes / No", spin=[1, 1000, 10] ,values=[], width=40, need_color=False, need_path=False,  where = "after"):
        '''Clase que engloba los posibles wiget de tkinter a emplear.
        frame: Tk.frame donde se incorpora.
        wiget: que clase de wiget es (entry, box, spin, check).
        label: texto que acompaña al wiget.
        coord_label: tupla con coord x e y de la ubicación del label en el frame.
        coord_wiget: tupla con coord x e y de la ubicación del wiget en el frame.
        text: modificable por otro string, empleado en los check.
        spin: lista con los valores permitidos para un spin [min, max, salto]. Modificable.
        values: para los box, lista con los valores predeterminados posibles.
        width: ancho del wiget.
        need_color: booleano, si es True incorpora un boton para acceder a panel de colores.
        need_path: booleano, si es True incorpora un boton para acceder a un filedialog.
        where = acepta after o before y es para saber donde ubicar el boton de paleta de colores o de ruta'''
        
        self.frame = frame
        self.wiget = wiget
        
        #define wiget
        if self.wiget == "entry":
            self.var = tk.StringVar()
            self.w = tk.Entry(frame, 
                              width=width, 
                              textvariable=self.var)
            
        if self.wiget == "box":
            self.var = tk.StringVar()
            self.w = ttk.Combobox(frame, 
                                  values=values, 
                                  width=width, 
                                  textvariable=self.var )
            
        if self.wiget == "spin":
            self.var = tk.IntVar()
            self.w = ttk.Spinbox(frame, from_=spin[0],to=spin[1],
                         increment=spin[2],
                         width=5,
                         textvariable=self.var)
            
        if self.wiget == "check":
            self.var = tk.IntVar()
            self.w = tk.Checkbutton(frame,
                           text=text, 
                           variable=self.var,
                           onvalue = 1, 
                           offvalue = 0)
            
        #crea label asociado al wiget
        tk.Label(frame, text=label).place(bordermode="outside", x=coord_label[0], y=coord_label[1])
        self.w.place(bordermode="outside", x=coord_wiget[0], y=coord_wiget[1])
        
        #crea boton paleta de colores
        if need_color == True:
             color_btn = tk.Button(frame, text="...", width=2, height=1, command = lambda: self.color(self.w))
             if where == "after":
                color_btn.place(bordermode="outside", x=coord_wiget[0]+width*7, y=coord_wiget[1])
             if where == "before":
                color_btn.place(bordermode="outside", x=coord_wiget[0]-width*7, y=coord_wiget[1])
        
        #crea boton búsqueda de ruta
        if need_path == True:
            path_btn = tk.Button(frame, width=6, height=1, text="Search...", command= lambda: self.search_path(self.w))
            if where == "after":
                path_btn.place(bordermode="outside", x=coord_wiget[0]+width*10, y=coord_wiget[1])
            if where == "before":
                path_btn.place(bordermode="outside", x=coord_wiget[0]-width*2, y=coord_wiget[1])
            
    def get_value(self):
        '''método para obtener el valor ingresado en el wiget. Devuelve dicho valor en string'''
        if self.wiget == "check":
            try:
                value = self.var.get()
            except AttributeError as e:
                value = self.var
        else:
            value = self.w.get()
            
        return value
    
    
    def search_path(self, wiget):
        '''funcionalidad de botón para búsqueda de ruta. Devuelve un string con la ruta del
        archivo selecionado'''
        filename = filedialog.askopenfilename(initialdir = "/",
                                                   title = "Select a file",
                                                   filetypes = (("csv files","*.csv"),
                                                   ("excel files", "*.xlsm"),
                                                   ("all files", "*.*")),)
        
        #escribe ruta en wiget
        wiget.insert(0, filename)
        path = filename
        
        return path
   
    def findExtension(self, path):
        '''Determina la extensión del archivo seleccionado en el buscador de ruta'''
        index = path.find(".")
        ext = path[index::]
        
        return ext   
    
    def color(self, entry):
        '''Abre ventana de colores e escribe el color seleccionado en el wiget'''
        chooseColor = colorchooser.askcolor(parent=self.frame)[1]
    
        entry.delete(0, 'end')
        entry.insert(0, chooseColor)

    
#################################################################################################


class ButtonBar():
    
    def __init__(self, root, c1, c2, c3):
        self.root = root
        self.buttonBar = tk.Frame(root, width=200, height=700, bg="white")
        self.buttonBar.pack(side='left',expand=False, fill=tk.BOTH,anchor="nw")
         
        #carga de imagen de boton graficador
        self.funImagen = self.chargeImage("ButtonImagen/imagen2.png")
        
        #creamos boton graficador
        self.btnGraph = tk.Button(self.buttonBar, text = "Button", image = self.funImagen, bg="white", command=c1)
        self.btnGraph.pack(expand=True, fill="both")
        
        #carga de imagen boton ajustes
        self.fitImagen = self.chargeImage("ButtonImagen/imagen1.png")
        
        #creamos boton ajustes
        self.btnFit = tk.Button(self.buttonBar, text = "Button", image = self.fitImagen,bg="white", command=c2)
        self.btnFit.pack(expand=True, fill="both")
        
        #carga de imagen boton ML
        self.mlImagen = self.chargeImage("ButtonImagen/imagen3.png")
        
        #creamos boton ML
        self.btnMl = tk.Button(self.buttonBar, text = "Button", image = self.mlImagen, bg="white", command=c3)
        self.btnMl.pack(expand=True, fill="both")
        
    def chargeImage(self, path):
        
        image =  Imagen(path, (150, 200))
        
        return image.re()



#######################Estructuras de interfaz gráfica#########################


class SettingGrid(Wiget):
    def __init__(self, frame, dataGrid, width=100, x=50, y=500, state=True):
        '''Ventana emergenete para configuración de grilla en gráficas'''
        
        self.frame = frame
        
        self.btnGrid = tk.Button(frame, text="Color and Grid", width=width, command=lambda: self.openGridWindow(dataGrid))
        self.btnGrid.place(bordermode="outside", x=x, y=y)
        
    
    def openGridWindow(self, dataGrid):
        
        height = 500
        width = 500
        
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
                    self.alphaGrid.get_value(),

        )
    
    
        self.btnGrid["state"] = "normal"
        
        self.wg.destroy()
    

class SettingLegend(Wiget):
    def __init__(self, frame, dataLegend, width=100, x=15, y=500, state=True):
        '''Ventana emergenete para configuración de leyendas en gráficas'''
        self.frame = frame
        
        self.btnLegend = tk.Button(self.frame, text="Legends", width=width, command=lambda: self.openLegendWindow(dataLegend))
        self.btnLegend.place(bordermode="outside", x=x, y=y)
    

    def openLegendWindow(self, dataLegend):

        height = 450
        width = 500
        
        self.wg = tk.Toplevel(self.frame, height=height, width=width)

        self.wg.title("Legend and Text")
        self.wg.resizable(width=False, height=False)

        self.legend = Wiget(self.wg, 'Apply Legends', (20, 10), "check",(190, 10))
                
        self.loc = Wiget(self.wg, 'Ubication legend', (20, 60), "box", (190, 60),
                         width=25,
                         values=['best',
                                'upper left', 
                                'upper right', 
                                'lower left', 
                                'lower right',
                                'upper center',
                                'lower center',
                                'center left',
                                'center right'])
           
        self.shadow = Wiget(self.wg, 'Shadow', (20, 110), "box", (190, 110), 
                         width=25,
                         values=[True, False])
 
        self.xlabel = Wiget(self.wg, 'x label', (20, 160),"entry", (190, 160), 
                            width=25)
                
        self.ylabel = Wiget(self.wg, 'y label', (20, 210), "entry", (190, 210), 
                            width=25)
                
        self.fontsize = Wiget(self.wg, 'fontsize', (20, 260), "spin", (190, 260), 
                             width=5,
                             spin=[0, 20, 1])
        
        self.sizeBox = Wiget(self.wg,'Box Height', (20, 310),"spin",
                    (190, 310), 
                    width=10,
                    spin=[5, 25, 1])
        
    

        self.setLegend = ttk.Button(self.wg, text="Set and close", width=45, command=lambda: self.getValues(dataLegend))
        self.setLegend.place(bordermode="outside", x=20, y=360) 
        
        
    def getValues(self, dataLegend):
        
        dataLegend.update_data(self.legend.get_value(),
                             self.loc.get_value(),
                             self.shadow.get_value(),
                             self.xlabel.get_value(),
                             self.ylabel.get_value(),
                             self.fontsize.get_value(),
                             self.sizeBox.get_value(),
               
                             )
        
        self.btnLegend["state"] = "normal"
        self.wg.destroy()


##############################################################################################

class EqEntry(Wiget):
    '''LabelFrame para configuracion de gráficos'''
    def __init__(self, frame, height=200, width =510, x=15, y=20):
        
        eqLabel =  tk.LabelFrame(frame,height=height, width=width, text="Equation parameters")
        eqLabel.place(bordermode="outside", x=x, y=y)
        
        self.eq = Wiget(eqLabel,"Equation", (15, 50), "entry", (80, 50), width= round(width*0.12))
        
        w = round(width*0.019)                
        
        self.xi = Wiget(eqLabel, "xi", (15, 100), "spin", (60, 100), width=w)
        self.xf = Wiget(eqLabel, "xf", (15, 150), "spin", (60, 150), width=w)
        
        self.yi = Wiget(eqLabel, "yi", (175, 100), "spin", (220, 100), width=w)        
        self.yf = Wiget(eqLabel, "yf", (175, 150), "spin", (220, 150), width=w)
        
        self.frec = Wiget(eqLabel, "frec", (300, 100), 
                     "spin",
                      (355, 100),
                      spin=[1, 500, 50],
                      width=5)


class StyleEntry(Wiget):
    
    def __init__(self, frame, height=250, width=510, x=15, y=20):
        '''LabelFrame para configuracion del estilo de gráficos'''
        lb =  tk.LabelFrame(frame,height=height, width=width, text="Style Plot")
        lb.place(bordermode="outside", x=x, y=y)    
        
        #tipo
        self.type = Wiget(lb, "Type", (15, 50), "box", (150, 50), 
                       values=["Scatter", "Lineal"], 
                       width=round(width*0.06))
        #color de línea
        self.color = Wiget(lb, "Color (RGBA)", (15, 100), "entry", (150, 100),
                         width= round(width*0.06),
                         need_color=True,
                         where = "after")
        #nombre
        self.label =  Wiget(lb, "Label", (15, 150), "entry", (150, 150), width= round(width*0.06))
        #ancho de línea
        self.lw = Wiget(lb, "Linewidth", (15, 200), "spin", (150, 200), width=5, 
                        spin=[1, 30, 1])

#################################################################################################

class ConfigFitPanel(Wiget):
    
    def __init__(self, notebook, df, dataGrid, dataLegend):
        
        self.fitLabel =  tk.Frame(notebook,height=900, width=400)
        notebook.add(self.fitLabel, text="Equation Fit")
        
        self.plotLabel =  tk.Frame(notebook,height=900, width=400)
        notebook.add(self.plotLabel, text="Configuration Plot")
    
        self.x = Wiget(self.fitLabel, 
                       "x values column", 
                       (10, 20), 
                       "box", 
                       (105, 20), 
                       values=[e for e in df.columns], 
                       width=10)
            
        self.xfrom = Wiget(self.fitLabel, 
                           "from x", 
                           (200, 20), 
                           "spin", 
                           (250, 20),
                           spin=[1, 10000, 10],
                           width=5)
            
        self.xto = Wiget(self.fitLabel, 
                           "to", 
                           (310, 20), 
                           "spin", 
                           (340, 20),
                           spin=[1, 10000, 10],
                           width=5)
            
        self.y = Wiget(self.fitLabel, 
                       "y values column", 
                       (10, 60), 
                       "box", 
                       (105, 60), 
                       values=[e for e in df.columns], 
                       width=10)
            
        self.yfrom = Wiget(self.fitLabel, 
                           "from y", 
                           (200, 60), 
                           "spin", 
                           (250, 60),
                           spin=[1, 10000, 10],
                           width=5)
        
        self.yto = Wiget(self.fitLabel, 
                         "to", 
                         (310, 60), 
                         "spin", 
                         (340, 60),
                         spin=[1, 10000, 10],
                         width=5)
        
        self.xtype = Wiget(self.fitLabel, 
                           "type",
                           (400, 20),
                           "box",
                           (430, 20),
                           width=5,
                           values=["value", "datetime"]
                           )
        
        
        self.ytype = Wiget(self.fitLabel, 
                           "type",
                           (400, 60),
                           "box",
                           (430, 60),
                           width=5,
                           values=["value", "datetime"]
                           )
        
        
        self.xformat = Wiget(self.fitLabel, 
                           "",
                           (600, 20),
                           "entry",
                           (490, 20),
                           width=10
                           )
        
        self.yformat = Wiget(self.fitLabel, 
                           "",
                           (650, 60),
                           "entry",
                           (490, 60),
                           width=10
                           )
        
    
        self.nvar = Wiget(self.fitLabel, 
                         "Numbers of parameters", 
                         (10, 100), 
                         "spin", 
                         (150, 100),
                         spin=[1, 5, 1],
                         width=5)
    
        self.eq = Wiget(self.fitLabel, 
                         "Equation", 
                         (10, 140), 
                         "entry", 
                         (100, 140),
                         width=40)
            
        self.seed = Wiget(self.fitLabel, 
                         "Seed values", 
                         (10, 180), 
                         "entry", 
                         (100, 180),
                         width=40)
            
        self.attemps = Wiget(self.fitLabel, 
                         "Attempts", 
                         (10, 220), 
                         "spin", 
                         (100, 220),
                         spin=[1, 10000, 1000],
                         width=5)
            
        self.color = ButtonCP(self.plotLabel, 10, 30, "Linecolor", 10, 1)
    

        self.marketColor = ButtonCP(self.plotLabel, 10, 70, "Marketcolor", 10, 1)
        
        self.market = Wiget(self.plotLabel, 
                       "Market", 
                       (10, 110), 
                       "box", 
                       (125, 110), 
                       values=['None','.', ',', 'o', 'v', '^', 'p', 'P', '+', 'x'], 
                       width=23)
            

        self.labelPoint = Wiget(self.plotLabel, 
                         "Label points", 
                         (10, 140), 
                         "entry", 
                         (125, 140),
                         width=25)
                        
        self.labelFit = Wiget(self.plotLabel, 
                         "Label fit", 
                         (10, 170), 
                         "entry", 
                         (125, 170),
                         width=25)
            
        
        SettingGrid(self.plotLabel, dataGrid, width=10, x=350, y=30)
        SettingLegend(self.plotLabel, dataLegend, width=10, x=350, y=110)
        

        
################################################################################

class ButtonCP():
    def __init__(self, frame, x, y ,text, width, height, color = True):
        
        self.frame = frame
        self.chooseColor = None
        
        if color:
            btn = tk.Button(self.frame, text=text, width=width, height=height, command = lambda: self.color(x, y))
        else:
            btn = tk.Button(self.frame, text=text, width=width, height=height, command = lambda: self.search())
    
        btn.place(bordermode="outside", x=x, y=y)
    
    def color(self, x, y):
        
        self.chooseColor = colorchooser.askcolor()[1]
       
        tk.Label(self.frame, text=self.chooseColor).place(bordermode="outside", x=x+100, y=y)
        
    def get_value(self):
        
        if self.chooseColor == None:
            return "orange"
        else:
            return self.chooseColor
        
#################################################################################

class Toolbar(NavigationToolbar2Tk):

    def set_message(self, s):
        pass

class Canvas():
    def __init__(self, frame, fig, data=None):
        #specify the window as master
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        #canvas.get_tk_widget().pack(side='top')
        canvas.get_tk_widget().place(relheight=0.9, relwidth=1)                             
                                 

        # navigation toolbar
        self.toolbarFrame = tk.Frame(master=frame)
        self.toolbar = Toolbar(canvas, self.toolbarFrame)
        
        self.quit = ttk.Button(self.toolbar, text="Close",command = lambda: self.deleteAll(frame, data=data))
        self.quit.pack(side='right',expand=False, fill="x")
               
        #self.toolbarFrame.pack(side='bottom',expand=False, fill="x")
        self.toolbarFrame.place(rely=0.9, relheight=0.1, relwidth=1) 

    def deleteAll(self, frame, data=None):
        for widgets in frame.winfo_children():
            widgets.destroy()
        
        if data != None:
            data.clear()

class CanvasFrame(Canvas):
    
    def __init__(self, frame, fun, fig, x_grid, y_grid, x_exp, y_exp):
        
        super().__init__(frame, fig)
        
        self.btn_info = ttk.Button(self.toolbar, text="Show information", command=lambda: self.showInfo(frame, fun, x_grid, y_grid, x_exp, y_exp))
        self.btn_info.pack(side='right',expand=False, fill="both")

    def showInfo(self, frame, f, x_grid, y_grid, x_exp, y_exp):
        
        wg = tk.Toplevel(frame , width=800, height=400)
        wg.title("Information about curve fitting")
        
        wg.resizable(width=False, height=False)
        frame1 = tk.Frame(wg)
        frame2 = tk.Frame(wg)
        
        frame1.place(relx=0, relheight=1, relwidth=0.4)
        frame2.place(relx=0.4, relheight=1, relwidth=0.6)
        
        text = tk.Text(frame1)
        text.place(relheight=1, relwidth=1)
        
        title = "Report Information"
        
    
        text.insert("insert", f"{title:.^117s}")
        
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        
        text.insert("insert",f"f(x) = {f.eq:^32s}")
        
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        
        h = ("Variable", "Fit Value", "Error")
        head = f"{h[0]:^12}|{h[1]:^12}|{h[2]:^12}"
        
        text.insert("insert",head)
        
        for v, val, err in f.fitVars:
            line = f"{v:^12}|{val:^12.4f}|{err:^12.4f}"
            text.insert("insert", f"\n")
            text.insert("insert",line)
        
        eq = f.eqReplace()
        f.replaceVariables()
        r, sreg, stot = f.r_squared(x_exp, y_exp)
        
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        text.insert("insert",f"Sreg = {sreg:<15.4f} ")
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        text.insert("insert",f"Stot = {stot:<15.4f} ")
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        text.insert("insert",f"R^2 = {r:<15.4f} ")
        text.insert("insert", f"\n")
        text.insert("insert", f"\n")
        
        text.insert("insert",f"f(x) = {eq:^32s}")
        text.insert("insert", f"\n")
        
        fill = ""
        text.insert("insert", f"{fill:.^312s}")
        
        text.configure(state='disabled')
        
        residuals = f.residuals(x_exp, y_exp)
        
        res_plot = self.plotResiduals(x_exp, residuals)
        
        canvas = FigureCanvasTkAgg(res_plot, master=frame2)
        canvas.draw()
        canvas.get_tk_widget().place(rely=0, relheight=0.9, relwidth=1)
    
        
        toolbarFrame = tk.Frame(master=frame2)
        toolbarFrame.place(rely=0.9, relheight=0.1, relwidth=1)
        toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)
        toolbar.update()
        
    
    def export(self, x, y, y_res, name_file = "fit_export.csv"):
        
        path = filedialog.askdirectory()
        file = os.path.join(path, name_file)
        
        elements = zip(x, y)
        
        with open(file, encoding='UTF8',  mode='w', newline='') as f:
            w = csv.writer(f, delimiter=',')
        
            headers = ("x", "y")
            w.writerow(headers)
            
            for value in elements:
                w.writerow(value)
                
    def plotResiduals(self, x_exp, residuals):
            
         fig, ax = plt.subplots()
         
         res_plot = ax.scatter(x_exp, residuals)

         return fig


