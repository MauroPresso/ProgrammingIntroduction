import sqlite3

miConexion = sqlite3.connect("TP_APP_IPP\\BDD_APP.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50), domicilio VARCHAR(100), dni INTEGER, edad INTEGER)''')

miConexion.close()