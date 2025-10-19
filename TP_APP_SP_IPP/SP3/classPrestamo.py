import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Prestamo():  
    # Constructor
    def __init__(self, id=0, nombre="",titulo="", fecha=date.today(), categoria="", servicios=0):
        self.id=id
        self.nombre=nombre
        self.titulo=titulo
        self.fecha=fecha
        self.categoria=categoria
        self.servicios=servicios
    
    # Método para agregar un prestamo
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO PrestamosDeLibros(NombreDelLector, Titulo, FechaDeDevolucion, Categoria, ServiciosAdicionales) VALUES ('%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.titulo, self.fecha, self.categoria, self.servicios))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        conexBD.cerrar()

    # Método para modificar un prestamo
    def Modificar(self):
        mensaje="""Se modifico el prestamo del lector %s
        que tiene el libro %s
        con fecha de devolucion %s
        y categoria %s
        y servicios adicionales %d
        CON EXITO!!!""" %(self.nombre,self.titulo,self.fecha,self.categoria,self.servicios)
        messagebox.showinfo("MODIFICAR",mensaje)

    
    # Método para eliminar un prestamo
    def Eliminar(self):
        mensaje="""Se elimino el prestamo del lector %s
        que tiene el libro %s
        con fecha de devolucion %s
        y categoria %s
        y servicios adicionales %d
        CON EXITO!!!""" %(self.nombre,self.titulo,self.fecha,self.categoria,self.servicios)
        messagebox.showinfo("ELIMINAR",mensaje)

    # Método para listar prestamos
    def ListarPrestamos():
        conexBD=Conexion()
        instruct_select="SELECT * FROM PrestamosDeLibros ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        lista_prestamos=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return lista_prestamos
