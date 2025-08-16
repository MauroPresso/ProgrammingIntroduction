# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
conexion = sqlite3.connect('empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
cursor = conexion.cursor()

# Inserto datos en la tabla 'EMPLEADOS'
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (1, 'Juan', 'Perez', 'Administrativo', 1234567)")
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (2, 'Pepe', 'Sanchez', 'Informatico', 1834960)")
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (3, 'Dardo', 'Rodriguez', 'Vendedor', 1224559)")
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (4, 'Elena', 'Fuseneco', 'Limpieza', 934567)")
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (5, 'Edgardo', 'Beltran', 'Mantenimiento', 934570)")
cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (6, 'Rosa', 'Juarez', 'Secretaria', 834567)")
# Para que los cambios se guarden en la base de datos
conexion.commit()

conexion.close()  # Cierro la conexión a la base de datos