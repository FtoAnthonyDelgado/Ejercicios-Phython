# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 14:24:44 2021

@author: USER
"""
import sympy as sym # nos ayudan con los calculos matematicos
import numpy as np # nos ayudan con los calculos matematicos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #librerias graficas para las funciones
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

class Modelo():
    i=0
#Funciones
    def __init__(self):
        self.i=0#definimos la variable i para utilizarlo en cualquier funcion que lo necesitemos
    def AC(self,pant,pant2,texto_pantalla,ventana):#funcion para borrar el contenido
        global operador#operador global para utilizarse en cualquier parte del codigo
        operador=''#operador global
        texto_pantalla.set('')#Deja la pantalla vacia
        pant.set('')
        pant2.set('')
        
        figura = plt.figure(figsize=(4,3),dpi=100)#se define la dimensiones de la figuras y los tamaños
        canvas = FigureCanvasTkAgg(figura,master=ventana)#se define el area del dibujo
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas = NavigationToolbar2Tk(canvas,ventana)#se agrega una barra de herramientas para manejar la grafica
        barra_tareas.place(x=410,y=290,relwidth=0.455)
        canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)
        plt.clf()#Borra el contenido de la grafica 

        
    i+=1
    def click(self,n,pantalla):#funcion para mostrar en pantalla el contenido del boton, n toma el valor del boton
        #Para usar la variable en cualquier parte del codigo
        pantalla.insert(self.i,n)#logramos que se muestre en pantalla todos los numeros que presionemos 
        self.i+= 1#los caracteres se van sumando para que no se nos borren 
        
    def operaciones(self,b,pantalla):#funcion para resolver las operaciones matematicas , b es el simbolo de la operacion
        global i
        long_b = len(b)#se cuentan los caracteres porque hay operaciones que usan 2 caracteres a la vez
        
        pantalla.insert(self.i,b)
        self.i += long_b#se suman los caracteres
        
    def DEL(self,pantalla,pant,pant2,texto_pantalla,ventana):#funcion para borrar caracter por caracter
        p = pantalla.get()#contenido de la pantalla
        if len(p):# numero de caracteres menor  0
            np = p[:-1]#se elimina el ultimo elemento de la pantalla
            self.AC(pant,pant2,texto_pantalla,ventana)
            pantalla.insert(0,np)#se muestran  los caracteres restantes ,sin contar con el ultimo 
        else:
            self.AC(pant,pant2,texto_pantalla,ventana)#se llama a la funcion en caso de no tener caracteres 
    
    def igual(self,pantalla,pant,pant2,texto_pantalla,ventana):#para evaluar las operaciones y presentar los resultados
        estado_P = pantalla.get()#se define una variable p en el cual se guarda lo que escribimos
        try:#implementamos un try
            global expresion#hacemos el llamado a nuestra operacion global
            #en dicha variable global se va a guardar lo que el usuario escriba convertido a una expresion matematica gracias al comando sym.sympify
            expresion = sym.sympify(estado_P)#se vuelve una expresion matematica el contenido de la pantalla
            self.AC(pant,pant2,texto_pantalla,ventana)#borramos el contenido en pantalla
            pantalla.insert(0,expresion)#se impimer la solucion
        except:
            self.AC(pant,pant2,texto_pantalla,ventana)
            #####
    def aprox(self,pantalla,pant,pant2,texto_pantalla,ventana):#Mostrar valores en forma decimal
        contenido= pantalla.get()# se denomina una variable contenido en lo que se guarda la expresion que el usuario escribio
        aproximacion=(sym.sympify(contenido)).evalf(15)#convertimos esa expresion en formato string a una expresion matematica con el evalf teniendo como argumento 15 convertimos esa expresion numerica en 15 decimales 
        self.AC(pant,pant2,texto_pantalla,ventana)#borramos el contenido de pantalla
        pantalla.insert(0,aproximacion)#insertamos el numero decimal
        
    def grafica(self,ventana,pantalla):#sirve para graficar las funciones que el usuario solicita 
        expresion = pantalla.get()# se nombra una variable expresion donde se guardara lo que el usuario escribe en pantalla pero en formato string
        expresion1 = sym.sympify(expresion)# en expresion 1 validamos  la expresion que escribe el usuario en una expresion matematica
        x = sym.Symbol('x')#con x vamos a validar x y que sea tomada como una variable matematica
        v = np.linspace(-15,15,100, endpoint=True)#creamos una lista con los valores atribuidos a nuestra funcion
        valores = []# aqui vamos a ir guardando los valores que salgan como resultado  de la expresion de v
        
        figura = plt.figure(figsize=(4,3),dpi=100)# creamos una figura en la que va a ir nuestras funciones  con figsize especificamos las medidas que va a tener con dpi realizamos la resolucion que va a tener esta
        canvas = FigureCanvasTkAgg(figura, master=ventana)#definimos el area de dibujo
        canvas.get_tk_widget().place(x=350,y=335,relwidth=0.455,relheight=0.44)# vamos especificar en que lugar de la ventana vamos a poner nuestro dibujo
        barra_tareas = NavigationToolbar2Tk(canvas, ventana)# es la barra para interactuar con la grafica
        barra_tareas.place(x=410,y=380,relwidth=0.455)# especificamos las cordenadas de nuestra barra de tareas
        canvas.get_tk_widget().place(x=410,y=381,relheight=0.455)
        
        for i in range(len(v)):#se crea un bucle en el que cada interacion evalua nuestra funcion con los valores de la lista v
            c = ((expresion1).evalf(subs={x: v[i]}))# que son guardadas en c 
            valores.append(c)#aqui se alamcenan los valores que hemos conseguido al remplazar los valores de v en nuestra funcion
            
        figura.add_subplot(111).plot(v,valores,label='{0}'.format(expresion))#con figura.add_subplot creamos un subplot donde estara la grafica de nuestra funcion
        plt.legend(loc = 'upper left')#se muestra la leyenda que nos indica la funcion que escribimos 
        plt.grid()#se genera una cuadricula
        canvas.draw()#se muestra la grafica
        
    def derivar(self,pant,pant2,pantalla,pantalla2,pantalla4,ventana):#funcion para derivar
        pant.set('')#borra el contenido anterior como ya dijimos
        pant2.set('')
        d = pantalla.get()# cabe recalcar en en la pantalla 1 vamos a escribir nuestra funcion principl en forma de string lo almacenamos en b
        if 'x' in d:#se muestra la variable por la cual se va a derivar
            d1= sym.sympify(d)#en esta funcion d se va a convertir en una funcion matematica
            r = sym.diff(d1,'x')#vamos a ocupar la funcion diff de sympi que necesita dos argumentos en este caso d1 y el segundo argumento seria para nuestra variable de diferenciacion
            pantalla4.insert(0,r)# nuestro valor de R se inserta en nuestra pantalla 2
            #mensaje='Grafica de la derivada ↑↑:'#mensaje que se imprime en la pantalla
            #pantalla4.insert(0, mensaje)# se inserta el mensaje
            expresion= pantalla4.get()#expresion como esta en string con la linea de abajo se le cambia a una expresion matematica
            expresion1= sym.sympify(expresion)
            x = sym.Symbol('x')#definimos como x a nuestro simbolo
            v = np.linspace(-15,15,100, endpoint=True)#son varios numeros que toma entre -15 y 100
            valores = []
            #toda esta parte es para crear el area de dibujo
            figura = plt.figure(figsize=(4,3),dpi=100)
            ax = figura.add_subplot(111)
            canvas = FigureCanvasTkAgg(figura, master=ventana)
            canvas.get_tk_widget().place(x=410,y=400,relwidth=0.455,relheight=0.44)
            barra_tareas = NavigationToolbar2Tk(canvas, ventana)
            barra_tareas.place(x=410,y=335,relwidth=0.455)
            canvas.get_tk_widget().place(x=410,y=335,relwidth=0.455)
            
            for i in range(len(v)):#creamos un for que va desde i hasta la longitud de v que va a tomar 100 valores de -15 a 15
                c = ((expresion1).evalf(subs={x: v[i]}))#definimos variable c con la expresion 1 que declaramos convertida a una expresion matematica aqui sustituimos x por cada valor del arreglo de numpyde la linea 109
                valores.append(c)#lo vamos agregando a una lista vacia con append
            ax.clear()#para que en la grafica original no se sobremonte 
            ax.plot(v,valores,label='{0}'.format(expresion))#utilizamos un format para que al momento de poner la leyenda en el string{0} vaya cambiando de valor
            plt.grid()#ponemos la cuadricula
            canvas.draw()#graficamos
            #todo esto es copiado de la funcion grafica
            expresion = pantalla.get()
            expresion1 = sym.sympify(expresion)
            x = sym.Symbol('x')
            v = np.linspace(-15,15,100, endpoint=True)
            valores = []
            figura = Figure(figsize=(4,3),dpi=100)
            canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
            #barra_tareas = NavigationToolbar2Tk(canvas , ventana)
            #barra_tareas.place(x=410,y=25,relwidth=0.455)
            canvas.get_tk_widget().place(x=410,y=25,relwidth=0.370)
            
            for i in range(len(v)):
                c =((expresion1).evalf(subs={x: v[i]}))
                valores.append(c)
            ax.plot(v,valores,label='{0}'.format(expresion))
            plt.legend(loc='upper left')
            canvas.draw()
            
    def integralindef(self,pant,pant2,pantalla,pantalla2,pantalla4,ventana):#funcion integral indefinida
        pant.set('')#elimina el contenido anterior
        pant2.set('')
        inte = pantalla.get()#en inte guardamos la funcion original
        inte1= sym.sympify(inte)#en inte una esa exprecion orginal la transformamos a una funcion matematica
        res = sym.integrate(inte1,('x',None, None))
        pantalla2.insert(0,res)
        expresion = pantalla2.get()#va a ser lo que se imprimo en la pantalla dos que es una integral pero esta se pone como string toca volver a crear a una funcion matematica
        expresion1= sym.sympify(expresion)#aqui lo creamos a una expresion matematica
        #mensaje='Grafica de la integral Indefinida ↑↑:'# se agrega un mensaje a la pantalla 4
        #pantalla4.insert(0,mensaje)#se inserta el mensaje 
        x= sym.Symbol('x')#definimos nuestro simbolo que es x
        v= np.linspace(-15,15,100,endpoint=True)# seria un arreglo de numpy que nos ayudara a sacar valores de nuestra funcion
        valores=[]# valores es una lista vacia
        #area de dibujo
        figura = plt.figure(figsize=(4,3),dpi=100)
        ax= figura.add_subplot(111)
        canvas = FigureCanvasTkAgg(figura, master=ventana)
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        #barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        #barra_tareas.place(x=410,y=290,relwidth=0.455)
        canvas.get_tk_widget().place(x=800,y=25,relwidth=0.450)
        
        for i in range(len(v)):#al igual que la derivada nuestra expresion 1 la evaluamos con el arreglo de numpy y este va a ser evaluado 
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)# se van guardando con .append
        ax.clear()#se pueda graficar de una manera esteteticamente bien
        ax.plot(v,valores,label='{0}'.format(expresion))#en la leyenda se puede ir colocando la funcion en este caso expresion
        plt.legend(loc='upper left')#colocamos la leyenda
        plt.grid()#y nuestra cuadricula
        
        canvas.draw()#dibujamos la grafica
        expresion = pantalla.get()
        expresion1 = sym.sympify(expresion)
        
        x = sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores=[]
        figura = Figure(figsize=(4,3),dpi=100)
        canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        #barra_tareas = NavigationToolbar2Tk(canvas, ventana)
        #barra_tareas.place(x=410,y=290,relwidth=0.455)
        canvas.get_tk_widget().place(x=900,y=25,relwidth=0.370)
        
        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores. append(c)
            
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.legend(loc='upper left')
        canvas.draw()
        
    
        
        
        
        
        
         
         
                
            
            
        
        
        
       
        
   
        
                