# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
miConexion = sqlite3.connect('TP1_IPP\\Situacion2\\biblioteca.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
miCursor = miConexion.cursor()

""" 
Tabla: Libros con los siguientes campos:
• id_libro (entero)
• titulo (texto)
• autor (texto)
• anio_publicacion (entero)
• genero (texto)
"""

miCursor.execute("CREATE TABLE LIBROS (ID INTEGER, TITULO VARCHAR(75), AUTOR VARCHAR(50), GENERO VARCHAR(25), ANO INTEGER)")

miConexion.close()  # Cierro la conexión a la base de datos