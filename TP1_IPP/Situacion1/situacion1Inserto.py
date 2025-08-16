# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion1\\empresa.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Inserto datos en la tabla 'EMPLEADOS'
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (1, 'Juan', 'Perez', 'Administrativo', 1234567)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (2, 'Pepe', 'Sanchez', 'Informatico', 1834960)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (3, 'Dardo', 'Rodriguez', 'Vendedor', 1224559)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (4, 'Elena', 'Fuseneco', 'Limpieza', 934567)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (5, 'Edgardo', 'Beltran', 'Mantenimiento', 934570)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (6, 'Rosa', 'Juarez', 'Secretaria', 834567)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (7, 'Miguel', 'Faermann', 'Supervisor', 984567)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (8, 'Guillermo', 'Granados', 'Contratista', 854567)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (9, 'Alberto', 'Hernandez', 'Logística', 884579)")
mi_cursor.execute("INSERT INTO EMPLEADOS (ID, NOMBRE, APELLIDO, PUESTO, SALARIO) VALUES (10, 'Maximo', 'Sartori', 'Instructor', 734560)")
# Para que los cambios se guarden en la base de datos
mi_conexion.commit()

mi_conexion.close()  # Cierro la conexión a la base de datos