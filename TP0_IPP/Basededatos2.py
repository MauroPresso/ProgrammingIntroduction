# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
conexion = sqlite3.connect('D:\\Mauro\\Facultad\\IFES\\Materias\\2doCuatri1erAnio\\IntroAlaProgramacion\\Practica\\TrabajoPractico1\\basededatos0.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
cursor = conexion.cursor()

# Selecciono datos de la tabla 'CONTACTOS'
cursor.execute("SELECT * FROM CONTACTOS")

# el metodo fetchall() devuelve la cantidad los registros de la consulta
cantidad_registros = cursor.fetchall()

# Imprimo los datos obtenidos
for registro in cantidad_registros:
    print(f"Nombre: {registro[0]}, Telefono: {registro[1]}")

# TABLA ORDENADA
input("Presione Enter para ver los registros ordenados por nombre...")
# Ordeno los registros por el campo 'NOMBRE'
cursor.execute("SELECT * FROM CONTACTOS ORDER BY NOMBRE")
cantidad_registros_ordenados = cursor.fetchall()    
# Imprimo los datos obtenidos
for registro in cantidad_registros_ordenados:
    print(f"Nombre: {registro[0]}, Telefono: {registro[1]}")

input("Presione Enter para ver los registros ordenados por telefono...")
# Ordeno los registros por el campo 'NOMBRE'
cursor.execute("SELECT * FROM CONTACTOS ORDER BY TELEFONO")
cantidad_registros_ordenados = cursor.fetchall()    
# Imprimo los datos obtenidos
for registro in cantidad_registros_ordenados:
    print(f"Nombre: {registro[0]}, Telefono: {registro[1]}")

conexion.close()  # Cierro la conexión a la base de datos