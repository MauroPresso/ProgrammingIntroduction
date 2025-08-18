import os
os.system('cls')
# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion1\\empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Selecciono datos de la tabla 'CONTACTOS'
mi_cursor.execute("SELECT * FROM EMPLEADOS")

# el metodo fetchall() devuelve la cantidad los registros (filas) de la consulta
cantidad_registros = mi_cursor.fetchall()

# Imprimo los datos obtenidos
k = 0
for registro in cantidad_registros:
    print(f"\nEmpleado nro {k + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    k = k + 1
# TABLA ORDENADA
input("Presione Enter para ver los registros ordenados por puesto...")
# Ordeno los registros por el campo 'NOMBRE'
mi_cursor.execute("SELECT * FROM EMPLEADOS ORDER BY PUESTO")
cantidad_registros_ordenados = mi_cursor.fetchall()    
# Imprimo los datos obtenidos
c = 0
for registro in cantidad_registros_ordenados:
    print(f"\nEmpleado nro {c + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    c = c + 1

input("Presione Enter para ver los registros ordenados por salario...")
# Ordeno los registros por el campo 'NOMBRE'
mi_cursor.execute("SELECT * FROM EMPLEADOS ORDER BY SALARIO")
cantidad_registros_ordenados = mi_cursor.fetchall()    
# Imprimo los datos obtenidos
i = 0
for registro in cantidad_registros_ordenados:
    print(f"\nEmpleado nro {i + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    i = i + 1

mi_conexion.close()  # Cierro la conexión a la base de datos