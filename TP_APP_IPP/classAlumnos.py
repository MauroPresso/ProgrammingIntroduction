import os
os.system("cls")

from tkinter import messagebox
from classConexion import Conexion

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
        conexBD=Conexion()
        instruct_insert="INSERT INTO Alumnos(nombre, domicilio, dni, edad) VALUES ('%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.domicilio, self.dni, self.edad))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()

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

    # Metodo para listar alumnos
    def ListaAlumnos(self):
        conexBD=Conexion()
        instruct_select="SELECT * FROM Alumnos ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        registros=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return registros # retorna los registros tomados por SELECT
        