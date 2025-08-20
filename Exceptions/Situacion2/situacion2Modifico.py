import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    mi_conexion = sqlite3.connect('TP1_IPP\\Situacion\\biblioteca.db')
    # Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
    mi_cursor = mi_conexion.cursor()
    # Selecciono datos de la tabla 'LIBROS'
    mi_cursor.execute("SELECT * FROM LIBROS")
    # Modifico datos en la tabla 'EMPLEADOS'
    mi_cursor.execute("UPDATE LIBROS SET ANO = 1945 WHERE TITULO = 'Los amorios de un procer'")
    mi_cursor.execute("UPDATE LIBROS SET AUTOR = 'Jose Alvarado' WHERE AUTOR = 'Pepe Sanchez'")
    mi_cursor.execute("UPDATE LIBROS SET TITULO = 'Furia Nocturna' WHERE GENERO = 'Terror'")
    mi_cursor.execute("UPDATE LIBROS SET TITULO = 'El reino de Melniboné' WHERE ANO = 2011")
    mi_cursor.execute("UPDATE LIBROS SET GENERO = 'Novela Juvenil' WHERE ID = 8")
    # Para que los cambios se guarden en la base de datos
    mi_conexion.commit()
    mi_conexion.close()  # Cierro la conexión a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")