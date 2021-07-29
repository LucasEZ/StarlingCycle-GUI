# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:49:22 2021

@author: lucas
"""

import tkinter as tk

class MlWindow():
    def __init__(self, root, windowApp):
        self.root = root
        self.mlWindow = tk.Frame(windowApp)
        windowApp.add(self.mlWindow, text="Machine Learning")
