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
from datetime import date, datetime, time
from tktimepicker import SpinTimePickerOld, constants as tkc
from classTurno import Turno

"""
FUNCIONES
"""

def _hora_time_desde_picker(picker) -> time:
    """Devuelve datetime.time leído del SpinTimePickerOld (HH:MM) en builds variadas."""
    # 1) Getters típicos
    try:
        h = int(picker.getHrs()); m = int(picker.getMins())
        return time(h, m)
    except Exception:
        pass

    # 2) Variables internas comunes
    for hh_attr, mm_attr in (('hoursVar', 'minutesVar'),
                             ('hourVar', 'minuteVar'),
                             ('hours', 'minutes'),
                             ('hour', 'minute')):
        try:
            h = int(getattr(picker, hh_attr).get())
            m = int(getattr(picker, mm_attr).get())
            return time(h, m)
        except Exception:
            continue

    # 3) Buscar spinboxes hijos (TSpinbox o Spinbox), recorriendo recursivamente
    def _spinboxes_rec(w):
        boxes = []
        for ch in w.winfo_children():
            cls = ch.winfo_class()
            if cls in ('TSpinbox', 'Spinbox'):
                boxes.append(ch)
            # seguir descendiendo (algunos builds anidan frames)
            boxes.extend(_spinboxes_rec(ch))
        return boxes

    try:
        spbs = _spinboxes_rec(picker)
        # A veces el orden es HH,MM; otras MM,HH. Intentamos parsear ambos.
        if len(spbs) >= 2:
            a = int(spbs[0].get())
            b = int(spbs[1].get())
            # Heurística: si a > 23 y b <= 23, intercambiamos
            if a > 23 and b <= 23:
                a, b = b, a
            # Clamp básico por si el control permite valores fuera de rango
            h = max(0, min(23, a))
            m = max(0, min(59, b))
            return time(h, m)
    except Exception:
        pass

    # 4) Si llegamos acá, no se pudo leer en tu build
    raise ValueError("No se pudo leer la hora del timePicker (build no soportado).")


def _hora_es_pasada_hoy(fecha_sel: date, hora_sel: time) -> bool:
    """True si la fecha es hoy y la hora es <= ahora."""
    ahora = datetime.now()
    return (fecha_sel == ahora.date()) and (hora_sel <= ahora.time())

def _resetear_timepicker():
    global ingreso_hora_turno
    # Intenta setters si existen…
    try:
        ingreso_hora_turno.setHrs(0); ingreso_hora_turno.setMins(0)
        return
    except Exception:
        pass
    ingreso_hora_turno.destroy()
    ingreso_hora_turno = SpinTimePickerOld(marco)
    ingreso_hora_turno.grid(row=4, column=1, sticky="w", padx=10, pady=10)
    ingreso_hora_turno.addAll(tkc.HOURS24)

def nuevo():
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    especialidad_medica.set(0)
    email.set(0); whatsapp.set(0); sms.set(0)
    _resetear_timepicker()
    ingreso_nombre_paciente.focus()

def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este turno")
    nombre_paciente.set("")
    motivo.set("")
    ingreso_fecha_turno.set_date(date.today())
    especialidad_medica.set(0)
    email.set(0); whatsapp.set(0); sms.set(0)
    _resetear_timepicker()
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

def guardar():
    fecha_sel = ingreso_fecha_turno.get_date()
    hora_sel = _hora_time_desde_picker(ingreso_hora_turno)      # -> datetime.time
    hora_iso = hora_sel.strftime("%H:%M:%S")                     # '23:15:00'
    if nombre_paciente.get() == "" or motivo.get() == "" or especialidad_medica.get() == 0:
        if nombre_paciente.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif motivo.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el motivo del turno.")
        else:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        return

    if fecha_sel < date.today():
        messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        return

    try:
        hora_sel = _hora_time_desde_picker(ingreso_hora_turno)  # datetime.time
    except Exception as e:
        messagebox.showerror("ERROR", str(e))
        return

    if _hora_es_pasada_hoy(fecha_sel, hora_sel):
        messagebox.showerror("ERROR", "La hora debe ser posterior a la actual.")
        return

    fecha_iso = fecha_sel.isoformat()             # "YYYY-MM-DD"
    hora_iso  = hora_sel.strftime("%H:%M:%S")     # "HH:MM:SS"

    miTurno = Turno(
        nombre=nombre_paciente.get(),
        motivo=motivo.get(),
        fecha=fecha_iso,
        hora=hora_iso,
        medico=determinar_especialidad_medica(especialidad_medica.get()),
        servicios=contar_preferencias()
    )
    miTurno.Agregar()


def modificar():
    sin_datos = (
        nombre_paciente.get() == "" and
        motivo.get() == "" and
        especialidad_medica.get() == 0
    )
    if sin_datos:
        messagebox.showerror("ERROR", "No hay turno para modificar.")
        return

    fecha_sel = ingreso_fecha_turno.get_date()
    if fecha_sel < date.today():
        messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        return

    try:
        hora_sel = _hora_time_desde_picker(ingreso_hora_turno)
    except Exception as e:
        messagebox.showerror("ERROR", str(e))
        return

    if _hora_es_pasada_hoy(fecha_sel, hora_sel):
        messagebox.showerror("ERROR", "La hora debe ser posterior a la actual.")
        return

    if messagebox.askquestion("MODIFICAR TURNO", "Confirmar que desea modificar el turno") == "yes":
        miTurno = Turno(
            nombre=nombre_paciente.get(),
            motivo=motivo.get(),
            fecha=fecha_sel.isoformat(),
            hora=hora_sel.strftime("%H:%M:%S"),
            medico=determinar_especialidad_medica(especialidad_medica.get()),
            servicios=contar_preferencias()
        )
        miTurno.Modificar()
        messagebox.showinfo("MODIFICAR TURNO", "El turno ha sido modificado")

def eliminar():
    sin_datos = (
        nombre_paciente.get() == "" and
        motivo.get() == "" and
        especialidad_medica.get() == 0
    )
    if sin_datos:
        messagebox.showerror("ERROR", "No hay turno para eliminar.")
        return

    if messagebox.askquestion("ELIMINAR TURNO", "Confirmar que desea eliminar el turno") == "yes":
        miTurno = Turno(
            nombre=nombre_paciente.get(),
            motivo=motivo.get(),
            fecha=ingreso_fecha_turno.get_date().isoformat(),
            hora=_hora_time_desde_picker(ingreso_hora_turno).strftime("%H:%M:%S"),
            medico=determinar_especialidad_medica(especialidad_medica.get()),
            servicios=contar_preferencias()
        )
        miTurno.Eliminar()
        messagebox.showinfo("ELIMINAR TURNO", "El turno ha sido eliminado")


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
# Etiqueta de la hora del turno
etiqueta_hora_turno = Label(marco, text="Hora del turno:")
etiqueta_hora_turno.grid(row=4, column=0, sticky="w", padx=10, pady=10)
etiqueta_hora_turno.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
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
ingreso_hora_turno = SpinTimePickerOld(marco)
ingreso_hora_turno.grid(row=4, column=1, sticky="w", padx=10, pady=10)
ingreso_hora_turno.addAll(tkc.HOURS24)  # arma HH y MM en formato 24h
_resetear_timepicker()

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