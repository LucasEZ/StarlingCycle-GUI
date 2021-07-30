# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:37:50 2021

@author: lucas
"""

from PIL import Image, ImageTk


class Imagen():
    '''Clase para cargar y ajustar tamaño de imágenes a las dimensiones de un botón'''
    
    def __init__(self,path,size):
        self.path = path
        self.x = size[0]
        self.y = size[1]
        
        self.openImage = Image.open(self.path)
        self.im = self.openImage.resize((self.x,self.y), Image.ANTIALIAS)
        
    def re(self):
        self.imagen = ImageTk.PhotoImage(self.im)
        return self.imagen
    
