import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Alumnos():  
    # Constructor
    def __init__(self, id=0,nombre="",idioma="", fecha=date.today(), nivel="", email="", whatsapp="", encuesta=""):
        self.id=id
        self.nombre=nombre
        self.idioma=idioma
        self.fecha=fecha
        self.nivel=nivel
        self.email=email
        self.whatsapp=whatsapp
        self.encuesta=encuesta
        
    
    # Método para agregar un alumno
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO Academia(nombre, idioma, fecha, nivel, email, whatsapp, encuesta) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.idioma, self.fecha, self.nivel, self.email, self.whatsapp, self.encuesta))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        conexBD.cerrar()

    # Método para modificar un alumno
    def Modificar(self):
        instruct_update="UPDATE Academia SET nombre='%s', idioma='%s', fecha='%s', nivel='%s', email='%s', whatsapp='%s', encuesta='%s' WHERE id=%d"
        conexBD=Conexion()
        conexBD.miCursor.execute(instruct_update % (self.nombre,self.idioma,self.fecha,self.nivel,self.email,self.whatsapp,self.encuesta,self.id))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO UPDATE
        conexBD.cerrar()
    
    # Método para eliminar un alumno
    def Eliminar(self):
        instruct_delete="DELETE FROM Academia WHERE id=%d"
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
        instruct_select="SELECT * FROM Academia ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        registros=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return registros # retorna los registros tomados por SELECT