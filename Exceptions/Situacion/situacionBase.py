import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    miConexion = sqlite3.connect('TP1_IPP\\Situacion\\empresa.db')
    miCursor = miConexion.cursor()
    miCursor.execute("CREATE TABLE EMPLEADOS (ID INTEGER, NOMBRE VARCHAR(25), APELLIDO VARCHAR(25), PUESTO VARCHAR(25), SALARIO INTEGER)")
    miConexion.close()  # Cierro la conexión a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")
