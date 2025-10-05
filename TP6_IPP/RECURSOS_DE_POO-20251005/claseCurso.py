import os
os.system("cls")

class Cursos():
    #definimos los atributos (características)
    #Id:estructura de base de datos. Clave principal de BDD
    #Este método se escribe “__init__” 
    # y para recordarlo lo puede asociar con “inicializar”. 
    #El self hace referencia al nombre del objeto en el que se encuentra escrito
    #SELF representa al objeto que se crea desde el modelo, desde la clase
    
    def __init__(self, id=0,nombre="",duracion="",modalidad=""):
        self.id=id
        self.nombre=nombre
        self.duracion=duracion
        self.modalidad=modalidad
        
    #def__init__ definimos los atributos de la clase    
    def Agregar(self):
        print("Se agrego el curso ",self.nombre, "de tipo ",self.modalidad)
    def Modificar(self):
        print("Se modificó el curso ",self.nombre, "de tipo ",self.modalidad)
    def Eliminar(self):
        print("Se elimino el curso ",self.nombre, "de tipo ",self.modalidad)
    #def Agregar(self) definimos los métodos

#creamos dos instancias de la clase CURSOS
Micurso1=Cursos(0,"Fortran","2 meses","presencial")
Micurso2=Cursos(0,"Python","3 meses","virtual")

#ejecutamos los métodos de los objetos de CURSOS
Micurso1.Eliminar()
Micurso2.Agregar()
Micurso2.Modificar()
Micurso1.Agregar()


# Se agregó el curso xxxx que tiene una duración de xxxx cuya modalidad es xxxx




