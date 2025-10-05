import os
os.system("cls")

#From el archivo clasePersona importo a Persona
from clasePersona import Persona
from claseEmpleado import Empleado

#Definición de la clase Administrativo
#Con sus atributos y métodos
class Administrativo(Persona,Empleado):    
    def __init__(self, id=0,nombre="",domicilio="",dni=0,categoria=0,
        antiguedad=0,sueldo=0):
        Persona.__init__(self,id,nombre,domicilio,dni)
        Empleado.__init__(self,categoria,antiguedad,sueldo)
   
   