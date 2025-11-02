import sqlite3

miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP1\\BDD_APP_academia.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS Academia (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NombreDelEstudiante VARCHAR(50), Idioma VARCHAR(15), FechaDeInscripcion DATE, Nivel VARCHAR(50), Email VARCHAR(3), Whatsapp VARCHAR(3), Encuesta VARCHAR(3))''')

miConexion.close()