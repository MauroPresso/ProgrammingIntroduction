import sqlite3

miConexion = sqlite3.connect("DATOS.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS Capacitacion (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Nombre VARCHAR(50), Apellido VARCHAR(50), Email VARCHAR(50), Capacitacion VARCHAR(50), Modalidad VARCHAR(20))''')

miConexion.close()