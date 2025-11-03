# @file situacionProblematica1.pyw
#
# @brief Programa que permite ingresar los datos de un alumno de una academia.
# @date 09/22/2025
# @author Mauro Presso
# @version 3.0
# @details
# Situación Problemática Nº1 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from classAlumno import Alumnos

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
        return "Primario"
    elif valor == 2:
        return "Secundario"
    else:
        return "Universitario"

"""
 @brief Función que convierte la categoría del libro a su valor correspondiente.
 @param categoria (str) - Categoría del libro.
 @return valor (int) - Valor correspondiente al nivel.
"""
def nivel_a_valor(nivel):
    if nivel == "Primario":
        return 1
    elif nivel == "Secundario":
        return 2
    else:
        return 3

"""
 @brief Función que transforma la preferencia de email a su valor correspondiente.
 @param none.
 @return SI o NO según corresponda.
"""

def preferencia_email_a_valor():
    # Email
    if email.get() == 1:
        preferencia_email = "SI"   
    elif email.get() == 0:
        preferencia_email = "NO"
    return preferencia_email

def preferencia_whatsapp_a_valor():
    # Whatsapp
    if whatsapp.get() == 1:
        preferencia_whatsapp = "SI"   
    elif whatsapp.get() == 0:
        preferencia_whatsapp = "NO"
    return preferencia_whatsapp

def preferencia_encuesta_a_valor():
    # Encuesta
    if encuesta.get() == 1:
        preferencia_encuesta = "SI"   
    elif encuesta.get() == 0:
        preferencia_encuesta = "NO"
    return preferencia_encuesta

"""
 @brief Función que convierte el número de servicios seleccionados a los valores de los checkbuttons
 @param val (str) - Valor del servicio.
 @return none
"""
def email_a_checkbutton(email_val):
    # Email
    if email_val == "NO":
        email.set(0)
    elif email_val == "SI":
        email.set(1)

def whatsapp_a_checkbutton(whatsapp_val):
    # Whatsapp
    if whatsapp_val == "NO":
        whatsapp.set(0)
    elif whatsapp_val == "SI":
        whatsapp.set(1)

def encuesta_a_checkbutton(encuesta_val):
    # Encuesta
    if encuesta_val == "NO":
        encuesta.set(0)
    elif encuesta_val == "SI":
        encuesta.set(1)


"""
 @brief Funcion que vacia los entrys.
 @param none
 @return none
"""
def limpiar_campos():
    # Entrys
    nombre_completo.set("")
    idioma.set("")
    ingreso_fecha_inscripcion.set_date(date.today())
    # Radiobuttons
    nivel_estudios.set(0)
    # Checkbuttons
    email.set(0); whatsapp.set(0); encuesta.set(0)
    # Foco en el primer entry
    ingreso_nombre_completo.focus()

"""
 @brief Funcion que administra los estados de los entrys y los botones de accion.
 @param estado (string)
 @return none
"""
def state_textbox_and_checkbuttons(estado):
    # Entrys
    ingreso_nombre_completo.config(state=estado)
    ingreso_idioma.config(state=estado)
    ingreso_fecha_inscripcion.config(state=estado)
    # Radiobuttons
    primario.config(state=estado)
    secundario.config(state=estado)
    universitario.config(state=estado)
    # Checkbuttons
    check_email.config(state=estado)
    check_whatsapp.config(state=estado)
    check_encuesta.config(state=estado)

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
    ingreso_nombre_completo.focus() #nombre del entry
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
    ingreso_nombre_completo.focus() #nombre del entry
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
    if nombre_completo.get() == "" or idioma.get() == "" or ingreso_fecha_inscripcion.get_date() <= date.today() or nivel_estudios.get() == 0:
        if nombre_completo.get() == "":
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
                miAlumnos = Alumnos(nombre=nombre_completo.get(), idioma=idioma.get(), fecha=ingreso_fecha_inscripcion.get_date(), nivel=determinar_nivel(nivel_estudios.get()), email=preferencia_email_a_valor(), whatsapp=preferencia_whatsapp_a_valor(), encuesta=preferencia_encuesta_a_valor())
                miAlumnos.Agregar()
                messagebox.showinfo("AGREGAR Alumnos", "La inscripción ha sido agregado correctamente.")
            else:
                miAlumnos = Alumnos(id=visorBD.item(visorBD.selection())['text'], nombre=nombre_completo.get(), idioma=idioma.get(), fecha=ingreso_fecha_inscripcion.get_date(), nivel=determinar_nivel(nivel_estudios.get()), email=preferencia_email_a_valor(), whatsapp=preferencia_whatsapp_a_valor(), encuesta=preferencia_encuesta_a_valor())
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
        nombre_completo.set(visorBD.item(visorBD.selection())['values'][0])
        idioma.set(visorBD.item(visorBD.selection())['values'][1])
        fecha.set((visorBD.item(visorBD.selection())['values'][2]))
        nivel_estudios.set(nivel_a_valor(visorBD.item(visorBD.selection())['values'][3]))
        email_a_checkbutton(visorBD.item(visorBD.selection())['values'][4])
        whatsapp_a_checkbutton(visorBD.item(visorBD.selection())['values'][5])
        encuesta_a_checkbutton(visorBD.item(visorBD.selection())['values'][6])
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
raiz.title("**** Registro de nuevos alumnos de la academia ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP_APP_SP_IPP\\SP1\\icono2.ico')
except Exception:
    pass
raiz.config(bg = "purple")
raiz.config(cursor = "pencil") 

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20)
marco.pack(fill="none", expand=True)
marco.config(bg = "grey", relief= "groove") 

"""
ETIQUETAS
"""
# Subtitulo de la app
etiqueta_subtitulo = Label(marco, text = "REGISTRO DE NUEVOS ALUMNOS")
etiqueta_subtitulo.grid(row=0,column=0,sticky="w",padx=10,pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_subtitulo.config(fg = "white", bg = "black", width = 40, font = ("Rockell", 14, "italic"))
# Etiqueta del nombre completo
etiqueta_nombre_completo = Label(marco, text="Nombre completo:")
etiqueta_nombre_completo.grid(row=1, column=0, sticky="w", padx=20, pady=30) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_completo.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del numero de documento
etiqueta_idioma = Label(marco, text="Idioma:")
etiqueta_idioma.grid(row=2, column=0, sticky="w", padx=20, pady=30) 
etiqueta_idioma.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del correo electronico
etiqueta_fecha_inscripcion = Label(marco, text="Fecha de inscripción:")
etiqueta_fecha_inscripcion.grid(row=3, column=0, sticky="w", padx=20, pady=30)
etiqueta_fecha_inscripcion.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del boton de opcion
etiqueta_nivel_estudios = Label(marco, text = "NIVEL DE ESTUDIOS:")
etiqueta_nivel_estudios.grid(row=0,column=2,sticky="w",padx=10,pady=10)
etiqueta_nivel_estudios.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
# Etiqueta de la casilla de verificacion
etiqueta_preferencias_contacto = Label(marco, text = "PREFERENCIAS DE CONTACTO:")
etiqueta_preferencias_contacto.grid(row=0,column=3,sticky="w",padx=10,pady=10)
etiqueta_preferencias_contacto.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
"""
INGRESOS
"""
# Declaro el tipo de dato de los Entry (IntVar para enteros y StringVar para texto).
nombre_completo=StringVar()
idioma=StringVar()
fecha = StringVar()       
# Ingreso del nombre completo
ingreso_nombre_completo = Entry(marco, textvariable=nombre_completo)
ingreso_nombre_completo.grid(row=1, column=1, sticky="w", padx=10, pady=10)
ingreso_nombre_completo.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"), state="disabled")
# Ingreso del idioma
ingreso_idioma = Entry(marco, textvariable=idioma)
ingreso_idioma.grid(row=2, column=1, sticky="w", padx=10, pady=10)
ingreso_idioma.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"), state="disabled")
# Ingreso de la fecha de inscripcion
ingreso_fecha_inscripcion = DateEntry(marco, date_pattern='yyyy-mm-dd', textvariable=fecha)
ingreso_fecha_inscripcion.grid(row=3, column=1, sticky="w", pady=8)
ingreso_fecha_inscripcion.config(width = 30, state="disabled")

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
nivel_estudios=IntVar()
# Opcion de primario
primario=Radiobutton(marco, text="Primario", variable=nivel_estudios, value=1)
primario.grid(row=1, column=2, sticky="w", padx=10, pady=10)
primario.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# Opcion de secundario
secundario=Radiobutton(marco, text="Secundario", variable=nivel_estudios, value=2)
secundario.grid(row=2, column=2, sticky="w", padx=10, pady=10)
secundario.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# Opcion de terciario completo
universitario=Radiobutton(marco, text="Universitario", variable=nivel_estudios, value=3)
universitario.grid(row=3, column=2, sticky="w", padx=10, pady=10)
universitario.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")

"""
CASILLAS DE VERIFICACION
"""
# Son TRES porque son INDEPENDIENTES
email=IntVar()
whatsapp=IntVar()
encuesta=IntVar()
# EMAIL
check_email = Checkbutton(marco, text="e-mail", variable=email, onvalue=1, offvalue=0)
check_email.grid(row=1,column=3,sticky="w",padx=10,pady=10)
check_email.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# WHATSAPP
check_whatsapp = Checkbutton(marco, text="WhatsApp", variable=whatsapp, onvalue=1, offvalue=0)
check_whatsapp.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_whatsapp.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# ENCUESTA
check_encuesta = Checkbutton(marco, text="Encuesta", variable=encuesta, onvalue=1, offvalue=0)
check_encuesta.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_encuesta.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")

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
visorBD=ttk.Treeview(marco, columns=('NombreDelLector', 'Idioma', 'FechaDeInscripcion', 'Nivel', 'Email', 'Whatsapp', 'Encuesta'))
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
visorBD.heading('#4', text="Nivel de Estudios")
visorBD.column('#4', width=50)
# Email
visorBD.heading('#5', text="Email")
visorBD.column('#5', width=10)
# Whatsapp
visorBD.heading('#6', text="Whatsapp")
visorBD.column('#6', width=10)
# Encuesta
visorBD.heading('#7', text="Encuesta")
visorBD.column('#7', width=10)

# Cargar datos en el visor
cargarEnVisorBD()

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga.
raiz.mainloop()