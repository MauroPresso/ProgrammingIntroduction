import os
os.system("cls")

from tkinter import messagebox

class Alumnos():  
    # Constructor
    def __init__(self, id=0,nombre="",domicilio="",dni=0,edad=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
        self.edad=edad
    
    # Método para agregar un alumno
    def Agregar(self):
        mensaje="""Se agrego el alumno %s
        que vive en %s
        con dni %d
        y de %d años de edad,
        CON EXITO!!!""" %(self.nombre,self.domicilio,self.dni,self.edad)
        messagebox.showinfo("AGREGAR",mensaje)
        #messagebox.tipo("TITULO","Se agrego un nuevo alumno")
        #Alumno1=Alumnos("Jorge","Cipolletti")
        #print("Se agrego el alumno ",self.nombre,self.domicilio)

    # Método para modificar un alumno
    def Modificar(self):
        mensaje="""Se modifico el alumno %s
        que vive en %s
        con dni %d
        y de %d años de edad,
        CON EXITO!!!""" %(self.nombre,self.domicilio,self.dni,self.edad)
        messagebox.showinfo("MODIFICAR",mensaje)
        #messagebox.tipo("TITULO","Se modifico un alumno")
        #Alumno1=Alumnos("Jorge","Cipolletti")
        #print("Se modifico el alumno ",self.nombre,self.domicilio)
    
    # Método para eliminar un alumno
    def Eliminar(self):
        mensaje="""Se elimino el alumno %s
        que vive en %s
        con dni %d
        y de %d años de edad,
        CON EXITO!!!""" %(self.nombre,self.domicilio,self.dni,self.edad)
        messagebox.showinfo("ELIMINAR",mensaje)
        #messagebox.tipo("TITULO","Se elimino un alumno")
        #Alumno1=Alumnos("Jorge","Cipolletti")
        #print("Se elimino el alumno ",self.nombre,self.domicilio)