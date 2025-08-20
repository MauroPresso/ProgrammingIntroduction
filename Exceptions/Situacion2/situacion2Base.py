import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    miConexion = sqlite3.connect('TP1_IPP\\Situacion\\biblioteca.db')
    # Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
    miCursor = miConexion.cursor()
    miCursor.execute("CREATE TABLE LIBROS (ID INTEGER, TITULO VARCHAR(75), AUTOR VARCHAR(50), GENERO VARCHAR(25), ANO INTEGER)")
    miConexion.close()  # Cierro la conexión a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")