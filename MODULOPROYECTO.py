from tkinter import *
import sqlite3
import tkinter.messagebox as msgb

class Admin(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master

        self.btn1=Button(self, text="Ver Usuarios", command=lambda:self.nvt(1),width=20,bd=4)
        self.btn1.grid(column=1,row=0)

        self.btn2=Button(self, text="Ver Empleados",command=lambda:self.nvt(2),width=20,bd=4)
        self.btn2.grid(column=1,row=1)

        self.btn3=Button(self, text="Ver Comidas",command=lambda:self.nvt(3),width=20,bd=4)
        self.btn3.grid(column=1,row=2)

        self.btn4=Button(self, text="Ver Registros",command=lambda:self.nvt(4),width=20,bd=4)
        self.btn4.grid(column=1,row=3)

        self.btn5=Button(self, text="Agregar comida", command=lambda:self.nvt(5),width=20,bd=4)
        self.btn5.grid(column=2,row=0)

        self.btn6=Button(self, text="Agregar empleado", command=lambda:self.nvt(6),width=20,bd=4)
        self.btn6.grid(column=2,row=1)

        self.btn7=Button(self, text="Agregar Cliente", command=lambda:self.nvt(7),width=20,bd=4)
        self.btn7.grid(column=2,row=2)

        self.btn8=Button(self, text="Eliminar Comida", command=lambda:self.nvt(8),width=20,bd=4)
        self.btn8.grid(column=3,row=0)

        self.btn9=Button(self, text="Eliminar Empleado",command=lambda:self.nvt(9),width=20,bd=4)
        self.btn9.grid(column=3,row=1)

        self.btn10=Button(self, text="Eliminar Cliente",command=lambda:self.nvt(10),width=20,bd=4)
        self.btn10.grid(column=3,row=2)

        

        self.btn12=Button(self, text="Ver ventas de empleado",command=lambda:self.nvt(12),width=20,bd=4)
        self.btn12.grid(column=4, row=0)

        self.btn13=Button(self, text="Ver demanda de comida", command=lambda:self.nvt(13), width=20, bd=4)
        self.btn13.grid(column=4, row=1)

        self.btn14=Button(self, text="Ver consumos de Usuarios", command=lambda:self.nvt(14), width=20, bd=4)
        self.btn14.grid(column=4, row=2)

        self.btn15=Button(self, text="Hacer una Transaccion", command=lambda:self.nvt(15), width=20, bd=4)
        self.btn15.grid(column=4, row=3)

        self.pack()
        
    def nvt(self,x):
        if x==1:
            self.nuevaV=Toplevel(self.master)
            self.app=VerUs(self.nuevaV)
        elif x==2:
            self.nuevaV=Toplevel(self.master)
            self.app=VerEm(self.nuevaV)
        elif x==3:
            self.nuevaV=Toplevel(self.master)
            self.app=VerCom(self.nuevaV)
        elif x==4:
            self.nuevaV=Toplevel(self.master)
            self.app=VerRe(self.nuevaV)
        elif x==5:
            self.nuevaV=Toplevel(self.master)
            self.app=AgrCom(self.nuevaV)
        elif x==6:
            self.nuevaV=Toplevel(self.master)
            self.app=AgrEmp(self.nuevaV)
        elif x==7:
            self.nuevaV=Toplevel(self.master)
            self.app=AgrCli(self.nuevaV)
        elif x==8:
            pass
        elif x==9:
            pass
        elif x==10:
            pass
        elif x==11:
            pass
        elif x==12:
            pass
    
class VerUs(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master
        espacio="----------------------------"
        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.Usuario=Listbox(self, width=75)
        self.Usuario.grid(row=1, column=1)

        for i in c.execute("SELECT * FROM cliente"):
            self.Usuario.insert("end",i)
            self.Usuario.insert("end",espacio)
        self.pack()

        conn.close()
        
class VerEm(Frame):
    def __init__(self,master):
        
        Frame.__init__(self,master)
        self.master=master
        espacio="----------------------------"
        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.Usuario=Listbox(self)
        self.Usuario.grid(row=1, column=1)

        for i in c.execute("SELECT * FROM empleado"):
            self.Usuario.insert("end",i)
            self.Usuario.insert("end",espacio)
        self.pack()

        conn.close()
        
class VerCom(Frame):
    def __init__(self,master):
        
        Frame.__init__(self,master)
        self.master=master

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.Usuario=Listbox(self,width=50)
        self.Usuario.grid(row=1, column=1)
        espacio="----------------------------"

        for i in c.execute("SELECT * FROM info"):
            self.Usuario.insert("end",i)
            self.Usuario.insert("end",espacio)
        self.pack()

        conn.close()

class VerRe(Frame):
    def __init__(self,master):
        
        Frame.__init__(self,master)
        self.master=master

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.Usuario=Listbox(self,width=50)
        self.Usuario.grid(row=1, column=1)
        espacio="----------------------------"

        for i in c.execute("SELECT * FROM logs"):
            self.Usuario.insert("end",i)
            self.Usuario.insert("end",espacio)
        self.pack()

        conn.close()

class AgrCom(Frame):
    def __init__(self,master):
        
        Frame.__init__(self,master)
        self.master=master

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.txt1=Label(self,text="Ingrese el numero del restaurante (1-3)")
        self.txt1.grid(column=0, row=0)

        self.txt2=Label(self, text="Ingrese el nombre de la comida")
        self.txt2.grid(column=0,row=1)

        self.txt3=Label(self, text="Ingrese el precio de la comida")
        self.txt3.grid(column=0, row=2)

        self.ent1=Entry(self)
        self.ent1.grid(column=1,row=0)

        self.ent2=Entry(self)
        self.ent2.grid(column=1,row=1)

        self.ent3=Entry(self)
        self.ent3.grid(column=1,row=2)

        self.btn1=Button(self, text="Ingresar", command=self.validar)
        self.btn1.grid(column=1,row=3)

        
        self.pack()

    def validar(self):
        a=self.ent1.get()
        b=self.ent2.get()
        d=self.ent3.get()

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()
        
        try:
            a=int(a)
            b=str(b)
            d=float(d)
            if a not in [1,2,3]:
                msgb.showerror("ERROR","Usted Ha ingresado un numero de restaurante invalido")
            else:
                c.execute("INSERT INTO info(norest,nombre,precio,pedidos) values(?,?,?,?)",(a,b,d,0))
                msgb.showinfo("Exito!","Inserción a la base de datos exitosa")
                conn.commit()
                conn.close()
        except Exception as e:
            msgb.showerror("ERROR","Alguno de los valores ingresados no es valido")
            print(e)
            
class AgrEmp(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.txt1=Label(self,text="Ingrese nombre del empleado")
        self.txt1.grid(column=0, row=0)

        self.txt2=Label(self, text="Ingrese la clave de acceso para ese empleado")
        self.txt2.grid(column=0,row=1)

        self.txt3=Label(self, text="Ingrese el establecimiento donde trabaja (1-3) o 4 si es administrador")
        self.txt3.grid(column=0, row=2)

        self.ent1=Entry(self)
        self.ent1.grid(column=1,row=0)

        self.ent2=Entry(self)
        self.ent2.grid(column=1,row=1)

        self.ent3=Entry(self)
        self.ent3.grid(column=1,row=2)

        self.btn1=Button(self, text="Ingresar", command=self.validar)
        self.btn1.grid(column=1,row=3)

        
        self.pack()

    def validar(self):
        a=self.ent1.get()
        b=self.ent2.get()
        d=self.ent3.get()

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()
        
        try:
            d=int(d)
            if d not in [1,2,3,4]:
                msgb.showerror("ERROR","Usted Ha ingresado un numero de restaurante invalido")
            else:
                c.execute("INSERT INTO empleado( nombre, clave,establecimiento,pedidos) values(?,?,?,?)",(a, b,d, 0))
                msgb.showinfo("Exito!","Inserción a la base de datos exitosa")
                conn.commit()
                conn.close()
        except Exception as e:
            msgb.showerror("ERROR","Alguno de los valores ingresados no es valido")
            print(e)

class AgrCli(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master

        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()

        self.txt1=Label(self,text="Ingrese carnet del estudiante")
        self.txt1.grid(column=0, row=0)

        self.txt2=Label(self, text="Ingrese el nombre del estudiante")
        self.txt2.grid(column=0,row=1)

        self.txt3=Label(self, text="Ingrese la carrera del estudiante")
        self.txt3.grid(column=0, row=2)

        self.txt4=Label(self,text="Este servicio es disponible? (1=si, 0=no)")
        self.txt4.grid(column=0,row=3)

        self.txt5=Label(self,text="Cual va a ser el limite de consumo para este estudiante?")
        self.txt5.grid(column=0, row=4)

        self.ent1=Entry(self)
        self.ent1.grid(column=1,row=0)

        self.ent2=Entry(self)
        self.ent2.grid(column=1,row=1)

        self.ent3=Entry(self)
        self.ent3.grid(column=1,row=2)

        self.ent4=Entry(self)
        self.ent4.grid(column=1,row=3)

        self.ent5=Entry(self)
        self.ent5.grid(column=1,row=4)

        self.btn1=Button(self, text="Ingresar", command=self.validar)
        self.btn1.grid(column=1,row=5)

        
        self.pack()

    def validar(self):
        a=self.ent1.get()
        b=self.ent2.get()
        d=self.ent3.get()
        e=self.ent4.get()
        f=self.ent5.get()
        
        conn=sqlite3.connect("proyecto.db")
        c=conn.cursor()
        
        try:
            a=int(a)
            f=int(f)
            e=int(e)
            if e not in [0,1]:
                msgb.showerror("ERROR","Usted Ha ingresado un numero de restaurante invalido")
            else:
                c.execute("INSERT INTO cliente(idcli,nombre,carrera,disp,limite,saldo) values(?,?,?,?,?,?)",(a,b,d,e,f,0))
                msgb.showinfo("Exito!","Inserción a la base de datos exitosa")
                conn.commit()
                conn.close()
        except Exception as e:
            msgb.showerror("ERROR","Alguno de los valores ingresados no es valido")
            print(e)
