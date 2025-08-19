import os
os.system('cls')

# Importo la librería sqlite3
import sqlite3

# Conecto a la base de datos (Seria como el ruta a la base de datos)
mi_conexion = sqlite3.connect('TP1_IPP\\Situacion3\\tienda.db')

# Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
mi_cursor = mi_conexion.cursor()

# Selecciono datos de la tabla 'PPRODUCTOS'
mi_cursor.execute("SELECT * FROM PRODUCTOS")

# Modifico datos en la tabla 'EMPLEADOS'
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 22000 WHERE NOMBRE = 'Pollo'")
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 16000 WHERE NOMBRE = 'Pan'")
mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 13000 WHERE NOMBRE = 'Leche'")
mi_cursor.execute("UPDATE PRODUCTOS SET STOCK = 65 WHERE CATEGORIA = 'Higiene personal'")
mi_cursor.execute("UPDATE PRODUCTOS SET STOCK = 73 WHERE CATEGORIA = 'Limpieza'")

# Para que los cambios se guarden en la base de datos
mi_conexion.commit()

mi_conexion.close()  # Cierro la conexión a la base de datos