import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Turno():  
    # Constructor
    def __init__(self, id=0, nombre="", motivo="", fecha=date.today(), horario=f"{00}:{00}:00", medico="", recordatorios=0):
        self.id=id
        self.nombre=nombre
        self.motivo=motivo
        self.fecha=fecha
        self.horario=horario
        self.medico=medico
        self.recordatorios=recordatorios
    
    # Método para agregar un alumno
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO TurnosMedicos(NombreDelPaciente, Motivo, Fecha, Hora, Medico, OpcionesDeRecordatorio) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.motivo, self.fecha, self.horario, self.medico, self.recordatorios))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()
    # Método para modificar un alumno
    def Modificar(self):
        mensaje="Se modifico el turno del paciente %s que tiene el motivo %s con fecha %s y horario %s y medico %s y recordatorios %d CON EXITO!!!" %(self.nombre, self.motivo, self.fecha, self.horario, self.medico, self.recordatorios)
        messagebox.showinfo("MODIFICAR",mensaje)
    # Método para eliminar un alumno
    def Eliminar(self):
        mensaje="Se elimino el turno del paciente %s que tiene el motivo %s con fecha %s y horario %s y medico %s y recordatorios %d CON EXITO!!!" %(self.nombre,self.motivo,self.fecha,self.horario,self.medico,self.recordatorios)
        messagebox.showinfo("ELIMINAR",mensaje)
