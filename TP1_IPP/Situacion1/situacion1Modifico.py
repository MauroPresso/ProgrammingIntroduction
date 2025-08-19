import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion1\\empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Selecciono datos de la tabla 'EMPLEADOS'
mi_cursor.execute("SELECT * FROM EMPLEADOS")

# Modifico datos en la tabla 'EMPLEADOS'
mi_cursor.execute("UPDATE EMPLEADOS SET SALARIO = 906357 WHERE APELLIDO = 'Sartori'")
mi_cursor.execute("UPDATE EMPLEADOS SET NOMBRE = 'Jose' WHERE NOMBRE = 'Pepe'")
mi_cursor.execute("UPDATE EMPLEADOS SET PUESTO = 'Transportista' WHERE PUESTO = 'Logística'")
mi_cursor.execute("UPDATE EMPLEADOS SET SALARIO = 2105987 WHERE PUESTO = 'Informatico'")
mi_cursor.execute("UPDATE EMPLEADOS SET APELLIDO = 'Faerman' WHERE APELLIDO = 'Faermann'")

# Para que los cambios se guarden en la base de datos
mi_conexion.commit()

mi_conexion.close()  # Cierro la conexión a la base de datos