# Ejercicio 1 - Programación Orientada a Objetos
"""
Este ejercicio consiste en crear una clase que represente un alumno, con atributos como nombre, edad y DNI.
"""

class ALumno():
    def __init__(self, id=0, nombre="", domicilio="", edad=0, dni=0): # Inicializador de la clase
        self.id = id
        self.nombre = nombre
        self.domicilio = domicilio
        self.edad = edad
        self.dni = dni