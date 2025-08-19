import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion2\\biblioteca.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Selecciono datos de la tabla 'LIBROS'
mi_cursor.execute("SELECT * FROM LIBROS")

# Elimino datos en la tabla 'LIBROS'
mi_cursor.execute("DELETE FROM LIBROS WHERE GENERO = 'Terror'")
mi_cursor.execute("DELETE FROM LIBROS WHERE ANO = 1945")

# Para que los cambios se guarden en la base de datos
mi_conexion.commit()

mi_conexion.close()  # Cierro la conexión a la base de datos