# Ejercicio 1 - Programación Orientada a Objetos
"""
Este ejercicio consiste en crear una clase que represente un el encabezado de la información de un dispositivo de una red de control de procesos industriales,
con atributos como ID, tipo e información.
"""

class Header():
    def __init__(self, id, tipo, info):
        self.id = id
        self.tipo = tipo
        self.info = info

    # Otros métodos de la clase
    def Agregar(self):
        print(f"Se agrego el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")
    def Modificar(self):
        print(f"Se modificó el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")
    def Eliminar(self):
        print(f"Se eliminó el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")