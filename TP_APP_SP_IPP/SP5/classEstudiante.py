import os
os.system("cls")

from datetime import date
from tkinter import messagebox
from classConexion import Conexion

class Alumnos():  
    # Constructor
    def __init__(self, id=0,nombre="",idioma="", fecha=date.today(), nivel="", material="", clases="", talleres=""):
        self.id=id
        self.nombre=nombre
        self.idioma=idioma
        self.fecha=fecha
        self.nivel=nivel
        self.material=material
        self.clases=clases
        self.talleres=talleres
        
    
    # Método para agregar un alumno
    def Agregar(self):
        conexBD=Conexion()
        instruct_insert="INSERT INTO EscuelaDeIdiomas(NombreDelEstudiante, Idioma, FechaDeInscripcion, Nivel, MaterialImpreso, ClasesGrabadas, TalleresExtras) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        conexBD.miCursor.execute(instruct_insert % (self.nombre, self.idioma, self.fecha, self.nivel, self.material, self.clases, self.talleres))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO INSERT
        conexBD.cerrar()

    # Método para modificar un alumno
    def Modificar(self):
        instruct_update="UPDATE EscuelaDeIdiomas SET NombreDelEstudiante='%s', Idioma='%s', FechaDeInscripcion='%s', Nivel='%s', MaterialImpreso='%s', ClasesGrabadas='%s', TalleresExtras='%s' WHERE id=%d"
        conexBD=Conexion()
        conexBD.miCursor.execute(instruct_update % (self.nombre,self.idioma,self.fecha,self.nivel,self.material,self.clases,self.talleres,self.id))
        conexBD.miConexion.commit() # COMMIT DEL COMANDO UPDATE
        conexBD.cerrar()
    
    # Método para eliminar un alumno
    def Eliminar(self):
        instruct_delete="DELETE FROM EscuelaDeIdiomas WHERE id=%d"
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
        instruct_select="SELECT * FROM EscuelaDeIdiomas ORDER BY id DESC"
        conexBD.miCursor.execute(instruct_select)
        registros=conexBD.miCursor.fetchall()
        conexBD.cerrar()
        return registros # retorna los registros tomados por SELECT