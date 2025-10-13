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
 @brief Función que convierte la hora y minutos en formato SQL.
 @param hora (int) - Hora del turno.
 @param minutos (int) - Minutos del turno.
 @return hora_sql (str) - Hora en formato SQL (HH:MM:SS).
"""
def time_sql(hora, minutos):
    if 0 <= hora <= 23 and 0 <= minutos <= 59:
        hora_sql = f"{hora:02}:{minutos:02}:00"
        return hora_sql
    else:
        raise ValueError("Hora o minutos fuera de rango")

""" 
 @brief Función que inicializa un nuevo registro, limpiando todos los campos de entrada.
 @param none
 @return none
 """
def nuevo():
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    hora_turno.set(0); minuto_turno.set(0)
    especialidad_medica.set(0)
    email.set(0); whatsapp.set(0); sms.set(0)
    ingreso_nombre_paciente.focus()

""" 
 @brief Función que cancela el registro actual, limpiando todos los campos de entrada.
 @param none
 @return none
 """
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este turno")
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    hora_turno.set(0); minuto_turno.set(0)
    especialidad_medica.set(0)
    email.set(0); whatsapp.set(0); sms.set(0)
    ingreso_nombre_paciente.focus()

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
 @brief Función que guarda el registro del turno del paciente.
 @param none
 @return none
"""
def guardar():
    condicion_hora = (hora_turno.get() < 0 or hora_turno.get() > 23)
    condicion_minuto = (minuto_turno.get() < 0 or minuto_turno.get() > 59)
    condicion_fecha = ((ingreso_fecha_turno.get_date()) <= date.today())
    condicion_paciente = (nombre_paciente.get() == "")
    condicion_motivo = (motivo.get() == "")
    condicion_especialidad = (especialidad_medica.get() == 0)
    if condicion_paciente or condicion_motivo or condicion_especialidad or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_paciente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_motivo:
            messagebox.showerror("ERROR", "Por favor, ingresa el motivo del turno.")
        elif condicion_especialidad:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("GUARDAR TURNO", "Confirmar que desea guardar el turno") == "yes":
            miTurno = Turno(
                nombre=nombre_paciente.get(),
                motivo=motivo.get(),
                fecha=ingreso_fecha_turno.get_date(),
                horario=time_sql(hora_turno.get(), minuto_turno.get()),
                medico=determinar_especialidad_medica(especialidad_medica.get()),
                recordatorios=contar_preferencias()
            )
            miTurno.Agregar()
            messagebox.showinfo("GUARDAR TURNO", "El turno ha sido guardado")
        else:
            messagebox.showinfo("GUARDAR TURNO", "El turno NO ha sido guardado")

""" 
 @brief Función que modifica el registro del turno del paciente.
 @param none
 @return none
"""
def modificar():
    condicion_hora = (hora_turno.get() < 0 or hora_turno.get() > 23)
    condicion_minuto = (minuto_turno.get() < 0 or minuto_turno.get() > 59)
    condicion_fecha = ((ingreso_fecha_turno.get_date()) <= date.today())
    condicion_paciente = (nombre_paciente.get() == "")
    condicion_motivo = (motivo.get() == "")
    condicion_especialidad = (especialidad_medica.get() == 0)
    if condicion_paciente or condicion_motivo or condicion_especialidad or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_paciente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_motivo:
            messagebox.showerror("ERROR", "Por favor, ingresa el motivo del turno.")
        elif condicion_especialidad:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("MODIFICAR TURNO", "Confirmar que desea modificar el turno") == "yes":
            miTurno = Turno(
            nombre=nombre_paciente.get(),
            motivo=motivo.get(),
            fecha=ingreso_fecha_turno.get_date(),
            horario=time_sql(hora_turno.get(), minuto_turno.get()),
            medico=determinar_especialidad_medica(especialidad_medica.get()),
            recordatorios=contar_preferencias()
            )
            miTurno.Modificar()
        else:
            messagebox.showinfo("MODIFICAR TURNO", "El turno NO ha sido modificado")

""" 
 @brief Función que elimina el registro del turno del paciente.
 @param none
 @return none
"""
def eliminar():
    condicion_hora = (hora_turno.get() < 0 or hora_turno.get() > 23)
    condicion_minuto = (minuto_turno.get() < 0 or minuto_turno.get() > 59)
    condicion_fecha = ((ingreso_fecha_turno.get_date()) <= date.today())
    condicion_paciente = (nombre_paciente.get() == "")
    condicion_motivo = (motivo.get() == "")
    condicion_especialidad = (especialidad_medica.get() == 0)
    if condicion_paciente or condicion_motivo or condicion_especialidad or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_paciente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_motivo:
            messagebox.showerror("ERROR", "Por favor, ingresa el motivo del turno.")
        elif condicion_especialidad:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("ELIMINAR TURNO", "Confirmar que desea eliminar el turno") == "yes":
            miTurno = Turno(
                nombre=nombre_paciente.get(),
                motivo=motivo.get(),
                fecha=ingreso_fecha_turno.get_date(),
                horario=time_sql(hora_turno.get(), minuto_turno.get()),
                medico=determinar_especialidad_medica(especialidad_medica.get()),
                recordatorios=contar_preferencias()
            )
            miTurno.Eliminar()
        else:
            messagebox.showinfo("ELIMINAR TURNO", "El turno NO ha sido eliminado")

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
marco.config(bg = "blue", relief= "sunken") 

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
etiqueta_fecha_turno.grid(row=3, column=0, sticky="w", padx=10, pady=10)
etiqueta_fecha_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la horario del turno
etiqueta_hora_turno = Label(marco, text="Horario del turno:")
etiqueta_hora_turno.grid(row=6, column=0, sticky="w", padx=10, pady=10)
etiqueta_hora_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Separador entre hora
etiqueta_separador_hora_minuto = Label(marco, text="Horas:")
etiqueta_separador_hora_minuto.grid(row=5, column=1, sticky="w", padx=0, pady=10)
etiqueta_separador_hora_minuto.config(fg = "yellow", bg = "black", width = 15, font = ("Rockell", 14, "italic"))
# Separador entre minuto
etiqueta_separador_minuto = Label(marco, text="Minutos:")
etiqueta_separador_minuto.grid(row=5, column=1, sticky="e", padx=0, pady=10)
etiqueta_separador_minuto.config(fg = "yellow", bg = "black", width = 15, font = ("Rockell", 14, "italic"))
# Etiqueta del boton de opcion
etiqueta_especialidad_medica = Label(marco, text = "*** ESPECIALIDAD MEDICA ***")
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
hora_turno=IntVar()
minuto_turno=IntVar()
# Ingreso del nombre paciente
ingreso_nombre_paciente = Entry(marco, textvariable=nombre_paciente)
ingreso_nombre_paciente.grid(row=1, column=1, sticky="w", padx=10,pady=10)
ingreso_nombre_paciente.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del motivo del turno
ingreso_motivo_paciente = Entry(marco, textvariable=motivo)
ingreso_motivo_paciente.grid(row=2, column=1, sticky="w", padx=10, pady=10)
ingreso_motivo_paciente.config(fg = "white", bg = "skyblue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del año de la fecha del turno
ingreso_fecha_turno = DateEntry(marco, date_pattern='yyyy/mm/dd', textvariable=fecha_turno)
ingreso_fecha_turno.grid(row=3, column=1, sticky="w", padx=10 ,pady=10)
ingreso_fecha_turno.config(width = 30)
# Ingreso de la hora del turno (timePicker)
ingreso_hora_turno = Entry(marco, textvariable=hora_turno)
ingreso_hora_turno.grid(row=6, column=1, sticky="w", padx=10, pady=10)
ingreso_hora_turno.config(fg = "white", bg = "skyblue", font = ("Arial", 14, "italic"), width=15)
# Ingreso de los minutos del turno (timePicker)
ingreso_minuto_turno = Entry(marco, textvariable=minuto_turno)
ingreso_minuto_turno.grid(row=6, column=1, sticky="e", padx=10, pady=10)
ingreso_minuto_turno.config(fg = "white", bg = "skyblue", font = ("Arial", 14, "italic"), width=15)

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
especialidad_medica=IntVar()
# Opcion de primario completo
medico_general=Radiobutton(marco, text="Medico General", variable=especialidad_medica, value=1)
medico_general.grid(row=1, column=2, sticky="w", padx=10, pady=10)
medico_general.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de secundario completo
medico_especialista=Radiobutton(marco, text="Medico Especialista", variable=especialidad_medica, value=2)
medico_especialista.grid(row=2, column=2, sticky="w", padx=10, pady=10)
medico_especialista.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de terciario completo
medico_cirujano=Radiobutton(marco, text="Medico Cirujano", variable=especialidad_medica, value=3)
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
boton_nuevo = Button(marco, text="NUEVO", command=lambda:nuevo())
boton_nuevo.grid(row=7, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_nuevo.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))
# Boton de guardar
boton_guardar = Button(marco, text="GUARDAR", command=lambda:guardar())
boton_guardar.grid(row=7, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_guardar.config(fg = "blue", bg = "white", width = 30, font = ("Verdana", 14, "italic"))
# Boton de modificar
boton_modificar = Button(marco, text="MODIFICAR", command=lambda:modificar())
boton_modificar.grid(row=8, column=0, columnspan=1, pady=10, padx=10, sticky="w")
boton_modificar.config(fg = "brown", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de eliminar
boton_eliminar = Button(marco, text="ELIMINAR", command=lambda:eliminar())
boton_eliminar.grid(row=8, column=1, columnspan=1, pady=10, padx=10, sticky="w")
boton_eliminar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de cancelar
boton_cancelar = Button(marco, text="CANCELAR", command=lambda:cancelar())
boton_cancelar.grid(row=7, column=2, columnspan=1, pady=10, padx=10, sticky="w")
boton_cancelar.config(fg = "purple", bg = "white", width = 30, font = ("Helvetica", 14, "italic"))
# Boton de salir.
boton_salir = Button(marco, text="SALIR", command=lambda:salida())
boton_salir.grid(row=9, column=0, columnspan=3, pady=10, padx=10, sticky="w")
boton_salir.config(fg = "red", bg = "black", width = 90, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()