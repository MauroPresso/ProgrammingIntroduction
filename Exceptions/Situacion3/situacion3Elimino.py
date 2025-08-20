import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    mi_conexion = sqlite3.connect('Exceptions\\Situacion3\\tienda.db')
    # Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
    mi_cursor = mi_conexion.cursor()
    # Selecciono datos de la tabla 'PRODUCTOS'
    mi_cursor.execute("SELECT * FROM PRODUCTOS")
    # Elimino datos en la tabla 'EMPLEADOS'
    mi_cursor.execute("DELETE FROM PRODUCTOS WHERE PRECIO > 50000")
    mi_cursor.execute("DELETE FROM PRODUCTOS WHERE CATEGORIA = 'Higiene personal'")
    # Para que los cambios se guarden en la base de datos
    mi_conexion.commit()
    mi_conexion.close()  # Cierro la conexión a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")