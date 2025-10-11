import sqlite3

class Conexion:
    def __init__(self):
        self.miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP2\\BDD_APP_clinica.db")
        self.miCursor = self.miConexion.cursor()
    def cerrar(self):
        self.miConexion.commit() # COMMIT PREVIO AL CIERRE DE LA CONEXION
        self.miConexion.close()