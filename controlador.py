# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:24:20 2021

@author: USER
"""

from vista import Vista#importamos vista 
from modelo import Modelo#importamos modelo 
 
class Controlador:#definimos clase controlador 
    def __init__(self):
        #ventana= tkinter.Tk()
        self.modelo = Modelo()
        self.vista = Vista(self.modelo)
        
    #def ejecutar():
        #ventana.resizable(False,False)
        #ventana.mainloop()