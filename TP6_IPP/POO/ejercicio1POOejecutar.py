import os
os.system("cls")

#From el archivo clasePersona importo a Persona
from ejercicio1POO import ALumno

# instanciacion
alumno1 = ALumno(1, "Pedro", "Calle Falsa 123", 31, 12345678)
alumno2 = ALumno(2, "Ana", "Avenida Siempre Viva 742", 28, 87654321)
alumno3 = ALumno(3, "Luis", "Boulevard de los Sueños Rotos 456", 35, 11223344)

# Ejecución de método agregar
input("\nPresione Enter para agregar los alumnos...")
alumno1.Agregar()
alumno2.Agregar()
alumno3.Agregar()

# Ejecución de método modificar
input("\nPresione Enter para modificar los alumnos...")
alumno1.Modificar()
alumno2.Modificar()
alumno3.Modificar()

# Ejecución de método eliminar
input("\nPresione Enter para eliminar los alumnos...")
alumno1.Eliminar()
alumno2.Eliminar()
alumno3.Eliminar()