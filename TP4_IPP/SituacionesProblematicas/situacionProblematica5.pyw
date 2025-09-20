# @file situacionProblematica5.pyw
#
# @brief Programa que permite registrar la inscripcion de un alumno en una instituto de idiomas.
# @date 09/22/2025
# @author Mauro Presso
# @version 3.0
# @details
# Situación Problemática Nº5 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox

"""
FUNCIONES
"""
""" 
 @brief Función que identifica la modalidad de cursada seleccionada por el alumno.
 @param none
 @return modalidad_cursada (str): Cadena con la modalidad de cursada seleccionada.
"""
def identificar_modalidad_cursada():
    if modalidad.get() == 1:
        return "Presencial"
    elif modalidad.get() == 2:
        return "Virtual"
    else:
        return "Mixta"

"""
 @brief Función que identifica el nivel de conocimiento seleccionado por el alumno.
 @param none
 @return nivel_conocimiento (str): Cadena con el nivel de conocimiento seleccionado.
"""
def identificar_nivel_conocimiento():
    if nivel.get() == 1:
        return "Basico"
    elif nivel.get() == 2:
        return "Intermedio"
    else:
        return "Avanzado"

"""
 @brief Función que lista las preferencias seleccionadas por el alumno.
 @param none
 @return preferencias_del_alumno (str): Cadena con las preferencias seleccionadas.
"""
def listar_preferencias():
    if material_impreso.get() == 0 and clases_grabadas.get() == 0 and talleres_extra.get() == 0:
        return "No seleccionaste ninguna preferencia."
    elif material_impreso.get() == 1 and clases_grabadas.get() == 1 and talleres_extra.get() == 1:
        return "Material impreso, Clases grabadas y Talleres extra."
    elif material_impreso.get() == 1 and clases_grabadas.get() == 1 and talleres_extra.get() == 0:
        return "Material impreso y Clases grabadas."
    elif material_impreso.get() == 1 and clases_grabadas.get() == 0 and talleres_extra.get() == 1:
        return "Material impreso y Talleres extra."
    elif material_impreso.get() == 0 and clases_grabadas.get() == 1 and talleres_extra.get() == 1:
        return "Clases grabadas y Talleres extra."
    elif material_impreso.get() == 1 and clases_grabadas.get() == 0 and talleres_extra.get() == 0:
        return "Material impreso."
    elif material_impreso.get() == 0 and clases_grabadas.get() == 1 and talleres_extra.get() == 0:
        return "Clases grabadas."   
    else:
        return "Talleres extra."

""" 
 @brief Función que maneja la inscripción del alumno.
 @param none
 @return none
"""
def inscribir():
    if nombre.get() == "" or idioma.get() == "" or nivel.get() == 0 or modalidad.get() == 0:
        if nombre.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif idioma.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el idioma que deseas aprender.")
        elif nivel.get() == 0:
            messagebox.showerror("ERROR", "Por favor, selecciona tu nivel de conocimiento.")
        else:
            #preferencias_del_alumno=listar_preferencias()
            messagebox.showerror("ERROR", "Por favor, selecciona la modalidad de cursada.")
    else:
        messagebox.showinfo("BIENVENIDO AL CURSO", f"Tu nombre: {nombre.get()}\n\nEl idioma que quieres aprender: {idioma.get()}\n\nTu nivel de conocimiento: {identificar_nivel_conocimiento()}\n\nModalidad de cursada: {identificar_modalidad_cursada()}\n\nTus preferencias: {listar_preferencias()}\n\nTe has inscrito correctamente. Bienvenido/a al curso!")

"""
 @brief Función que maneja la cancelación de la inscripción.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar esta inscripción")
    # Entrys
    nombre.set("")
    idioma.set("")
    # Botones de opción
    nivel.set(0)
    modalidad.set(0)
    # Casillas de verificación
    material_impreso.set(0)
    clases_grabadas.set(0)
    talleres_extra.set(0)

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
raiz.title("**** Registro de alumnos del instituto de idiomas ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\audio.ico')
except Exception:
    pass
raiz.config(bg = "red") # bg: background (color de fondo).
raiz.config(cursor = "star") # cursor: es el iconito del mouse.

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20)
marco.pack(fill="x", expand=True)
marco.config(bg = "yellow", relief= "ridge") 

"""
ETIQUETAS
"""
# Subtitulo
subtitulo = Label(marco, text="Datos para inscribirse:")
subtitulo.grid(row=0, column=0, columnspan=2, sticky="w", pady=10, padx=10)
subtitulo.config(fg = "yellow", bg = "blue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta del nombre completo
etiqueta_nombre_alumno = Label(marco, text="Nombre del alumno:")
etiqueta_nombre_alumno.grid(row=1, column=0, sticky="w", padx=10, pady=10)
etiqueta_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del Idioma que desea aprender
etiqueta_idioma_alumno = Label(marco, text="Idioma que desea aprender:")
etiqueta_idioma_alumno.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_idioma_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del Nivel de conocimiento
etiqueta_nivel_conocimiento = Label(marco, text="Nivel de conocimiento:")
etiqueta_nivel_conocimiento.grid(row=0, column=2, sticky="w", padx=10, pady=10)
etiqueta_nivel_conocimiento.config(fg = "yellow", bg = "blue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta de la modalidad de cursada
etiqueta_modalidad_cursada = Label(marco, text="Modalidad de cursada:")
etiqueta_modalidad_cursada.grid(row=0, column=3, sticky="w", pady=10, padx=10)
etiqueta_modalidad_cursada.config(fg = "yellow", bg = "blue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta de las preferencias
etiqueta_preferencias = Label(marco, text="Seleccione las preferencias:")
etiqueta_preferencias.grid(row=0, column=4, sticky="w", pady=10, padx=10)
etiqueta_preferencias.config(fg = "yellow", bg = "blue", font = ("Arial", 14, "bold italic underline"))

"""
ENTRYS
"""
# Variables de los Entrys
nombre = StringVar()
idioma = StringVar()
nivel = IntVar()
# Ingreso del nombre del alumno
ingreso_nombre_alumno = Entry(marco, textvariable=nombre)
ingreso_nombre_alumno.grid(row=1, column=1, sticky="w", pady=10, padx=10)
ingreso_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Ingreso del Idioma que desea aprender
ingreso_idioma_alumno = Entry(marco, textvariable=idioma)
ingreso_idioma_alumno.grid(row=2, column=1, sticky="w", pady=10, padx=10)
ingreso_idioma_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))

"""
BOTONES DE OPCION
"""
# Variable del boton de opcion de nivel de conocimiento
nivel = IntVar()
# Boton de opcion de nivel de conocimiento basico
nivel_conocimiento_basico = Radiobutton(marco, text="Basico", variable=nivel, value=1)
nivel_conocimiento_basico.grid(row=1, column=2, sticky="w", pady=10, padx=10)
nivel_conocimiento_basico.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Boton de opcion de nivel de conocimiento intermedio
nivel_conocimiento_intermedio = Radiobutton(marco, text="Intermedio", variable=nivel, value=2)
nivel_conocimiento_intermedio.grid(row=2, column=2, sticky="w", pady=10, padx=10)
nivel_conocimiento_intermedio.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Boton de opcion de nivel de conocimiento avanzado
nivel_conocimiento_avanzado = Radiobutton(marco, text="Avanzado", variable=nivel, value=3)
nivel_conocimiento_avanzado.grid(row=3, column=2, sticky="w", pady=10, padx=10)
nivel_conocimiento_avanzado.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))

# Variable del boton de opcion de modalidad de cursada
modalidad = IntVar()
# Boton de opcion de modalidad de cursada presencial
modalidad_cursada_presencial = Radiobutton(marco, text="Presencial", variable=modalidad, value=1)
modalidad_cursada_presencial.grid(row=1, column=3, sticky="w", pady=10, padx=10)
modalidad_cursada_presencial.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Boton de opcion de modalidad de cursada virtual
modalidad_cursada_virtual = Radiobutton(marco, text="Virtual", variable=modalidad, value=2)
modalidad_cursada_virtual.grid(row=2, column=3, sticky="w", pady=10, padx=10)
modalidad_cursada_virtual.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Boton de opcion de modalidad de cursada mixta
modalidad_cursada_mixta = Radiobutton(marco, text="Mixta", variable=modalidad, value=3)
modalidad_cursada_mixta.grid(row=3, column=3, sticky="w", pady=10, padx=10)
modalidad_cursada_mixta.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))

"""
CASILLAS DE VERIFICACION
"""
# Variables de las casillas de verificacion
material_impreso = IntVar()
clases_grabadas = IntVar()
talleres_extra = IntVar()
# Opcion de material impreso
opcion_material_impreso = Checkbutton(marco, text="Material impreso", variable=material_impreso)
opcion_material_impreso.grid(row=1, column=4, sticky="w", pady=10, padx=10)
opcion_material_impreso.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Opcion de clases grabadas
opcion_clases_grabadas = Checkbutton(marco, text="Clases grabadas", variable=clases_grabadas)
opcion_clases_grabadas.grid(row=2, column=4, sticky="w", pady=10, padx=10)
opcion_clases_grabadas.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))
# Opcion de talleres extra
opcion_talleres_extra = Checkbutton(marco, text="Talleres extra", variable=talleres_extra)
opcion_talleres_extra.grid(row=3, column=4, sticky="w", pady=10, padx=10)
opcion_talleres_extra.config(fg = "black", bg = "white", font = ("Arial", 14, "bold italic"))

"""
BOTONES DE ACCION
"""
# Boton de inscribir.
boton_inscribir = Button(marco, text="Inscribir", command=lambda:inscribir())
boton_inscribir.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="w")
boton_inscribir.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))
#Boton de cancelar inscripcion.
boton_cancelar = Button(marco, text="Cancelar", command=lambda:cancelar())
boton_cancelar.grid(row=5, column=0, columnspan=2, pady=10, padx=10, sticky="w")
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de salir.
boton_salir = Button(marco, text="Salir", command=lambda:salida())
boton_salir.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="w")
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()