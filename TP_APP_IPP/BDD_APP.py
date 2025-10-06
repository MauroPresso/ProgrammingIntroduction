import sqlite3

miConexion = sqlite3.connect("TP_APP_IPP\\BDD_APP.db")
miCursor = miConexion.cursor()
miCursor.execute('''CREATE TABLE Alumnos (id INTEGER NOT NULLPRIMARY KEY AUTOINCREMENT, nombre VARCHAR(50), domicilio VARCHAR(100), dni INTEGER, edad INTEGER)''')