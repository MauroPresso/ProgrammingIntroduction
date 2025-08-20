import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    mi_conexion = sqlite3.connect('TP1_IPP\\Situacion\\biblioteca.db')
    # Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
    mi_cursor = mi_conexion.cursor()
    # Selecciono datos de la tabla 'CONTACTOS'
    mi_cursor.execute("SELECT * FROM LIBROS")
    # el metodo fetchall() devuelve la cantidad los registros de la consulta
    cantidad_registros = mi_cursor.fetchall()
    # Imprimo los datos obtenidos
    k = 0
    for registro in cantidad_registros:
        print(f"\nLibro nro {k + 1}.\n- ID: {registro[0]}\n- TITULO: {registro[1]}\n- AUTOR: {registro[2]}\n- GENERO: {registro[3]}\n- ANO: {registro[4]}\n")
        k = k + 1
    # TABLA ORDENADA
    input("Presione Enter para ver los registros ordenados por GENERO...")
    # Ordeno los registros por el campo 'GENERO'
    mi_cursor.execute("SELECT * FROM LIBROS ORDER BY GENERO")
    cantidad_registros_ordenados = mi_cursor.fetchall()    
    # Imprimo los datos obtenidos
    c = 0
    for registro in cantidad_registros_ordenados:
        print(f"\nLibro nro {c + 1}.\n- ID: {registro[0]}\n- TITULO: {registro[1]}\n- AUTOR: {registro[2]}\n- GENERO: {registro[3]}\n- ANO: {registro[4]}\n")
        c = c + 1
    input("Presione Enter para ver los registros ordenados por ANO...")
    # Ordeno los registros por el campo 'ANO'
    mi_cursor.execute("SELECT * FROM LIBROS ORDER BY ANO")
    cantidad_registros_ordenados = mi_cursor.fetchall()    
    # Imprimo los datos obtenidos
    i = 0
    for registro in cantidad_registros_ordenados:
        print(f"\nLibro nro {i + 1}.\n- ID: {registro[0]}\n- TITULO: {registro[1]}\n- AUTOR: {registro[2]}\n- GENERO: {registro[3]}\n- ANO: {registro[4]}\n")
        i = i + 1
    mi_conexion.close()  # Cierro la conexión a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")