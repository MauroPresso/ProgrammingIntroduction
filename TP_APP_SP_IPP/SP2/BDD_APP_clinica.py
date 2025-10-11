import sqlite3

miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP2\\BDD_APP_clinica.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS TurnosMedicos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NombreDelPaciente VARCHAR(50), Motivo VARCHAR(100), Fecha DATE, Hora TIME, Medico VARCHAR(50), OpcionesDeRecordatorio INTEGER)''')

miConexion.close()