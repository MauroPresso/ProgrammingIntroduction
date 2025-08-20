import os
os.system('cls')

# Importo la libreria sqlite3
import sqlite3

try:
    # Conecto a la base de datos (Seria como el ruta a la base de datos)
    mi_conexion = sqlite3.connect('TP1_IPP\\Situacion\\biblioteca.db')
    # Creo un cursor para ejecutar comandos SQL (Seria como el puntero a la base de datos)
    mi_cursor = mi_conexion.cursor()
    # Inserto datos en la tabla 'LIBROS'
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (1, 'Los amorios de un procer', 'Juan Perez', 'Novela historica', 1955)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (2, 'La viuda', 'Pepe Sanchez', 'Novela negra', 1933)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (3, 'La guerra de las galaxias', 'Dardo Rodriguez', 'Ciencia ficcion', 2003)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (4, 'Todo vale en la guerra y el amor', 'Elena Fuseneco', 'Novela romantica', 1973)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (5, 'La busqueda del tesoro', 'Edgardo Beltran', 'Aventura', 1984)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (6, 'El reino de Darthon', 'Rosa Juarez', 'Fantasia', 2011)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (7, 'El principio del fin', 'Miguel Faermann', 'Distopia', 2020)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (8, 'Verano sin ti', 'Guillermo Granados', 'Juvenil', 1999)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (9, 'Furia Blanca', 'Alberto Hernandez', 'Terror', 1967)")
    mi_cursor.execute("INSERT INTO LIBROS (ID, TITULO, AUTOR, GENERO, ANO) VALUES (10, 'Virgen a los 40', 'Maximo Sartori', 'Autoayuda', 2025)")
    # Para que los cambios se guarden en la base de datos
    mi_conexion.commit()
    mi_conexion.close()  # Cierro la conexion a la base de datos
except:
    print("¡ERROR: Problemas con la base de datos de la empresa!\n¡Comuniquese con el administrador!\n¡Sepa disculpar los inconvenientes!\n¡Muchas gracias!")