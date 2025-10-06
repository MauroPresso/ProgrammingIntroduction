import sqlite3

miConexion = sqlite3.connect("TP_APP_IPP\\BDD_APP.db")
miCursor = miConexion.cursor()
miCursor.execute('''
    CREATE TABLE IF NOT EXISTS Alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL,
        domicilio VARCHAR(100) NOT NULL,
        dni INTEGER NOT NULL,
        edad INTEGER NOT NULL
    )
''')