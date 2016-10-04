#holi

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#BYRON ANDRES MOTA HERNANDEZ 15246 1ER SEMESTRE 2016
#iniciado el 11 de enero del 2016
#ALGORRITMOS Y PROGRAMACION BASICA
#CATEDRATICA, LYNETTE GARCIA
#se hicieron las siguientes consultas en el internet:
# acerca de tk.Toplevel y su herencia: http://stackoverflow.com/questions/34994991/passing-class-values-to-another-class-using-tkinter-in-python-3-5/34996060#34996060
# acerca de queries de multiples lineas: http://stackoverflow.com/questions/34776312/saving-the-result-of-a-sqlite-query-as-a-python-variable/34776463#34776463
# acerca de como hacer que la fase 3 se muevan juntas: http://stackoverflow.com/questions/4066974/scrolling-multiple-tkinter-listboxes-together
#sobre el manejo de *args y **kwargs http://stackoverflow.com/questions/3394835/args-and-kwargs

#se importan los modulos necesarios, en este caso tkinter (GUI de python), tkinter.messagebox ('popups' del GUI de python, no vienen incluidos en el modulo inicial de tkinter), os (funciones de consola), slqite3 (servicio de base de datos) en python 2.7 los mismos modulos se llaman Tkinter y tkMessageBox respectivamente

from tkinter import * 
import tkinter.messagebox as msgb
import os
import sqlite3
import matplotlib
import datetime
import MODULOPROYECTO as mdl


#---------------------------se crea la clase para la fase 1---------------------------#
class fase1(Frame):
    def _revisar(self):
        self.ventanan=Toplevel(self.master)
        self.app=Revisar(self.ventanan)


#---------------------------se crea el metodo de generar nuevas ventanas----------------------------#
    def ventanaN(self,a):
        n=a[0]
        B=str(a[1])
        m=str(n)
        op=int(m)
        nl=(None,B)
        u=self.usuar.get()
        if op in [1,2,3]:
            self.ventanan= Toplevel(self.master)
            self.app= fase3(self.ventanan,a)
        elif op==4:
            self.ventanan=Toplevel(self.master)
            self.app=mdl.Admin(self.ventanan)
        elif op==5:
            self.ventanan=Toplevel(self.master)
            self.app=fase2(self.ventanan,nl)

            
#---------------------------armado del GUI en general y definicion de algunos metodos----------------------#
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master

        #labels que contienen texto
        
        self.txt1 = Label(self, text="Usuario")
        self.txt2 = Label(self, text="Clave")

        #widgets que van a recibir usuario y contrase;a    
        self.usuar = Entry(self,width=25)
        self.contr = Entry(self, show="*",width=25)

        #se define la posicion y el estilo
        self.txt1.grid(row=0,sticky=E)
        self.txt2.grid(row=1, sticky=E) #lo que hace sticky es 'pegar' o orientar el texto en la dirección descrita (N,W,S,E, que respectivamente significa, norte, oeste, sur y este)
        self.usuar.grid(row=0, column=1)
        self.contr.grid(row=1, column=1)
        

        #boton de aceptar, envia el comando de validacion
        self.ingr = Button(self, text="Aceptar", command = self._activar,width=25)
        self.ingr.grid(row=4,column=0,columnspan=2,pady=5)

        
        

        #boton de revistar estado de cuenta
        self.cta=Button(self,text="Ver Estado de cuenta", command=self._revisar,width=25)
        self.cta.grid(row=5,column=0,columnspan=2)
        
        #se aplican los elementos a la ventana
        self.pack()
        
#---------------------------funcion de validacion-----------------------------------#
    def _activar(self):
                #se hace la conección a la base de datos
        conn=sqlite3.connect("proyecto.db")
                #se crea el cursor para los queries
        c=conn.cursor()
        #se recibe la información de la misma clase(el valor de contraseña y usuario)
        u = self.usuar.get()
        p = self.contr.get()
        #se insertan los valores en un tuple
        d=(u,p)
        #se crea una lista vacía para que almacene los queries
        row=[]
        #para cada elemento en la tabla empleado de la base de datos se crea un tuple adentro de la lista
        qry=("SELECT nombre,clave FROM empleado")
        for i in c.execute(qry):
            row.append(i)
        
        
#proceso de validación
#proceso de validacion, para los valores de la lista
        if d in row:
    #si sí están dentro de la lista se envia un mensaje de "exitoso"
            msgb.showinfo("AUTENTICACION EXITOSA", "Acceso permitido")
            
            c.execute("SELECT establecimiento FROM empleado WHERE nombre=(?)",(u,))
            esta=str(c.fetchone())
            c.execute("SELECT idemp FROM empleado WHERE nombre=(?)",(u,))
            empleado=str(c.fetchone())
            empleado=empleado.replace("(","")
            empleado=empleado.replace(")","")
            empleado=empleado.replace(",","")
            esta=esta.replace("(","")
            esta=esta.replace(")","")
            esta=esta.replace(",","")
            mvar=(esta,empleado)
            self.ventanaN(mvar)
            conn.close()
            #se ejecuta la fase dos del programa
    #si no está en la lsita, envia un mensaje de "error"        
        else:
            msgb.showerror("ERROR", "Contraseña o usuario incorrecto")



#---------------------------se crea la clase para la fase 2---------------------------#


#--------------------------------IMPORTANTE!-------------------------------------------------#
#-------------------ESTA FASE SOLAMENTE ES UTILIZADA PARA EL EMPLEADO GOD, ES PARA PRUEBAS DEL SISTEMA-------------------------#
class fase2(Frame):
    #---------------------------se crea la funcion para la creacion de una nueva ventana y la herencia de el valor x---------------------------#
    def nvvtn(self,x):
        self.vent= Toplevel(self.master)
    #se hereda la variable x
        self.app= fase3(self.vent,x)
        
        
        

         
    def __init__(self, master,a):

        Frame.__init__(self,master)
        
        self.master=master
        self.frame=Frame(self.master)
    #se crean los widjets, en los cuales se va a contener las imagenes y el texto del label
        self.logo1=PhotoImage(file="cafegit.png")
        self.logo2=PhotoImage(file="gogren.png")
        self.logo3=PhotoImage(file="bagelfact.png")
        self.txti=Label(self, text="Seleccione el restaurante donde desea hacer la transacción")

        #se posicionan los widjet
        self.txti.pack(pady=20)
        self.btn1=Button(self, image=self.logo1, command=lambda: self.nvvtn((1,a[1])), width=120)
        self.btn2=Button(self, image=self.logo2, command=lambda: self.nvvtn((2,a[1])), width=120)
        self.btn3=Button(self, image=self.logo3, command=lambda: self.nvvtn((3,a[1])), width=120)

        #se hace un espacio entre los widjet
        self.btn1.pack(pady=10)
        self.btn2.pack(pady=10)
        self.btn3.pack(pady=10)

        self.pack()
#---------------------------se crea la clase para la fase 3---------------------------#
class fase3(Frame):
    
    nom=0
    def agr(self):
        
        v=self.carntE.get()
        conn=sqlite3.connect("Proyecto.db")
        c=conn.cursor()
        
        try:
            a=int(v)
            if a in self.elemts:
                self.cargs.insert("end",a)
                self.arr.append(a)

                y=dict(self.idYp)
                self.sbttl.append((y[a]))
                r=sum(self.sbttl)
                print("subtotal?",self.sbttl)
                print("cargos?",self.arr)
                self.subtval.delete(0)  
                self.subtval.insert("end",r)
            else:
                msgb.showerror("Error", "ese elemento no pertenece a este restaurante o no existe")
        except Exception as e:
            msgb.showerror("ERROR", e)
        conn.close()
        
    def delt(self):
        a=self.remv.get()
        try:
            k=int(a)
            if k in self.arr:
                self.cargs.delete("end",k)
                self.arr.remove(k)
                y=dict(self.idYp)
                self.sbttl.remove((y[k]))
                r=sum(self.sbttl)
                self.subtval.delete(0)
                self.subtval.insert("end",r)
            else:
                msgb.showerror("ERROR", "valor no está en los valores ingresados")    
        except Exception as e:
            msgb.showerror("ERROR", e)

            
    
    def __init__(self, master,x):
        #todas estas listas van a contener los valores esenciales para la ejecucion de la tercera fase
        self.arr=[]
        self.elemts=[]
        self.prc=[]
        self.sbttl=[]
        
        self.sumSt=sum(self.sbttl)
        self.x=x
        self.ops=str(x[0])
        y=int(self.ops)
        idls=str(x[1])
        self.idempleado=int(idls)
        
        conn=sqlite3.connect("Proyecto.db")
        c=conn.cursor()
        self.idYp=[]
                         
        for i in c.execute('Select idcom,precio FROM info WHERE norest=?',(y,)):
            self.idYp.append(i)

            
        #este if define a que restaurante se ha accesado
        if y==1:
            nm="Café Gitane"
        elif y==2:
            nm="Go Green"
        elif y==3:
            nm="Bagel Factory"
            
        Frame.__init__(self,master)
        self.master=master
        self.frame=Frame(self.master)
        
        y=str(x)
        #label para el nombre del restaurante
        self.txtm=Label(self, text=nm)
        self.txtm.grid(row=1, columnspan=5)

        #label para el id del producto
        self.txt1=Label(self, text="ID producto")
        self.txt1.grid(row=2, column=1)

        #label para el nombre del producto
        self.txt2=Label(self, text="Nombre producto")
        self.txt2.grid(row=2,column=2)

        #label para el precio del producto
        self.txt3=Label(self, text="Precio producto")
        self.txt3.grid(row=2,column=3)

        #se crea scrollbar(que nunca es posicionado
        self.scrlb=Scrollbar(self,orient="vertical")

        #se crea la lista que va a contener los valores de idcom
        self.lista1=Listbox(self, yscrollcommand=self.yscroll1,exportselection=0,bd=2)
        self.lista1.grid(row=3,column=1)

        #se crea la lista que va a contener los valores de nombre
        self.lista2=Listbox(self, yscrollcommand=self.yscroll2,width=40,bd=2)
        self.lista2.grid(row=3, column=2)

        #se crea la lista que va a contener los valores de precio
        self.lista3=Listbox(self, yscrollcommand=self.yscroll3,bd=2)
        self.lista3.grid(row=3, column=3)

        #se crea el label para la instrucción
        self.carnt=Label(self,text="ingrese la id del producto -->")
        self.carnt.grid(row=4, column=1)

        #se crea el label para la entrada del valor
        self.carntE=Entry(self)
        self.carntE.grid(row=4,column=2)

        #se crea el boton para agregar un cargo
        self.agre=Button(self,text="agregar cargo",command=self.agr,bd=2)
        self.agre.grid(row=4,column=3)

        #se crea la lista que va a contener el pedido
        self.cargs=Listbox(self,bd=2)
        self.cargs.grid(row=5, column=1,rowspan=3)

        #se crea la label para la instrucción 2
        self.rest=Label(self,text="ingrese la id que desea remover -->",bd=2)
        self.rest.grid(row=5, column=2)

        #se crea la entrada para el valor a eliminar
        self.remv=Entry(self,bd=2)
        self.remv.grid(row=5, column=3)

        #se crea el boton para eliminar
        self.remvB=Button(self,command=self.delt,bd=2,text="remover")
        self.remvB.grid(row=5,column=4)

        #se crea la instrucción para ingresar el carnet
        self.carnt=Label(self,text=("Ingrese el carnet del usuario"))
        self.carnt.grid(row=6,column=2)

        #se crea el espacio para ingresar el carnet del usuario
        self.carnetE=Entry(self)
        self.carnetE.grid(row=6, column=3)
        
        
        #se crea el espacio para el subtotal
        #self.sbt=Label(self,text=("subtotal: "+str(self.subt)))
        #self.sbt.grid(row=7, column=2)
        
#--------no se implementó el widjet de scrollbar porque complicaba demasiado el codigo de manera inecesaria,
#pero su funcionalidad sigue inacta, simplemente no se posicionó en el programa

        #self.scrlb.config(command=self.yview)
        #self.scrlb.grid(row=3, column=4,rowspan=1)
        
        
       #se hace la conección a la base de datos
        y=self.ops
        conn=sqlite3.connect("Proyecto.db")
        c=conn.cursor()
        elementos=[]

        #se crea la lista con la id de la comida y el precio de esta,
        #esta lista es util para el subtotal(y total)
        self.idYp=[]
        for i in c.execute('Select idcom,precio FROM info WHERE norest=?',(y,)):
            self.idYp.append(i)
            
        #se insertan los elementos de las columnas "idcom","nombre","precio" a sus widjet
        for i in c.execute('SELECT idcom FROM info WHERE norest=?',(y,)):
            prep=str(i)
            prep=prep.replace("(","")
            prep=prep.replace(")","")
            prep=prep.replace(",","")
            prep=int(prep)
            self.lista1.insert("end",prep)
            self.elemts.append(prep)
    
        for i in c.execute('SELECT nombre FROM info WHERE norest=?',(y,)): 
            nam=str(i)
            nam=nam.replace("{","")
            nam=nam.replace("}","")
            nam=nam.replace("(","")
            nam=nam.replace(",","")
            nam=nam.replace(")","")
            self.lista2.insert("end",nam)
            
        for i in c.execute('SELECT precio FROM info WHERE norest=?',(y,)):
            self.lista3.insert("end",i)


        self.subtval=Listbox(self,height=1)
        self.subtval.grid(row=7,column=3)

        self.textsbt=Label(self,text="Subtotal: ")
        self.textsbt.grid(row=7,column=2)
        self.pack()

        self.Facturar=Button(self,text="facturar",bd=4,width=30, command=self.Facturar)
        self.Facturar.grid(row=9,column=2)
        
#-----------las siguientes funciones sirven para:----------------------#

#si hay un cambio de posicion o movimiento en la lista 1, la lista 2 y 3 se mueven tambien
    def yscroll1(self, *args):
        if  self.lista2.yview()!=self.lista1.yview()!=self.lista3.yview():
            self.lista2.yview_moveto(args[0])
            self.lista3.yview_moveto(args[0])
        self.scrlb.set(*args)
#si hay un cambio de posicion o movimiento en la lista 2, la lista 1 y 3 se mueven tambien        
    def yscroll2(self, *args):
        if  self.lista1.yview()!=self.lista2.yview()!=self.lista1.yview():
            self.lista1.yview_moveto(args[0])
            self.lista3.yview_moveto(args[0])
        self.scrlb.set(*args)
#si hay un cambio de posicion o movimiento en la lista 3, la lista 2 y 1 se mueven tambien
    def yscroll3(self, *args):
        if self.lista2.yview()!=self.lista3.yview()!=self.lista1.yview():
            self.lista1.yview_moveto(args[0])
            self.lista2.yview_moveto(args[0])
        self.scrlb.set(*args)
#sobre escribe la posicion cuando hay un cambio
    def yview(self, *args):
        self.lista1.yview(*args)
        self.lista2.yview(*args)
        self.lista3.yview(*args)

    def Facturar(self):
        fecha=datetime.datetime.now()
        carnet=self.carnetE.get()
        conn=sqlite3.connect("Proyecto.db")
        c=conn.cursor()
        c.execute("SELECT idcli FROM cliente")
        estudiantes=c.fetchall()
        clientes=[]
        for i in estudiantes:
            i=str(i)
            i=i.replace("(","")
            i=i.replace(")","")
            i=i.replace(",","")
            clientes.append(int(i))
        try:
            
            if carnet=="":
                msgb.showerror("ERROR","Debe ingresar el carnet antes de facturar")
            else:
                carnet=int(carnet)
                if carnet in clientes:

                    query="SELECT disp FROM cliente WHERE idcli="+str(carnet)
                    c.execute(query)
                    disponibilidad=c.fetchall()
                    if disponibilidad[0][0]==1:
                    
                        query = "SELECT saldo FROM cliente WHERE idcli= "+str(carnet)
                        #c.execute(("SELECT saldo FROM cliente WHERE idcli=?",(carnet,)))
                        c.execute(query)
                        saldodisp=c.fetchall()
                        total=sum(self.sbttl)
                        query="SELECT limite FROM cliente WHERE idcli= "+str(carnet)
                        c.execute(query)
                        limite=c.fetchall()
                        contador=0
                        futuro=total+saldodisp[0][0]
                        print(self.arr)
                        if (limite[0][0]-futuro)>=0:
                            for i in range(len(self.arr)):
                                idemp=str(self.idempleado)
                                carnetf=str(carnet)
                                query="INSERT into logs (idemp, idcli, idcom, fecha, precio) values (?,?,?,?,?)"
                                parametros=(int(self.idempleado),int(carnet),int(self.arr[i]),str(fecha),float(self.sbttl[i]))
                                c.execute(query,parametros)
                                contador=contador+1

                                a=self.arr[i]
                                query="SELECT pedidos FROM info WHERE idcom="+str(a)
                                c.execute(query)
                                n=c.fetchall()
                                finl=n[0][0]+1
                                print(finl)
                                query="UPDATE info SET pedidos="+str(finl)+" WHERE idcom="+str(a)
                                c.execute(query)
                                
                            msgb.showinfo("EXITO!","Cobro realizado exitosamente")
                            query="UPDATE cliente SET saldo="+str(futuro)+" WHERE idcli= "+str(carnet)
                            c.execute(query)
                            query="SELECT pedidos FROM empleado WHERE idemp= "+str(self.idempleado)
                            c.execute(query)
                            pedidosEMP=c.fetchall()
                            final=pedidosEMP[0][0]+contador
                            query="UPDATE empleado SET pedidos="+str(final)+" WHERE idemp="+str(self.idempleado)
                            c.execute(query)

                            
                             
                            conn.commit()
                        else:
                            msgb.showerror("ERROR","SALDO INSUFICIENTE PARA REALIZAR ESTA TRANSACCION")
                    else:
                        msgb.showerror("ERROR","ESTE ESTUDIANTE NO TIENE DISPONIBLE EL SERVICIO DE COBROS")
                else:
                    msgb.showerror("ERROR","El carnet ingresado no existe")
        except Exception as e:
            msgb.showerror("ERROR","Ingrese el numero de carnet, no caracteres")
            print(e)
        

class Revisar(Frame):
    def __init__(self,master):
        #I dont know what id does, but it makes it work
        Frame.__init__(self,master)
        self.master=master
        
        self.consulta=Entry(self)
        self.consulta.grid(row=1,column=1)

        self.lbl=Label(self,text="Ingrese el numero del carnet a consultar")
        self.lbl.grid(row=0,column=1)

        self.btn=Button(self,text="Revisar carnet",command=self.Buscar)
        self.btn.grid(row=2,column=1)
        
        
        self.pack()
        
    def Buscar(self):
        crnt=self.consulta.get()
        conn=sqlite3.connect('Proyecto.db')
        c=conn.cursor()
        try:
            carnet=int(crnt)
            persns=[]
            c.execute("SELECT * FROM cliente WHERE idcli=(?)",(carnet,))
            res=c.fetchall()
            if len(res) is not 0:
                if res[0][3]==1:
                    alerta=None
                    SaldoAct=res[0][5]
                    SaldoPem=res[0][4]
                    SaldoFN=SaldoPem-SaldoAct
                    msgb.showinfo("Saldo Actual", "Su saldo Actual es de: "+str(SaldoAct)+" Le quedan disponibles: Q"+str(SaldoFN))
                else:
                    msgb.showerror("Error","esta persona no tiene habilitada el servicio de creditos")
            else:
                msgb.showerror("Error","no se ha creado la persona con el carnet mencionado")
                
        except Exception as e:
            print("error",e)

                    
#se crea el objeto TK (ventana del programa)
root = Tk()

#se crea el marco en donde irÃ¡ el programa
marco= Frame(root, padx=100, pady=50)

#se 'pone' el marco en la ventana 
marco.pack()

#se instancia la clase 'fase1'
lf = fase1(marco)

#se mantiene el programa abierto, esto es necesario, de lo contrario se cerrarÃ¡ al terminar de ejecutarse una vez
root.mainloop()
