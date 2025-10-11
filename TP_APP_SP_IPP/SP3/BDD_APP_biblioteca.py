import sqlite3

miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP3\\BDD_APP_biblioteca.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS PrestamosDeLibros (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NombreDelLector VARCHAR(50), Titulo VARCHAR(100), FechaDeDevolucion DATE, Categoria VARCHAR(50), ServiciosAdicionales INTEGER)''')

miConexion.close()