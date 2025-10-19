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

    # Método para agregar una compra
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO TiendaOnline(NombreDelCliente, Producto, FechaDeEntregaAprox, HorarioDeEntregaAprox, TipoDeCuenta, Preferencias) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()
    # Método para modificar una compra
    def Modificar(self):
        mensaje="Se modifico la compra de %s que tiene el producto %s con fecha %s y horario %s y tipo de cuenta %s y preferencias %d CON EXITO!!!" %(self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias)
        messagebox.showinfo("MODIFICAR",mensaje)
    # Método para eliminar una compra
    def Eliminar(self):
        mensaje="Se elimino la compra de %s que tiene el producto %s con fecha %s y horario %s y tipo de cuenta %s y preferencias %d CON EXITO!!!" %(self.nombre, self.producto, self.fecha, self.horario, self.tipoDeCuenta, self.preferencias)
        messagebox.showinfo("ELIMINAR",mensaje)
    # Metodo para listar compras
    def ListarCompras(): # no necesita self porque no usa atributos de instancia.
        conexBD=Conexion() # crea el objeto de conexion
        instruct_select="SELECT * FROM TiendaOnline ORDER BY id DESC" # ORDER BY id DESC para que muestre primero los mas viejos
        conexBD.miCursor.execute(instruct_select) # ejecuta el SELECT
        registros=conexBD.miCursor.fetchall() # fetchall() toma todos los registros del SELECT
        conexBD.cerrar() # cierra la conexion
        return registros # retorna los registros tomados por SELECT