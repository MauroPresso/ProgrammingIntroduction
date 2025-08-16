# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
conexion = sqlite3.connect('TP0_IPP\\basededatos0.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
cursor = conexion.cursor()

# Creo una tabla llamada 'clientes' con columnas 'nombre' y 'edad'
cursor.execute("CREATE TABLE CONTACTOS (NOMBRE VARCHAR(50), TELEFONO INTEGER)")

conexion.close()  # Cierro la conexión a la base de datos