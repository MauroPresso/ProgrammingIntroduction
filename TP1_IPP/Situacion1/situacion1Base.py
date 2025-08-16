# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
miConexion = sqlite3.connect('empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
miCursor = miConexion.cursor()

""" 
    Creo una base de datos llamada empresa con los campos (columnas):
        • id (entero).
        • nombre (texto)
        • apellido (texto)
        • puesto (texto)
        • salario (entero).
"""

miCursor.execute("CREATE TABLE EMPLEADOS (ID INTEGER, NOMBRE VARCHAR(25), APELLIDO VARCHAR(25), PUESTO VARCHAR(25), SALARIO INTEGER)")

miConexion.close()  # Cierro la conexión a la base de datos