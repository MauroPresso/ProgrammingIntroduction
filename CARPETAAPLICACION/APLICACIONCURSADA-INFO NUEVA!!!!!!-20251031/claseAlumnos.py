import os
os.system("cls")
from tkinter import messagebox
from conexion import conexionBD

#Definición de la clase Alumnos
#Con sus atributos y métodos
class Alumnos():
     
    def __init__(self, id=0,nombre="",domicilio="",dni=0,edad=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
        self.edad=edad
    #def__init__ definimos los atributos de la clase    
    
    def Agregar(self):
        conexBD=conexionBD()
        #INSERT INTO <TABLA> (CAMPOS) VALUES VALORES....
        sql="insert into ALUMNOS(nombre,domicilio,dni,edad) values ('%s','%s','%s','%s')"
        conexBD.cursor.execute(sql%(self.nombre,self.domicilio,self.dni,self.edad))
        conexBD.con.commit()
        messagebox.showinfo("AGREGAR","nuevo alumno ingresado")
        conexBD.cerrar()             

    def listaAlumno():    
        conexBD=conexionBD()
        #select * FROM <TABLA> ORDER BY <CAMPO>
        sql='select * from Alumnos order by id desc'
        #ejecuto la instrucción sql
        conexBD.cursor.execute(sql)
        #fetchall() toma todos los datos
        datos=conexBD.cursor.fetchall()
        conexBD.cerrar()
        #quiero que la variable datos me devuelva el contenido en esa variable
        return datos
        #ahora nos vamos a la interfaz gráfica    

    def Modificar(self):
        #print("Se modificó el alumno ",self.nombre)
        conexBD=conexionBD()
        sql="update alumnos set Nombre='%s',Domicilio='%s',Dni=%s,Edad=%s where id=%s"
        conexBD.cursor.execute(sql %(self.nombre,self.domicilio,self.dni,self.edad,self.id))
        conexBD.con.commit()
        messagebox.showinfo("MODIFICAR","Datos de alumno modificado")
        conexBD.cerrar()

    def Eliminar(self):
        #print("Se eliminó el alumno ",self.nombre)
        conexDB=conexionBD()
        sql="delete from alumnos where id=%s"
        try:
            conexDB.cursor.execute(sql %self.id)
            conexDB.cerrar()
            messagebox.showinfo('ELIMINAR','Alumno eliminado!')
        except:
            messagebox.showerror('ELIMINAR','No se ha seleccionado ningún alumno')    
    
        
    


