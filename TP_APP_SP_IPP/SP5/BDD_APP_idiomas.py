import sqlite3

miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP5\\BDD_APP_idiomas.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS EscuelaDeIdiomas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NombreDelEstudiante VARCHAR(50), Idioma VARCHAR(100), FechaDeInscripcion DATE, Nivel VARCHAR(50), ServiciosAdicionales INTEGER)''')

miConexion.close()