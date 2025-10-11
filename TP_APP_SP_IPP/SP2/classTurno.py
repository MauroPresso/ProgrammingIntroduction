import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Turno():  
    # Constructor
    def __init__(self, id=0, nombre="", motivo="", fecha=date.today(), hora="", medico="", servicios=0):
        self.id=id
        self.nombre=nombre
        self.motivo=motivo
        self.fecha=fecha
        self.medico=medico
        self.servicios=servicios
    
    # Método para agregar un alumno
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO TurnosMedicos(NombreDelPaciente, Motivo, Fecha, Hora, Medico, Servicios) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.motivo, self.fecha, self.hora, self.medico, self.servicios))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()

    # Método para modificar un alumno
    def Modificar(self):
        mensaje="""Se modifico el prestamo del lector %s
        que tiene el libro %s
        con fecha de devolucion %s
        y categoria %s
        y servicios adicionales %d
        CON EXITO!!!""" %(self.nombre,self.titulo,self.fecha,self.categoria,self.servicios)
        messagebox.showinfo("MODIFICAR",mensaje)

    
    # Método para eliminar un alumno
    def Eliminar(self):
        mensaje="""Se elimino el prestamo del lector %s
        que tiene el libro %s
        con fecha de devolucion %s
        y categoria %s
        y servicios adicionales %d
        CON EXITO!!!""" %(self.nombre,self.titulo,self.fecha,self.categoria,self.servicios)
        messagebox.showinfo("ELIMINAR",mensaje)
