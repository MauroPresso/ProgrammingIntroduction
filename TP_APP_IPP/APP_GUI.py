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
from tkinter import ttk
from classAlumnos import Alumnos

"""
FUNCIONES
"""
"""
 @brief Funcion que vacia los entrys.

 @param none

 @return none
"""
def limpiar_campos():
    nombre.set("")
    domicilio.set("")
    edad.set(0)
    dni.set(0)

"""
 @brief Funcion que administra los estados de los entrys y los botones de accion.

 @param estado (string)

 @return none
"""
def estado_textbox(estado):
    ingreso_nombre_alumno.config(state=estado)
    ingreso_domicilio_alumno.config(state=estado)
    ingreso_edad_alumno.config(state=estado)
    ingreso_dni_alumno.config(state=estado)

"""
 @brief Funcion que carga los registros en el visor de la app.
 @param none
 @return none
"""
def cargarEnVisorBD():
    boton_modificar.config(state="normal")
    boton_eliminar.config(state="normal")
    vaciarElVisorBD()
    registros=Alumnos.ListaAlumnos()
    for r in registros:
        #              VINC.C/CAMPO0(ID) VALORES(OTROS CAMPOS)               
        visorBD.insert('', 0, text=r[0], values=(r[1], r[2], r[3], r[4]))

"""
 @brief Funcion que borra los registros en el visor de la app.
 @param none
 @return none
"""  
def vaciarElVisorBD():
    boton_modificar.config(state="normal")
    boton_eliminar.config(state="normal")
    registros=visorBD.get_children()
    for r in registros:
        visorBD.delete(r)
        

"""
 @brief Función que maneja la limpieza de los campos de entrada de texto.

 @param none

 @return none
"""
def nuevo():
    global registroNuevo
    registroNuevo=True
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    # Entrys
    limpiar_campos()
    ingreso_nombre_alumno.focus() #nombre del entry
    # deshabilito Entrys
    estado_textbox("normal")
    # deshabilito Buttons
    boton_nuevo.config(state="disabled")
    boton_cancelar.config(state="normal")
    boton_guardar.config(state="normal")

"""
 @brief Función que maneja la cancelacion.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar el ingreso de un nuevo registro")
    # Entrys
    limpiar_campos()
    ingreso_nombre_alumno.focus() #nombre del entry
    # deshabilito Entrys
    estado_textbox("disabled")
    # deshabilito Buttons
    boton_nuevo.config(state="normal")
    boton_cancelar.config(state="disabled")
    boton_guardar.config(state="disabled")  

""" 
 @brief Función que maneja la inscripción del alumno.
 @param none
 @return none
"""
def guardar():
    # valido que los campos no esten vacios
    if nombre.get() == "" or domicilio.get() == "" or dni.get() == 0 or edad.get() == 0:
        if nombre.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif domicilio.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el domicilio.")
        elif edad.get() == 0:
            messagebox.showerror("ERROR", "Por favor, ingresa tu edad.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa tu DNI.")
    else:
        global registroNuevo
        if registroNuevo==True:
            miAlumno = Alumnos(nombre=nombre.get(), domicilio=domicilio.get(), dni=dni.get(), edad=edad.get())
            miAlumno.Agregar()
            messagebox.showinfo("AGREGADO","Nuevo registro ingresado")
        else:
            miAlumno = Alumnos(id=int(visorBD.item(visorBD.selection())['text']), nombre=nombre.get(), domicilio=domicilio.get(), dni=dni.get(), edad=edad.get())
            miAlumno.Modificar()
            messagebox.showinfo("MODIFICADO","Registro modificado")
        # limpio los campos
        cargarEnVisorBD()
        limpiar_campos()
        estado_textbox("disabled")
        # deshabilito Buttons
        boton_nuevo.config(state="normal")
        boton_cancelar.config(state="disabled")
        boton_guardar.config(state="disabled")

"""
 @brief Función que maneja la modificación de la inscripción.
 
 @param none
    
 @return none
"""
def modificar():
    global registroNuevo
    registroNuevo=False
    try:
        limpiar_campos()
        estado_textbox("normal")
        boton_guardar.config(state="normal")
        boton_nuevo.config(state="disabled")
        boton_cancelar.config(state="normal")

        nombre.set(visorBD.item(visorBD.selection())['values'][0])
        domicilio.set(visorBD.item(visorBD.selection())['values'][1])
        dni.set(visorBD.item(visorBD.selection())['values'][2])
        edad.set(visorBD.item(visorBD.selection())['values'][3])
    except:
        messagebox.showerror("ERROR", "Debe seleccionar un registro para modificar.")
        estado_textbox("disabled")
        boton_guardar.config(state="disabled")
        boton_nuevo.config(state="normal")
        boton_cancelar.config(state="disabled")

"""
 @brief Función que maneja la eliminación de la inscripción.

 @param none

 @return none
"""
def eliminar():
    try:
        miAlumno = Alumnos(id=int(visorBD.item(visorBD.selection())['text']))
        miAlumno.Eliminar()
        limpiar_campos()
        estado_textbox("disabled")
        # deshabilito Buttons
        boton_nuevo.config(state="normal")
        boton_cancelar.config(state="disabled")
        boton_guardar.config(state="disabled")
        cargarEnVisorBD()
    except:
        messagebox.showerror("ERROR", "Debe seleccionar un registro para eliminar.")


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
# Icono de la app
raiz.iconbitmap('TP_APP_IPP\\Software.ico')
raiz.config(bg = "orange") # bg: background (color de fondo).
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
ingreso_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60, state="disabled") #state="disabled" para que no se pueda escribir en el entry
# Ingreso del domicilio que desea aprender
ingreso_domicilio_alumno = Entry(marco, textvariable=domicilio)
ingreso_domicilio_alumno.grid(row=2, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_domicilio_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60, state="disabled") #state="disabled" para que no se pueda escribir en el entry
# Ingreso de los edad que desea cursar
ingreso_edad_alumno = Entry(marco, textvariable=edad)
ingreso_edad_alumno.grid(row=3, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_edad_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60, state="disabled") #state="disabled" para que no se pueda escribir en el entry
# Ingreso del dni del alumno
ingreso_dni_alumno = Entry(marco, textvariable=dni)
ingreso_dni_alumno.grid(row=4, column=1, columnspan=2, sticky="w", pady=10, padx=10)
ingreso_dni_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), width=60, state="disabled") #state="disabled" para que no se pueda escribir en el entry

"""
BOTONES DE ACCION
"""
# Boton de nuevo.
boton_nuevo = Button(marco, text="NUEVO", command=lambda:nuevo())
boton_nuevo.grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_nuevo.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"), state="normal")
# Boton de guardar
boton_guardar = Button(marco, text="GUARDAR", command=lambda:guardar())
boton_guardar.grid(row=5, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_guardar.config(fg = "blue", bg = "white", width = 30, font = ("Verdana", 14, "italic"), state="disabled")
# Boton de modificar
boton_modificar = Button(marco, text="MODIFICAR", command=lambda:modificar())
boton_modificar.grid(row=6, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_modificar.config(fg = "orange", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"), state="disabled")
# Boton de eliminar
boton_eliminar = Button(marco, text="ELIMINAR", command=lambda:eliminar())
boton_eliminar.grid(row=6, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_eliminar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"), state="disabled")
# Boton de cancelar
boton_cancelar = Button(marco, text="CANCELAR", command=lambda:cancelar())
boton_cancelar.grid(row=5, column=2, columnspan=1, pady=10, padx=10, sticky="w")
boton_cancelar.config(fg = "purple", bg = "white", width = 30, font = ("Helvetica", 14, "italic"), state="disabled")
# Boton de salir.
boton_salir = Button(marco, text="SALIR", command=lambda:salida())
boton_salir.grid(row=8, column=0, columnspan=3, pady=10, padx=10, sticky="w")
boton_salir.config(fg = "red", bg = "black", width = 90, font = ("Helvetica", 14, "italic"), state="normal")

"""
IMPORTANTE: CREAR PRIMERO LOS WIDGETS Y LUEGO LLAMAR A LAS FUNCIONES QUE LOS UTILIZAN.
"""

"""
VISOR
"""
# Visor
visorBD=ttk.Treeview(marco, columns=('nombre', 'domicilio', 'dni', 'edad'))
cant_campos=4
visorBD.grid(row=7, column=0, columnspan=cant_campos, sticky="nsew")
# Scrollbar
barraDespl=ttk.Scrollbar(marco, orient=VERTICAL, command=visorBD.yview)
barraDespl.grid(row=(cant_campos+3), column=cant_campos, sticky="ns")
visorBD.configure(yscrollcommand=barraDespl.set)
# CONFIGURACION
# ID
visorBD.heading('#0', text="ID")
visorBD.column('#0', width=30)
# Nombre
visorBD.heading('#1', text="Nombre")
visorBD.column('#1', width=100)
# Domicilio
visorBD.heading('#2', text="Domicilio")
visorBD.column('#2', width=100)
# DNI
visorBD.heading('#3', text="DNI")
visorBD.column('#3', width=100)
# Edad
visorBD.heading('#4', text="Edad")
visorBD.column('#4', width=100)
# Cargar datos en el visor
cargarEnVisorBD()

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()