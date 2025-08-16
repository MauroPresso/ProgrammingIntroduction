# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
conexion = sqlite3.connect('empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
cursor = conexion.cursor()

# Selecciono datos de la tabla 'CONTACTOS'
cursor.execute("SELECT * FROM EMPLEADOS")

# el metodo fetchall() devuelve la cantidad los registros (filas) de la consulta
cantidad_registros = cursor.fetchall()

# Imprimo los datos obtenidos
k = 0
for registro in cantidad_registros:
    print(f"\nEmpleado nro {k + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    k = k + 1
# TABLA ORDENADA
input("Presione Enter para ver los registros ordenados por puesto...")
# Ordeno los registros por el campo 'NOMBRE'
cursor.execute("SELECT * FROM EMPLEADOS ORDER BY PUESTO")
cantidad_registros_ordenados = cursor.fetchall()    
# Imprimo los datos obtenidos
c = 0
for registro in cantidad_registros_ordenados:
    print(f"\nEmpleado nro {c + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    c = c + 1

input("Presione Enter para ver los registros ordenados por salario...")
# Ordeno los registros por el campo 'NOMBRE'
cursor.execute("SELECT * FROM EMPLEADOS ORDER BY SALARIO")
cantidad_registros_ordenados = cursor.fetchall()    
# Imprimo los datos obtenidos
i = 0
for registro in cantidad_registros_ordenados:
    print(f"\nEmpleado nro {i + 1}.\n- ID: {registro[0]}\n- Nombre: {registro[1]}\n- Apellido: {registro[2]}\n- Puesto: {registro[3]}\n- Salario: {registro[4]}\n")
    i = i + 1

conexion.close()  # Cierro la conexión a la base de datos