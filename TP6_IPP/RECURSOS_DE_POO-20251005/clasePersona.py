import os
os.system("cls")

#Definición de la clase Alumnos
#Con sus atributos y métodos
class Persona():
    #definimos los atributos (características)
    #Id:estructura de base de datos. Clave principal de BDD
    #Este método se escribe “__init__” 
    # y para recordarlo lo puede asociar con “inicializar”. 
    #El self hace referencia al nombre del objeto en el que se encuentra escrito
    #SELF representa al objeto que se crea desde el modelo, desde la clase
    
    def __init__(self, id=0,nombre="",domicilio="",dni=0):
        self.id=id
        self.nombre=nombre
        self.domicilio=domicilio
        self.dni=dni
               
    

