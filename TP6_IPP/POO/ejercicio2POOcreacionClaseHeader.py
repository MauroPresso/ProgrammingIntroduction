# Ejercicio 1 - Programación Orientada a Objetos
"""
Este ejercicio consiste en crear una clase que represente un el encabezado de la información de un dispositivo de una red de control de procesos industriales,
con atributos como ID, tipo e información.
"""

class Header():
    def __init__(self, id=0, tipo="", info=""):
        self.id = id
        self.tipo = tipo
        self.info = info