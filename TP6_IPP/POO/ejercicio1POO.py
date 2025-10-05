# Ejercicio 1 - Programación Orientada a Objetos
"""
Este ejercicio consiste en crear una clase que represente un alumno, con atributos como nombre, edad y DNI.
"""

class ALumno():
    # Constructor de la clase (me permite inicializar los atributos del objeto)
    def __init__(self, id=0, nombre="", domicilio="", edad=0, dni=0): 
        self.id = id
        self.nombre = nombre
        self.domicilio = domicilio
        self.edad = edad
        self.dni = dni
    # Otros métodos de la clase
    def Agregar(self):
        print(f"Se agrego el alumno:\n-Nombre: {self.nombre}\n-Edad: {self.edad}\n-DNI: {self.dni}")
    def Modificar(self):
        print(f"Se modificó el alumno:\n-Nombre: {self.nombre}\n-Edad: {self.edad}\n-DNI: {self.dni}")
    def Eliminar(self):
        print(f"Se eliminó el alumno:\n-Nombre: {self.nombre}\n-Edad: {self.edad}\n-DNI: {self.dni}")