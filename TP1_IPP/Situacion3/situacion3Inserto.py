# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion3\\tienda.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Inserto datos en la tabla 'PRODUCTOS'
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (1, 'Huevos', 'Alimentacion', '9999', 123)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (2, 'Azucar', 'Alimentacion', '800', 183)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (3, 'Pollo', 'Alimentacion', '20000', 122)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (4, 'Pan', 'Alimentacion', '14000', 93)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (5, 'Leche', 'Alimentacion', '11000', 94)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (6, 'Arroz', 'Alimentacion', '5000', 83)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (7, 'Porotos', 'Alimentacion', '3500', 98)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (8, 'Zapatillas', 'Vestimenta', '60000', 85)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (9, 'Detergente', 'Limpieza', '23000', 88)")
mi_cursor.execute("INSERT INTO PRODUCTOS (ID, NOMBRE, CATEGORIA, PRECIO, STOCK) VALUES (10, 'Jabon', 'Higiene personal', '6000', 73)")
# Para que los cambios se guarden en la base de datos
mi_conexion.commit()

mi_conexion.close()  # Cierro la conexión a la base de datos