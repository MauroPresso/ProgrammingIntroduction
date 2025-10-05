import os
os.system("cls")

class Docentes():  
   
    def __init__(self, id=0,nombre="",domicilio="",dni=0,categoria=0,
    antiguedad=0,sueldo=0):
        self.id=id
        self.nombre=nombre
        self.domiciclio=domicilio
        self.dni=dni
        self.categoria=categoria
        self.antiguedad=antiguedad
        self.sueldo=sueldo
   
    def Agregar(self):
        print("Se agrego el docente ",self.nombre, "con ",self.antiguedad," años de experiencia")
    def Modificar(self):
        print("Se modificó el docente ",self.nombre, "con ",self.antiguedad," años de experiencia")
    def Eliminar(self):
        print("Se eliminó el docente ",self.nombre, "con ",self.antiguedad," años de experiencia")

#creamos 3 objetos de la clase docente
Docente1=Docentes(0,"Ing Gonzalez",antiguedad=10)
Docente2=Docentes(1,"Ing Garcia",antiguedad=5)
Docente3=Docentes(2,"Ing Fernandez",antiguedad=7)

Docente1.Modificar()
Docente2.Agregar()
Docente3.Eliminar()

#Cada docente con cada método.
#Inventen ustedes la salida

