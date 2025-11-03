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
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from classEstudiante import Alumnos

"""
FUNCIONES
"""
""" 
 @brief Función que determina la categoría del libro según el valor seleccionado.
 @param valor (int) - Valor seleccionado en el botón de opción.
 @return categoría (str) - Categoría del libro correspondiente al valor.
"""
def determinar_nivel(valor):
    if valor == 1:
        return "Basico"
    elif valor == 2:
        return "Intermedio"
    else:
        return "Avanzado"

"""
 @brief Función que convierte la categoría del libro a su valor correspondiente.
 @param categoria (str) - Categoría del libro.
 @return valor (int) - Valor correspondiente al nivel.
"""
def nivel_a_valor(nivel):
    if nivel == "Basico":
        return 1
    elif nivel == "Intermedio":
        return 2
    else:
        return 3

"""
 @brief Función que transforma la preferencia de email a su valor correspondiente.
 @param none.
 @return SI o NO según corresponda.
"""

def preferencia_material_impreso_a_valor():
    # material impreso
    if material_impreso.get() == 1:
        preferencia_material_impreso = "SI"   
    elif material_impreso.get() == 0:
        preferencia_material_impreso = "NO"
    return preferencia_material_impreso

def preferencia_clases_grabadas_a_valor():
    # clases grabadas
    if clases_grabadas.get() == 1:
        preferencia_clases_grabadas = "SI"   
    elif clases_grabadas.get() == 0:
        preferencia_clases_grabadas = "NO"
    return preferencia_clases_grabadas

def preferencia_talleres_extra_a_valor():
    # talleres extra
    if talleres_extra.get() == 1:
        preferencia_talleres_extra = "SI"   
    elif talleres_extra.get() == 0:
        preferencia_talleres_extra = "NO"
    return preferencia_talleres_extra

"""
 @brief Función que convierte el número de servicios seleccionados a los valores de los checkbuttons
 @param val (str) - Valor del servicio.
 @return none
"""
def material_impreso_a_checkbutton(material_impreso_val):
    # Material Impreso
    if material_impreso_val == "NO":
        material_impreso.set(0)
    elif material_impreso_val == "SI":
        material_impreso.set(1)

def clases_grabadas_a_checkbutton(clases_grabadas_val):
    # clases grabadas
    if clases_grabadas_val == "NO":
        clases_grabadas.set(0)
    elif clases_grabadas_val == "SI":
        clases_grabadas.set(1)

def talleres_extra_a_checkbutton(talleres_extra_val):
    # talleres extra
    if talleres_extra_val == "NO":
        talleres_extra.set(0)
    elif talleres_extra_val == "SI":
        talleres_extra.set(1)


"""
 @brief Funcion que vacia los entrys.
 @param none
 @return none
"""
def limpiar_campos():
    # Entrys
    nombre.set("")
    idioma.set("")
    ingreso_fecha_inscripcion.set_date(date.today())
    # Radiobuttons
    nivel.set(0)
    # Checkbuttons
    opcion_material_impreso.set(0); opcion_clases_grabadas.set(0); opcion_talleres_extra.set(0)
    # Foco en el primer entry
    ingreso_nombre_alumno.focus()

"""
 @brief Funcion que administra los estados de los entrys y los botones de accion.
 @param estado (string)
 @return none
"""
def state_textbox_and_checkbuttons(estado):
    # Entrys
    ingreso_nombre_alumno.config(state=estado)
    ingreso_idioma_alumno.config(state=estado)
    ingreso_fecha_inscripcion.config(state=estado)
    # Radiobuttons
    nivel_conocimiento_basico.config(state=estado)
    nivel_conocimiento_intermedio.config(state=estado)
    nivel_conocimiento_avanzado.config(state=estado)
    # Checkbuttons
    opcion_material_impreso.config(state=estado)
    opcion_clases_grabadas.config(state=estado)
    opcion_talleres_extra.config(state=estado)

"""
 @brief Funcion que carga los registros en el visor de la app.
 @param none
 @return none
"""
def cargarEnVisorBD():
    boton_nuevo.config(state="normal")
    boton_modificar.config(state="normal")
    boton_eliminar.config(state="normal")
    vaciarElVisorBD()
    registros=Alumnos.ListaAlumnos()
    for r in registros:
        #              VINC.C/CAMPO0(ID) VALORES(OTROS CAMPOS)               
        visorBD.insert('', 0, text=r[0], values=(r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

"""
 @brief Funcion que borra los registros en el visor de la app.
 @param none
 @return none
"""  
def vaciarElVisorBD():

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
    state_textbox_and_checkbuttons("normal")
    # Botones de accion
    boton_nuevo.config(state="disabled")
    boton_modificar.config(state="disabled")
    boton_eliminar.config(state="disabled")
    boton_cancelar.config(state="normal")
    boton_guardar.config(state="normal")

"""
 @brief Función que maneja la cancelación del Alumnos.
 @param none
 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este Alumnos")
    # Entrys
    limpiar_campos()
    ingreso_nombre_alumno.focus() #nombre del entry
    # deshabilito Entrys
    state_textbox_and_checkbuttons("disabled")
    # Botones de accion
    boton_nuevo.config(state="normal")
    boton_modificar.config(state="normal")
    boton_eliminar.config(state="normal")
    boton_cancelar.config(state="disabled")
    boton_guardar.config(state="disabled")

""" 
 @brief Función que maneja el guardado del préstamo.
 @param none
 @return none
"""
def guardar():
    if nombre.get() == "" or idioma.get() == "" or ingreso_fecha_inscripcion.get_date() <= date.today() or nivel.get() == 0:
        if nombre.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif idioma.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el idioma del libro.")
        elif ingreso_fecha_inscripcion.get_date() <= date.today():
            messagebox.showerror("ERROR", "Por favor, ingresa la fecha de inscripción válida.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nivel de estudios.")
    else:
        global registroNuevo
        if messagebox.askquestion("CONFIRMAR GUARDADO", "¿Confirma que desea guardar la inscripción?") == "yes":
            if registroNuevo==True:
                miAlumnos = Alumnos(nombre=nombre.get(), idioma=idioma.get(), fecha=ingreso_fecha_inscripcion.get_date(), nivel=determinar_nivel(nivel.get()), material=preferencia_material_impreso_a_valor(), clases_grabadas=preferencia_clases_grabadas_a_valor(), talleres_extra=preferencia_talleres_extra_a_valor())
                miAlumnos.Agregar()
                messagebox.showinfo("AGREGAR Alumnos", "La inscripción ha sido agregado correctamente.")
            else:
                miAlumnos = Alumnos(id=visorBD.item(visorBD.selection())['text'], nombre=nombre.get(), idioma=idioma.get(), fecha=ingreso_fecha_inscripcion.get_date(), nivel=determinar_nivel(nivel.get()), material=preferencia_material_impreso_a_valor(), clases_grabadas=preferencia_clases_grabadas_a_valor(), talleres_extra=preferencia_talleres_extra_a_valor())
                miAlumnos.Modificar()
                messagebox.showinfo("MODIFICAR Alumnos", "La inscripción ha sido modificado correctamente.")
            # limpio los campos
            cargarEnVisorBD()
            limpiar_campos()
            state_textbox_and_checkbuttons("disabled")
            # Botones de accion
            boton_nuevo.config(state="normal")
            boton_modificar.config(state="normal")
            boton_eliminar.config(state="normal")
            boton_cancelar.config(state="disabled")
            boton_guardar.config(state="disabled")
        else:
            messagebox.showinfo("GUARDAR Alumnos", "La inscripción NO ha sido guardada.")

"""
 @brief Función que maneja la modificación del préstamo.
 @param none
 @return none
"""
def modificar():
    global registroNuevo
    registroNuevo=False
    try:
        limpiar_campos()
        state_textbox_and_checkbuttons("normal")
        # Cargo los valores en los entrys
        nombre.set(visorBD.item(visorBD.selection())['values'][0])
        idioma.set(visorBD.item(visorBD.selection())['values'][1])
        fecha.set((visorBD.item(visorBD.selection())['values'][2]))
        nivel.set(nivel_a_valor(visorBD.item(visorBD.selection())['values'][3]))
        material_impreso_a_checkbutton(visorBD.item(visorBD.selection())['values'][4])
        clases_grabadas_a_checkbutton(visorBD.item(visorBD.selection())['values'][5])
        talleres_extra_a_checkbutton(visorBD.item(visorBD.selection())['values'][6])
        # Botones de accion
        boton_guardar.config(state="normal")
        boton_cancelar.config(state="normal")
        boton_nuevo.config(state="disabled")
        boton_eliminar.config(state="disabled")
        boton_modificar.config(state="disabled")
    except:
        messagebox.showerror("ERROR", "Debe seleccionar un registro para modificar.")
        state_textbox_and_checkbuttons("disabled")
        boton_nuevo.config(state="normal")
        boton_modificar.config(state="normal")
        boton_eliminar.config(state="normal")
        boton_guardar.config(state="disabled")
        boton_cancelar.config(state="disabled")

"""
 @brief Función que maneja la eliminación del préstamo.
 @param none
 @return none
"""
def eliminar():
    try:
        miAlumno = Alumnos(id=int(visorBD.item(visorBD.selection())['text']))
        if messagebox.askquestion("CONFIRMAR ELIMINACIÓN", "¿Confirma que desea eliminar el préstamo?") == "yes":  
            miAlumno.Eliminar()
            limpiar_campos()
            state_textbox_and_checkbuttons("disabled")
            cargarEnVisorBD()
        else:
            messagebox.showinfo("ELIMINAR Alumnos", "El préstamo NO ha sido eliminado.")
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
raiz.title("**** Registro de alumnos del instituto de idiomas ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP_APP_SP_IPP\\SP5\\audio.ico')
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
subtitulo.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta del nombre completo
etiqueta_nombre_alumno = Label(marco, text="Nombre del alumno:")
etiqueta_nombre_alumno.grid(row=1, column=0, sticky="w", padx=10, pady=10)
etiqueta_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del Idioma que desea aprender
etiqueta_idioma_alumno = Label(marco, text="Idioma que desea aprender:")
etiqueta_idioma_alumno.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_idioma_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta de los meses de cursado
etiqueta_meses_cursado = Label(marco, text="Meses que deseas cursar:")
etiqueta_meses_cursado.grid(row=3, column=0, sticky="w", padx=10, pady=10)
etiqueta_meses_cursado.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"))
# Etiqueta del Nivel de conocimiento
etiqueta_nivel_conocimiento = Label(marco, text="Nivel de conocimiento:")
etiqueta_nivel_conocimiento.grid(row=0, column=2, sticky="w", padx=10, pady=10)
etiqueta_nivel_conocimiento.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta de la modalidad de cursada
etiqueta_modalidad_cursada = Label(marco, text="Modalidad de cursada:")
etiqueta_modalidad_cursada.grid(row=0, column=3, sticky="w", pady=10, padx=10)
etiqueta_modalidad_cursada.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic underline"))
# Etiqueta de las preferencias
etiqueta_preferencias = Label(marco, text="Seleccione las preferencias:")
etiqueta_preferencias.grid(row=0, column=4, sticky="w", pady=10, padx=10)
etiqueta_preferencias.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic underline"))

"""
ENTRYS
"""
# Variables de los Entrys
nombre = StringVar()
idioma = StringVar()
fecha = StringVar()
nivel = IntVar()

# Ingreso del nombre del alumno
ingreso_nombre_alumno = Entry(marco, textvariable=nombre)
ingreso_nombre_alumno.grid(row=1, column=1, sticky="w", pady=10, padx=10)
ingreso_nombre_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), state="disabled")
# Ingreso del Idioma que desea aprender
ingreso_idioma_alumno = Entry(marco, textvariable=idioma)
ingreso_idioma_alumno.grid(row=2, column=1, sticky="w", pady=10, padx=10)
ingreso_idioma_alumno.config(fg = "yellow", bg = "skyblue", font = ("Arial", 14, "bold italic"), state="disabled")
# Ingreso de la fecha de inscripcion
ingreso_fecha_inscripcion = DateEntry(marco, date_pattern='yyyy-mm-dd', textvariable=fecha)
ingreso_fecha_inscripcion.grid(row=3, column=1, sticky="w", pady=8)
ingreso_fecha_inscripcion.config(width = 30, state="disabled")
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
""" 
BOTONES DE ACCION
"""
# Boton de nuevo.
boton_nuevo = Button(marco, text="NUEVO", command=lambda:nuevo())
boton_nuevo.grid(row=5, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_nuevo.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"), state="disabled")
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
VISOR
"""
# Visor
visorBD=ttk.Treeview(marco, columns=('NombreDelLector', 'Idioma', 'FechaDeInscripcion', 'Nivel', 'MaterialImpreso', 'ClasesGrabadas', 'TalleresExtras'))
visorBD.grid(row=7, column=0, columnspan=3, sticky="nsew")
# Scrollbar
barraDespl=ttk.Scrollbar(marco, orient=VERTICAL, command=visorBD.yview)
barraDespl.grid(row=7, column=3, sticky="ns")
visorBD.configure(yscrollcommand=barraDespl.set)
# CONFIGURACION
# ID
visorBD.heading('#0', text="ID")
visorBD.column('#0', width=10)
# Nombre
visorBD.heading('#1', text="Nombre Del Estudiante")
visorBD.column('#1', width=50)
# Idioma
visorBD.heading('#2', text="Idioma")
visorBD.column('#2', width=50)
# Fecha De Inscripción
visorBD.heading('#3', text="Fecha De Inscripción")
visorBD.column('#3', width=50)
# Nivel de estudios
visorBD.heading('#4', text="Nivel de Conocimiento")
visorBD.column('#4', width=50)
# Material Impreso
visorBD.heading('#5', text="Material Impreso")
visorBD.column('#5', width=10)
# Clases Grabadas
visorBD.heading('#6', text="Clases Grabadas")
visorBD.column('#6', width=10)
# Talleres Extras
visorBD.heading('#7', text="Talleres Extras")
visorBD.column('#7', width=10)

# Cargar datos en el visor
cargarEnVisorBD()

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()