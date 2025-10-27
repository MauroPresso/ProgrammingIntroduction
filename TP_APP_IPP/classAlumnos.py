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
        conexBD.cerrar()

    # Método para modificar un alumno
    def Modificar(self):
        instruct_update="UPDATE Alumnos SET nombre='%s', domicilio='%s', dni='%s', edad='%s' WHERE id=%d"
        conexBD=Conexion()
        conexBD.miCursor.execute(instruct_update % (self.nombre,self.domicilio,self.dni,self.edad,self.id))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO UPDATE
        conexBD.cerrar()
    
    # Método para eliminar un alumno
    def Eliminar(self):
        instruct_delete="DELETE FROM Alumnos WHERE id=%d"
        conexBD=Conexion()
        try:
            conexBD.miCursor.execute(instruct_delete % (self.id))
            conexBD.miConexion.commit() # COMMIT DEL COMANDO DELETE
            messagebox.showinfo("ELIMINADO", "Registro eliminado correctamente.")
        except:
            messagebox.showerror("ERROR", "No se pudo eliminar el registro.")
        conexBD.cerrar()

    # Metodo para listar alumnos
    def ListaAlumnos(): # no necesita self porque no usa atributos de instancia.
        conexBD=Conexion()
        instruct_select="SELECT * FROM Alumnos ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        registros=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return registros # retorna los registros tomados por SELECT
        