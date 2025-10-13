import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Compra():  
    # Constructor
    def __init__(self, id=0, nombre="", producto="", fecha=date.today(), horario=f"{00}:{00}:00", tipoDeCuenta="", preferencias=0):
        self.id=id
        self.nombre=nombre
        self.producto=producto
        self.fecha=fecha
        self.horario=horario
        self.tipoDeCuenta=tipoDeCuenta
        self.preferencias=preferencias

    # Método para agregar un alumno
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO TiendaOnline(NombreDelCliente, Producto, FechaDeEntregaAprox, HorarioDeEntregaAprox, TipoDeCuenta, Preferencias) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()
    # Método para modificar un alumno
    def Modificar(self):
        mensaje="Se modifico la compra de %s que tiene el producto %s con fecha %s y horario %s y tipo de cuenta %s y preferencias %d CON EXITO!!!" %(self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias)
        messagebox.showinfo("MODIFICAR",mensaje)
    # Método para eliminar un alumno
    def Eliminar(self):
        mensaje="Se elimino la compra de %s que tiene el producto %s con fecha %s y horario %s y tipo de cuenta %s y preferencias %d CON EXITO!!!" %(self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias)
        messagebox.showinfo("ELIMINAR",mensaje)
