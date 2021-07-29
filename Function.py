# -*- coding: utf-8 -*-
"""
Created on Sat May 29 14:21:56 2021

@author: lucas
"""
import numpy as np
import re
import math as mt

class Function():
    
    def __init__(self, equation):
        '''Clase para procesar la ecuación de entrada, determinar variables y codificar la misma
        para poder ser ejecutada por el interprete'''
        
        #ecuación
        self.eq = equation
        
        #verifica que exista una variable dependiente x
        self.checkEq = self.checkEq(equation)
        
        #variable de decodificación
        self.f = self.decodeEquation(equation)
        
        #variable de reemplazo de variables
        self.replaceParm = False
        self.chargeParm = False
        
        #variables detectadas en la ecuación
        self.v = self.detectVariables()

    def checkEq(self, eq):
        depVariable = re.compile('x')
        
        searcher = depVariable.search(eq)
        
        if searcher == None:
            return False
        else:
            return True
        
    def decodeEquation(self, eq):
        '''decodifica la equación y la re escribe en forma de código para ser interpretada.
        El resultado se encuentra sobrescrito en la variable f.
        '''
            
        simbols = {
            'np.exp' : re.compile(r'e(\^)+'),
            '**' : re.compile(r'\^'),
            "np.sqrt": re.compile(r'sqt'),
            "np.log": re.compile(r'ln'),
            "np.log2": re.compile(r'log2'),
            "np.log10": re.compile(r'log10'),
            "np.sin":  re.compile(r'sin'),
            "np.cos": re.compile(r'cos'),
            "np.tan" : re.compile(r'tan'),
            "mt.pi" : re.compile(r'pi'),
            "mt.e" : re.compile(r'pe')
            }
        
        for simbol in simbols.keys():
            eq = re.sub(simbols[simbol],simbol,eq)
        
        return eq
    
    def detectVariables(self):
        '''Detecta el número de variables presente en la equación. Busca el patrón nx. Devuelve
        una lista con todas las variables detectadas'''
        patron =  re.compile(r'(n\d*)')
        nv = patron.findall(self.f)
        
        for v in range(len(nv)+1):
            try:
                index = nv.index('n')
                nv.pop(index)
            except ValueError as e:
                pass
        
        return nv
    
    def createFunc(self):
        '''devuelve una funcion dependiente de x más todas las variables de ajuste'''
        
        if self.checkEq:
            if len(self.v) > 0:
                str_variables = 'x,' + ','.join(self.v)
                try:
                    f = eval(f'lambda {str_variables}: ' + self.f)
                    return f
                except NameError as e:
                    pass
            else:
                try:
                    f =  eval('lambda x: ' + self.f) 
                    return f
                except NameError as e:
                    pass
    
    def adjustedFunction(self): #ex func function
        '''devuelve la función con los parámetros ajustados ya establecidos'''

        try:
            f =  eval('lambda x: ' + self.f_fit) 
            return f
        except NameError as e:
            print(e)


    def eqReplace(self):
        
        aux = self.eq
        
        for e in zip(self.v, self.p):
            f = re.sub(e[0], str(round(e[1],3)), aux)
            aux = f
        
        return aux
    
    def chargeFitParameters(self, p, e):
        '''Carda los parámetros de ajuste como atributos de clase'''
        
        #parámetros de ajuste
        self.p = p
        
        #error de los parámetros de ajuste
        self.e = np.sqrt(np.diag(e))
        
        #merge variable, valor óptimo y error
        self.fitVars = zip(self.v, p, self.e)
        self.chargeParm = True
                
    def replaceVariables(self):
        
        '''reemplaza las variables de la ecuación por los parámetros de ajuste cargados.
        Se genera el atributo f.fit, un string con la equación fiteada'''
        if self.chargeParm:
            f = self.f
            for e in zip(self.v, self.p):
                f = re.sub(e[0], str(e[1]), f)
            
            self.f_fit = f
            self.replaceParm = True        
        else:
            pass
    
    def getFitData(self, x_exp):
        '''evalua la función ajustada en una grilla de valores de x entre el primer y
        último valor de la serie x_exp'''

        if self.replaceParm:
            f =  eval('lambda x: ' + self.f_fit) 
            
            x_grid = np.linspace(x_exp[0], x_exp[-1], 1000)
            y_grid = f(x_grid)
        
            return x_grid, y_grid
    
    
    def residuals(self, x_exp, y_exp):
        '''calculo de residuos del ajuste, devuelve array con los residuos'''
        
        if self.replaceParm:
            f =  eval('lambda x: ' + self.f_fit) 
            
            y_grid = f(np.array(x_exp))
            
            residuals = np.array(y_exp) - y_grid
            
            return residuals
    
    def r_squared(self, x_exp, y_exp):
        '''Calculo de R2, devuelve su valor'''
        
        if self.replaceParm:
            f =  eval('lambda x: ' + self.f_fit) 
            
            x = np.array(x_exp)
            y = np.array(y_exp)
           
            y_grid = f(np.array(x))
        
            ssResidual = sum((y-y_grid)**2)       
            ssTotal = sum((y-np.mean(y))**2)     
            r_squared = 1 - (float(ssResidual))/ssTotal
            
            return r_squared, ssResidual, ssTotal
    

        


      