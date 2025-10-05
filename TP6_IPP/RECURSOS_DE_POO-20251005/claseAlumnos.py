import os
os.system("cls")

class Alumnos():        
    def __init__(self, id=0,nombre="",domicilio="",dni=0,edad=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
        self.edad=edad  
    def Agregar(self):
        print("Se agrego el alumno ",self.nombre,self.domicilio)
    def Modificar(self):
        print("Se modificó el alumno ",self.nombre)
    def Eliminar(self):
        print("Se eliminó el alumno ",self.nombre)

#crear tres instancias de la clase Alumnos
Alumno1=Alumnos(1,"Antonio Pereira","Cinco Saltos")
Alumno2=Alumnos(2,"Andres Fernandez","General Roca")
Alumno3=Alumnos(3,"Silvina Juarez","Neuquén")
#Ejecutamos los tres métodos
Alumno1.Agregar()
Alumno2.Modificar()
Alumno3.Eliminar()

Alumno1.Modificar()
Alumno3.Agregar()



