# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:35:42 2021

@author: USER
"""

import tkinter#importamos la libreria  que nos ayuda a crear la interfaz grafica

class Vista():#definimos la clase vista
    def __init__(self,modelo):#creamos el metodo contructor son self modelo
        self.modelo=modelo#definimos self modelo
        ventana=tkinter.Tk()#creamos la ventana
        ventana.title("Calculadora Grafica")#nombre a la ventana creada
        ventana.geometry("800x600")#dimensiones de nuestra ventana
        #ventana.resizable(False,False)#evitamos que se cambien las dimensiones de nuestra ventana-
        ventana.configure(background="darkgray")#ponemos un fondo 
        operator=''#Establecemos una variable vacia que la vamos a utilizar mas adelante
        texto_pantalla= tkinter.StringVar()#entradas de texto
        pant = tkinter.StringVar()#entrada de texto
        pant2= tkinter.StringVar()#entrada de texto
        #creando las pantallas 1 lo cual difinimos tamaño de letras,ancho, bordes y el establecemos las cordenadas que va a tomar cada una.
        pantalla=tkinter.Entry(ventana,font=('Arial',20),width=23,borderwidth=5,textvariable=texto_pantalla,justify=tkinter.RIGHT)
        pantalla.place(x=25,y=25)
        #creando la pantalla numero dos de la misma manera de la uno   
        pantalla2=tkinter.Entry(ventana,font=('Arial',20),textvariable=pant,width=24,borderwidth=None)
        pantalla2.place(x=410,y=335,relheight=0.26)
        #creando la pantalla 3
        pantalla3=tkinter.Entry(ventana,width=60, borderwidth=None)
        pantalla3.place(x=410,y=335,relheight=0.26)
        #creando la pantalla 4
        pantalla4=tkinter.Entry(ventana,font=('Arial',16),textvariable=pant2,width=24,borderwidth=None)
        pantalla4.place(x=410,y=335,relheight=0.26)
    #Creacion de botones primera fila
        boton11 = tkinter.Button(ventana,text='x',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('x',pantalla)]).place(x=25,y=100)
        boton12 = tkinter.Button(ventana,text='y',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('y',pantalla)]).place(x=117,y=100)
        boton13 = tkinter.Button(ventana,text='x^',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('**',pantalla)]).place(x=210,y=100)
        boton14 = tkinter.Button(ventana,text='sin',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('sin',pantalla)]).place(x=301,y=100)
    ########Creacion de los botones segunda fila
        boton21 = tkinter.Button(ventana,text='π',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.click('pi',pantalla)]).place(x=25,y=150)
        boton22 = tkinter.Button(ventana,text='e',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('E',pantalla)]).place(x=117,y=150)
        boton23 = tkinter.Button(ventana,text='√',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('√',pantalla)]).place(x=209,y=150)
        boton24 = tkinter.Button(ventana,text='cos',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('cos',pantalla)]).place(x=301,y=150)
    ########Creacion de lo botones tercera fila 
        boton31 = tkinter.Button(ventana,text=',',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.click(',',pantalla)]).place(x=25,y=200)
        boton32 = tkinter.Button(ventana,text='(',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('(',pantalla)]).place(x=117,y=200)
        boton33 = tkinter.Button(ventana,text=')',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones(')',pantalla)]).place(x=209,y=200)
        boton34 = tkinter.Button(ventana,text='tan',bd=10,bg='ivory4',width=8,height=1,command=lambda:[self.modelo.operaciones('tan',pantalla)]).place(x=301,y=200)
    ########Creacion de los botones cuarta fila
        boton41 = tkinter.Button(ventana,text='7',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(7,pantalla)]).place(x=25,y=300)
        boton42 = tkinter.Button(ventana,text='8',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(8,pantalla)]).place(x=97,y=300)
        boton43 = tkinter.Button(ventana,text='9',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(9,pantalla)]).place(x=169,y=300)
        boton44 = tkinter.Button(ventana,text='DEL',bd=10,bg='yellow',width=8,height=2,command=lambda:[self.modelo.DEL(pantalla,pant,pant2,texto_pantalla,ventana)]).place(x=241,y=300)
        boton45 = tkinter.Button(ventana,text='AC',bd=10,bg='yellow',width=8,height=2,command=lambda:[self.modelo.AC(pant,pant2,texto_pantalla,ventana)]).place(x=313,y=300)
    #######Creacion de los botones 5 fila
        boton51 = tkinter.Button(ventana,text='4',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(4,pantalla)]).place(x=25,y=370)
        boton52 = tkinter.Button(ventana,text='5',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(5,pantalla)]).place(x=97,y=370)
        boton53 = tkinter.Button(ventana,text='6',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(6,pantalla)]).place(x=169,y=370)
        boton54 = tkinter.Button(ventana,text='x',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.operaciones('*',pantalla)]).place(x=241,y=370)
        boton55 = tkinter.Button(ventana,text='÷',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.operaciones('/',pantalla)]).place(x=313,y=370)
    ######Creacion de los botones 6 Fila
        boton61 = tkinter.Button(ventana,text='1',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(1,pantalla)]).place(x=25,y=440)
        boton62 = tkinter.Button(ventana,text='2',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(2,pantalla)]).place(x=97,y=440)
        boton63 = tkinter.Button(ventana,text='3',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(3,pantalla)]).place(x=169,y=440)
        boton64 = tkinter.Button(ventana,text='+',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.operaciones('+',pantalla)]).place(x=241,y=440)
        boton65 = tkinter.Button(ventana,text='-',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.operaciones('-',pantalla)]).place(x=313,y=440)
    #####Creacion de los botones 7 fila
        boton71 = tkinter.Button(ventana,text='0',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.click(0,pantalla)]).place(x=25,y=510)
        boton72 = tkinter.Button(ventana,text='.',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.operaciones('.',pantalla)]).place(x=97,y=510)
        boton73 = tkinter.Button(ventana,text='GRAF',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.grafica(ventana,pantalla)]).place(x=169,y=510)
        boton74 = tkinter.Button(ventana,text='APROX',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.aprox(pantalla,pant,pant2,texto_pantalla,ventana)]).place(x=241,y=510)
        boton75 = tkinter.Button(ventana,text='=',bd=10,bg='ivory4',width=8,height=2,command=lambda:[self.modelo.igual(pantalla,pant,pant2,texto_pantalla,ventana)]).place(x=313,y=510)
    ##Creacion de los botones de operaciones 
        boton1 = tkinter.Button(ventana,text='Graf f(x)',bd=10,bg='ivory4',font=('Arial',20),width=6,height=0,command=lambda:[self.modelo.derivar(pant,pant2,pantalla,pantalla2,pantalla4,ventana)]).place(x=25,y=600)
        boton2 = tkinter.Button(ventana,text='Grf∫',bd=10,bg='ivory4',font=('Arial',20),width=6,height=0,command=lambda:[self.modelo.integralindef(pant,pant2,pantalla,pantalla2,pantalla4,ventana)]).place(x=241,y=600)
        

        










        ventana.mainloop()