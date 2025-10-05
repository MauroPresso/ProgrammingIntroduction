
from claseAlumnos import Alumnos
from claseDocente import Docentes
from claseCurso import Cursos
import os
os.system("cls")
print("SISTEMA EDUCATIVO 2024")

print("** CLASE ALUMNOS **")
print()
Alumno1=Alumnos(0,"Juan Perez","Cipolletti")
Alumno2=Alumnos(0,"Carlos García","Neuquén")
Alumno1.Agregar()
Alumno2.Modificar() 
print()
print("** CLASE DOCENTES** ")
print()
Docente1=Docentes(0,"Ing Perez",antiguedad=10)
Docente2=Docentes(1,"Ing Garcia",antiguedad=5)
Docente3=Docentes(2,"Ing Fernandez",antiguedad=7)

Docente1.Modificar()
Docente2.Agregar()
Docente3.Eliminar()
print()
print("** CLASE CURSOS **")
print()
Micurso1=Cursos(0,"Fortran","2 meses","presencial")
Micurso1.Agregar()
Micurso1.Eliminar()

