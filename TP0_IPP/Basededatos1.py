# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
conexion = sqlite3.connect('D:\\Mauro\\Facultad\\IFES\\Materias\\2doCuatri1erAnio\\IntroAlaProgramacion\\Practica\\TrabajoPractico1\\basededatos0.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
cursor = conexion.cursor()

# Inserto datos en la tabla 'CONTACTOS'
cursor.execute("INSERT INTO CONTACTOS (NOMBRE, TELEFONO) VALUES ('Juan Perez', 123456789)")
cursor.execute("INSERT INTO CONTACTOS (NOMBRE, TELEFONO) VALUES ('Maria Lopez', 987654321)")
cursor.execute("INSERT INTO CONTACTOS (NOMBRE, TELEFONO) VALUES ('Carlos Gomez', 456789123)")
cursor.execute("INSERT INTO CONTACTOS (NOMBRE, TELEFONO) VALUES ('Pepe Sanchez', 456789123)")

# Para que los cambios se guarden en la base de datos
conexion.commit()

conexion.close()  # Cierro la conexión a la base de datos