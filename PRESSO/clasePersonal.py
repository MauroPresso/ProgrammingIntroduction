import os
os.system("cls")

from tkinter import messagebox
from claseConexion import Conexion

class Personal():  
    # Constructor
    def __init__(self, id=0,nombre="",apellido="",email="",capacitacion="",modalidad=""):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.capacitacion=capacitacion
        self.modalidad=modalidad

    # Método para agregar un personal
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO Capacitacion (Nombre, Apellido, Email, Capacitacion, Modalidad) VALUES ('%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.apellido, self.email, self.capacitacion, self.modalidad))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        conexBD.cerrar()

    # Método para modificar un personal
    def Modificar(self):
        instruct_update="UPDATE Capacitacion SET Nombre='%s', Apellido='%s', Email='%s', Capacitacion='%s', Modalidad='%s' WHERE id=%d"
        conexBD=Conexion()
        conexBD.miCursor.execute(instruct_update % (self.nombre,self.apellido,self.email,self.capacitacion,self.modalidad,self.id))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO UPDATE
        conexBD.cerrar()
    
    # Método para eliminar un personal
    def Eliminar(self):
        instruct_delete="DELETE FROM Capacitacion WHERE id=%d"
        conexBD=Conexion()
        try:
            conexBD.miCursor.execute(instruct_delete % (self.id))
            conexBD.miConexion.commit() # COMMIT DEL COMANDO DELETE
            messagebox.showinfo("ELIMINADO", "Registro eliminado correctamente.")
        except:
            messagebox.showerror("ERROR", "No se pudo eliminar el registro.")
        conexBD.cerrar()

    # Metodo para listar alumnos
    def ListaCapacitaciones(): # no necesita self porque no usa atributos de instancia.
        conexBD=Conexion()
        instruct_select="SELECT * FROM Capacitacion ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        registros=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return registros # retorna los registros tomados por SELECT