# @file APP_GUI.py
#
# @brief Módulo de interfaz gráfica de la aplicacion.
# @date 10/06/2025
# @author Mauro Presso
# @version 1.0
# @details
# Aplicación - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox
from classAlumnos import Alumnos

"""
FUNCIONES
"""
"""
 @brief Función que maneja la limpieza de los campos de entrada de texto.

 @param none

 @return none
"""
def nuevo():
    messagebox.showwarning("ATENCIÓN", "Está por ingresar una nueva inscripción")
    # Entrys
    nombre.set("")
    domicilio.set("")
    edad.set(0)
    dni.set(0)

""" 
 @brief Función que maneja la inscripción del alumno.
 @param none
 @return none
"""
def guardar():
    if nombre.get() == "" or domicilio.get() == "" or dni.get() == 0 or edad.get() == 0:
        if nombre.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif domicilio.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el domicilio que deseas aprender.")
        elif edad.get() == 0:
            messagebox.showerror("ERROR", "Por favor, ingresa tu edad.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa tu DNI.")
    else:
        miAlumno = Alumnos(nombre=nombre.get(), domicilio=domicilio.get(), dni=dni.get(), edad=edad.get())
        miAlumno.Agregar()

"""
 @brief Función que maneja la modificación de la inscripción.
 
 @param none
    
 @return none
"""
def modificar():
    if nombre.get() == "" and domicilio.get() == "" and dni.get() == 0 and edad.get() == 0:
        messagebox.showerror("ERROR", "No hay inscripción para modificar.")
    else:
        respuesta = messagebox.askquestion("MODIFICAR INSCRIPCION", "Confirmar que desea modificar la inscripción")
        if respuesta=="yes":
            messagebox.showinfo("MODIFICAR INSCRIPCION", "La inscripción ha sido modificada")
        else:
            miAlumno = Alumnos(nombre=nombre.get(), domicilio=domicilio.get(), dni=dni.get(), edad=edad.get())
            miAlumno.Modificar()

"""
 @brief Función que maneja la eliminación de la inscripción.

 @param none

 @return none
"""
def eliminar():

    if nombre.get() == "" and domicilio.get() == "" and dni.get() == 0 and edad.get() == 0:
        messagebox.showerror("ERROR", "No hay inscripción para eliminar.")
    else:
        respuesta = messagebox.askquestion("ELIMINAR INSCRIPCION", "Confirmar que desea eliminar la inscripción")
        if respuesta=="yes":
            messagebox.showinfo("ELIMINAR INSCRIPCION", "La inscripción ha sido eliminada")
        else:
            miAlumno = Alumnos(nombre=nombre.get(), domicilio=domicilio.get(), dni=dni.get(), edad=edad.get())
            miAlumno.Eliminar()

"""
 @brief Función que maneja la salida de la aplicación.

 @param none

 @return none
"""
def salida():
    respuesta = messagebox.askquestion("SALIDA DE LA APP", "Confirmar que sale de la apicacion")
    if respuesta=="yes":
        raiz.destroy() # cuando destroy lo vinculas a command no se pone parentesis. En este caso, si.
    else:
        messagebox.showinfo("SALIDA DE LA APP", "Aun sigues aqui, gracias por quedarte!")


"""
RAIZ
"""
raiz = Tk()
raiz.title("** SISTEMA EDUCATIVO - TU NOMBRE **")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP_APP_IPP\\Software.ico')
except Exception:
    pass
raiz.config(bg = "red") # bg: background (color de fondo).
raiz.config(cursor = "star") # cursor: es el iconito del mouse.

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20)
marco.pack(fill="none", expand=True)
marco.config(bg = "yellow", relief= "ridge") 

"""
ETIQUETAS
"""
# Subtitulo
subtitulo = Label(marco, text="** CARGA DE ALUMNOS **")
subtitulo.grid(row=0, column=1, columnspan=2, sticky="w", pady=10, padx=10)
subtitulo.config(fg = "yellow", bg = "skyblue", font = ("Arial", 18, "bold italic underline"), width=40)
# Etiqueta del nombre completo
etiqueta_nombre_alumno = Label(marco, text="Nombre del alumno:")
etiqueta_nombre_alumno.grid(row=1, column=0, sticky="w", padx=10, pady=10)
etiqueta_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del domicilio 
etiqueta_domicilio_alumno = Label(marco, text="Domicilio:")
etiqueta_domicilio_alumno.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_domicilio_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta de los edad de cursado
etiqueta_edad_alumno = Label(marco, text="Edad")
etiqueta_edad_alumno.grid(row=3, column=0, sticky="w", padx=10, pady=10)
etiqueta_edad_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del dni de conocimiento
etiqueta_dni_alumno = Label(marco, text="DNI:")
etiqueta_dni_alumno.grid(row=4, column=0, sticky="w", padx=10, pady=10)
etiqueta_dni_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic underline"))

"""
ENTRYS
"""
# Variables de los Entrys
nombre = StringVar()
domicilio = StringVar()
dni = IntVar()
edad = IntVar()
# Ingreso del nombre del alumno
ingreso_nombre_alumno = Entry(marco, textvariable=nombre)
ingreso_nombre_alumno.grid(row=1, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60)
# Ingreso del domicilio que desea aprender
ingreso_domicilio_alumno = Entry(marco, textvariable=domicilio)
ingreso_domicilio_alumno.grid(row=2, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_domicilio_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60)
# Ingreso de los edad que desea cursar
ingreso_edad_alumno = Entry(marco, textvariable=edad)
ingreso_edad_alumno.grid(row=3, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_edad_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60)
# Ingreso del dni del alumno
ingreso_dni_alumno = Entry(marco, textvariable=dni)
ingreso_dni_alumno.grid(row=4, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_dni_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60)

"""
BOTONES DE ACCION
"""
# Boton de inscribir.
boton_inscribir = Button(marco, text="NUEVO", command=lambda:nuevo())
boton_inscribir.grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_inscribir.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))
# Boton de guardar
boton_guardar = Button(marco, text="GUARDAR", command=lambda:guardar())
boton_guardar.grid(row=5, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_guardar.config(fg = "blue", bg = "white", width = 30, font = ("Verdana", 14, "italic"))
# Boton de modificar
boton_modificar = Button(marco, text="MODIFICAR", command=lambda:modificar())
boton_modificar.grid(row=6, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_modificar.config(fg = "orange", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de eliminar
boton_eliminar = Button(marco, text="ELIMINAR", command=lambda:eliminar())
boton_eliminar.grid(row=6, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_eliminar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de salir.
boton_salir = Button(marco, text="SALIR", command=lambda:salida())
boton_salir.grid(row=7, column=0, columnspan=3, pady=10, padx=10, sticky="w")
boton_salir.config(fg = "red", bg = "black", width = 90, font = ("Helvetica", 14, "italic"))


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()