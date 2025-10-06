import sqlite3

class Conexion:
    def __init__(self):
        self.miConexion = sqlite3.connect("TP_APP_IPP\\BDD_APP.db")
        self.miCursor = self.miConexion.cursor()
        self.miCursor.execute('''CREATE TABLE Alumnos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50), domicilio VARCHAR(100), dni INTEGER, edad INTEGER)''')

    def cerrar(self):
        self.miConexion.commit()
        self.miConexion.close()