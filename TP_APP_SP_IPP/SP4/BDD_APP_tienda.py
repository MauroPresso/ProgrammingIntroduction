import sqlite3

miConexion = sqlite3.connect("TP_APP_SP_IPP\\SP4\\BDD_APP_tienda.db")
miCursor = miConexion.cursor()

miCursor.execute('''CREATE TABLE IF NOT EXISTS TiendaOnline (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, NombreDelCliente VARCHAR(50), Producto VARCHAR(100), FechaDeEntregaAprox DATE, HorarioDeEntregaAprox TIME, TipoDeCuenta VARCHAR(50), Preferencias INTEGER)''')

miConexion.close()