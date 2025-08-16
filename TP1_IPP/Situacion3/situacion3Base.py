# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
miConexion = sqlite3.connect('TP1_IPP\\Situacion3\\tienda.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
miCursor = miConexion.cursor()

""" 
Crear la Base de datos: tienda
Tabla: Productos con los siguientes campos:
• id_producto (entero)
• nombre_producto (texto)
• categoria (texto)
• precio (entero)
• stock (entero)
"""

miCursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE VARCHAR(25), CATEGORIA VARCHAR(25), PRECIO INTEGER, STOCK INTEGER)")

miConexion.close()  # Cierro la conexión a la base de datos