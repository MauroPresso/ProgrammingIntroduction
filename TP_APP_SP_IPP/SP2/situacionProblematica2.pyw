# @file situacionProblematica2.pyw
#
# @brief Programa que permite ingresar los datos de un paciente de una clinica medica.
# @date 09/22/2025
# @author Mauro Presso
# @version 3.0
# @details
# Situación Problemática Nº2 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date
from classTurno import Turno

"""
FUNCIONES
"""

"""
FUNCIONES
"""

""" 
 @brief Función que determina la categoría del libro según el valor seleccionado.

 @param valor (int) - Valor seleccionado en el botón de opción.

 @return categoría (str) - Categoría del libro correspondiente al valor.
"""
def determinar_especialidad_medica(valor):
    if valor == 1:
        return "General"
    elif valor == 2:
        return "Especialista"
    else:
        return "Cirujano"

"""
 @brief Función que cuenta la cantidad de preferencias seleccionadas.

 @param none

 @return contador_preferencias (int) - Cantidad de preferencias seleccionadas.
"""
def contar_preferencias():
    contador_preferencias = 0
    if email.get() != 0 or whatsapp.get() != 0 or sms.get() != 0:
        if email.get() == 1:
            contador_preferencias += 1
        if whatsapp.get() == 1:
            contador_preferencias += 1
        if sms.get() == 1:
            contador_preferencias += 1
    return contador_preferencias

"""
 @brief Función que maneja la limpieza de los campos de entrada de texto.

 @param none

 @return none
"""
def nuevo():
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    # Entrys
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    # Botones de opción
    especialidad_medica.set(0)
    # Casillas de verificación
    email.set(0)
    whatsapp.set(0)
    sms.set(0)
    ingreso_nombre_paciente.focus() #nombre del entry

"""
 @brief Función que maneja la cancelación del prestamo.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este prestamo")
    # Entrys
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    # Botones de opción
    especialidad_medica.set(0)
    # Casillas de verificación
    email.set(0)
    whatsapp.set(0)
    sms.set(0)
    ingreso_nombre_paciente.focus() #nombre del entry

""" 
 @brief Función que maneja la inscripción del alumno.
 @param none
 @return none
"""
def guardar():
    if nombre_paciente.get() == "" or motivo.get() == "" or ingreso_fecha_turno.get_date() <= date.today() or ingreso_hora_turno.get() == "" or especialidad_medica.get() == 0:
        if nombre_paciente.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif motivo.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el motivo del turno.")
        elif ingreso_fecha_turno.get_date() <= date.today():
            messagebox.showerror("ERROR", "Por favor, ingresa la fecha del turno válida.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa la categoría del turno.")
    else:
        miTurno = Turno(nombre=nombre_paciente.get(), motivo=motivo.get(), fecha=ingreso_fecha_turno.get_date(), hora=ingreso_hora_turno.get(), medico=especialidad_medica.get(), servicios=contar_preferencias())
        miTurno.Agregar()

"""
 @brief Función que maneja la modificación de la inscripción.
 
 @param none
    
 @return none
"""
def modificar():
    if nombre_paciente.get() == "" and motivo.get() == "" and ingreso_fecha_turno.get_date() == date.today() and ingreso_hora_turno.get() == "" and especialidad_medica.get() == 0:
        messagebox.showerror("ERROR", "No hay turno para modificar.")
    else:
        respuesta = messagebox.askquestion("MODIFICAR TURNO", "Confirmar que desea modificar el turno")
        if respuesta=="yes":
            messagebox.showinfo("MODIFICAR TURNO", "El turno ha sido modificado")
            miTurno = Turno(nombre=nombre_paciente.get(), motivo=motivo.get(), fecha=ingreso_fecha_turno.get_date(), hora=ingreso_hora_turno.get(), medico=especialidad_medica.get(), servicios=contar_preferencias())
            miTurno.Modificar()

"""
 @brief Función que maneja la eliminación de la inscripción.

 @param none

 @return none
"""
def eliminar():

    if nombre_paciente.get() == "" and motivo.get() == "" and ingreso_fecha_turno.get_date() == 0 and especialidad_medica.get() == "":
        messagebox.showerror("ERROR", "No hay turno para eliminar.")
    else:
        respuesta = messagebox.askquestion("ELIMINAR TURNO", "Confirmar que desea eliminar el turno")
        if respuesta=="yes":
            messagebox.showinfo("ELIMINAR TURNO", "El turno ha sido eliminado")
            miTurno = Turno(nombre=nombre_paciente.get(), motivo=motivo.get(), fecha=ingreso_fecha_turno.get_date(), hora=ingreso_hora_turno.get(), medico=especialidad_medica.get(), servicios=contar_preferencias())
            miTurno.Eliminar()


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
raiz.title("**** Registro de datos del turno del paciente ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP_APP_SP_IPP\\SP2\\HEART.ICO')
except Exception:
    pass
raiz.config(bg = "skyblue") 
raiz.config(cursor = "cross")

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20)
marco.pack(fill="none", expand=True)
marco.config(bg = "white", relief= "sunken") 

"""
ETIQUETAS
"""
# Subtitulo de la app
etiqueta_subtitulo = Label(marco, text = "*** DATOS DEL TURNO DEL PACIENTE ***")
etiqueta_subtitulo.grid(row=0,column=0,sticky="w",padx=10,pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_subtitulo.config(fg = "yellow", bg = "black", width = 40, font = ("Rockell", 14, "italic"))
# Etiqueta del nombre completo
etiqueta_nombre_paciente = Label(marco, text="Nombre del paciente:")
etiqueta_nombre_paciente.grid(row=1, column=0, sticky="w", padx=10, pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_paciente.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del motivo del turno
etiqueta_motivo_turno = Label(marco, text="Motivo del turno:")
etiqueta_motivo_turno.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_motivo_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la fecha del turno
etiqueta_fecha_turno = Label(marco, text="Fecha del turno:")
etiqueta_fecha_turno.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_fecha_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la hora del turno
etiqueta_hora_turno = Label(marco, text="Hora del turno:")
etiqueta_hora_turno.grid(row=3, column=0, sticky="w", padx=10, pady=10)
etiqueta_hora_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del boton de opcion
etiqueta_especialidad_medica = Label(marco, text = "*** HORARIO DEL TURNO ***")
etiqueta_especialidad_medica.grid(row=0,column=2,sticky="w",padx=10,pady=10)
etiqueta_especialidad_medica.config(fg = "yellow", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
# Etiqueta de la casilla de verificacion
etiqueta_preferencias_recordatorio = Label(marco, text = "*** RECORDATORIO ***")
etiqueta_preferencias_recordatorio.grid(row=0,column=3,sticky="w",padx=10,pady=10)
etiqueta_preferencias_recordatorio.config(fg = "yellow", bg = "black", width = 30, font = ("Rockell", 14, "italic"))


"""
INGRESOS
"""
# Declaro el tipo de dato de los Entry (IntVar para enteros y StringVar para texto).
nombre_paciente=StringVar()
motivo=StringVar()
fecha_turno=StringVar()
hora_turno=StringVar()
# Ingreso del nombre paciente
ingreso_nombre_paciente = Entry(marco, textvariable=nombre_paciente)
ingreso_nombre_paciente.grid(row=1, column=1, sticky="w", padx=10,pady=10)
ingreso_nombre_paciente.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del motivo del turno
ingreso_motivo_paciente = Entry(marco, textvariable=motivo)
ingreso_motivo_paciente.grid(row=2, column=1, sticky="w", padx=10, pady=10)
ingreso_motivo_paciente.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del año de la fecha del turno
ingreso_fecha_turno = DateEntry(marco, date_pattern='dd/mm/yyyy', textvariable=fecha_turno)
ingreso_fecha_turno.grid(row=4, column=1, sticky="w", padx=10 ,pady=10)
ingreso_fecha_turno.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso de la hora del turno
ingreso_hora_turno = Entry(marco, textvariable=hora_turno)
ingreso_hora_turno.grid(row=5, column=1, sticky="w", padx=10 ,pady=10)
ingreso_hora_turno.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
especialidad_medica=IntVar()
# Opcion de primario completo
medico_general=Radiobutton(marco, text="Turno MAÑANA", variable=especialidad_medica, value=1)
medico_general.grid(row=1, column=2, sticky="w", padx=10, pady=10)
medico_general.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de secundario completo
medico_especialista=Radiobutton(marco, text="Turno TARDE", variable=especialidad_medica, value=2)
medico_especialista.grid(row=2, column=2, sticky="w", padx=10, pady=10)
medico_especialista.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de terciario completo
medico_cirujano=Radiobutton(marco, text="Turno NOCHE", variable=especialidad_medica, value=3)
medico_cirujano.grid(row=3, column=2, sticky="w", padx=10, pady=10)
medico_cirujano.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
CASILLAS DE VERIFICACION
"""
# Son TRES porque son INDEPENDIENTES
email=IntVar()
whatsapp=IntVar()
sms=IntVar()
# EMAIL
check_email = Checkbutton(marco, text="e-mail", variable=email, onvalue=1, offvalue=0)
check_email.grid(row=1,column=3,sticky="w",padx=10,pady=10)
check_email.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# WHATSAPP
check_whatsapp = Checkbutton(marco, text="WhatsApp", variable=whatsapp, onvalue=1, offvalue=0)
check_whatsapp.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_whatsapp.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# ENCUESTA
check_sms = Checkbutton(marco, text="SMS", variable=sms, onvalue=1, offvalue=0)
check_sms.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_sms.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
BOTONES DE ACCION
"""
# Boton de nuevo.
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
# Boton de cancelar
boton_cancelar = Button(marco, text="CANCELAR", command=lambda:cancelar())
boton_cancelar.grid(row=5, column=2, columnspan=1, pady=10, padx=10, sticky="w")
boton_cancelar.config(fg = "purple", bg = "white", width = 30, font = ("Helvetica", 14, "italic"))
# Boton de salir.
boton_salir = Button(marco, text="SALIR", command=lambda:salida())
boton_salir.grid(row=7, column=0, columnspan=3, pady=10, padx=10, sticky="w")
boton_salir.config(fg = "red", bg = "black", width = 90, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()