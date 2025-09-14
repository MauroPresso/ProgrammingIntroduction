# @file situacionProblematica2.pyw
#
# @brief Programa que permite ingresar los datos de un paciente de una clinica medica.
# @date 09/22/2025
# @author Mauro Presso
# @version 2.0
# @details
# Situación Problemática Nº2 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox

"""
FUNCIONES
"""
"""
 @brief Función que maneja el registro de la inscripción.

 @param none

 @return none
"""
def registrar(): 
    # Entrys
    if nombre_paciente.get() == "" or ano_nacimiento.get() == 0 or especialidad_medica.get() == "" or edad.get() == 0:
        # Nombre completo
        if nombre_paciente.get() == "": # En el entry del nombre completo no hay nada
            messagebox.showerror("ERROR","No ingresaste tu nombre")
        # Numero de documento
        elif ano_nacimiento.get() == 0: # En el entry del numero de documento no hay nada
            messagebox.showerror("ERROR","No ingresaste tu numero de documento")
        # Correo electronico
        elif especialidad_medica.get() == "": # En el entry del correo electronico no hay nada
            messagebox.showerror("ERROR","No ingresaste tu correo electronico")  
        # Edad
        else: # En el entry de la edad no hay nada
            messagebox.showerror("ERROR","No ingresaste tu edad")
    # Botones de opción
    elif horario_turno.get() != 1 and horario_turno.get() != 2 and horario_turno.get() != 3:
        messagebox.showerror("ERROR","No seleccionaste tu nivel de estudios")
    else:
        messagebox.showinfo("SU TURNO HA SIDO REGISTRADO CON ÉXITO", f"Alumno: {nombre_paciente.get()}\nAño de nacimiento: {ano_nacimiento.get()}\nEdad: {edad.get()}\nEspecialidad médica solicitada: {especialidad_medica.get()}\nHorario del turno: {horario_turno.get()}")


"""
 @brief Función que maneja la cancelación del turno.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar esta inscripción")
    # Entrys
    nombre_paciente.set("")
    ano_nacimiento.set(0)
    especialidad_medica.set("")
    edad.set(0)
    # Botones de opción
    horario_turno.set(0)
    # Casillas de verificación
    email.set(0)
    whatsapp.set(0)
    sms.set(0)

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
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\HEART.ICO')
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
# Etiqueta del edad del paciente
etiqueta_edad_paciente = Label(marco, text="Edad del paciente:")
etiqueta_edad_paciente.grid(row=2, column=0, sticky="w", padx=10, pady=10)
etiqueta_edad_paciente.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la especialidad medica solicitada
etiqueta_especialidad_medica = Label(marco, text="Especialidad medica solicitada:")
etiqueta_especialidad_medica.grid(row=3, column=0, sticky="w", padx=10, pady=10)
etiqueta_especialidad_medica.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del año de nacimiento del paciente
etiqueta_ano_nacimiento = Label(marco, text="Año de nacimiento del paciente:")
etiqueta_ano_nacimiento.grid(row=4, column=0, sticky="w", padx=10, pady=10)
etiqueta_ano_nacimiento.config(fg = "orange", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del boton de opcion
etiqueta_horario_turno = Label(marco, text = "*** HORARIO DEL TURNO ***")
etiqueta_horario_turno.grid(row=0,column=2,sticky="w",padx=10,pady=10)
etiqueta_horario_turno.config(fg = "yellow", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
# Etiqueta de la casilla de verificacion
etiqueta_preferencias_recordatorio = Label(marco, text = "*** RECORDATORIO ***")
etiqueta_preferencias_recordatorio.grid(row=0,column=3,sticky="w",padx=10,pady=10)
etiqueta_preferencias_recordatorio.config(fg = "yellow", bg = "black", width = 30, font = ("Rockell", 14, "italic"))


"""
INGRESOS
"""
# Declaro el tipo de dato de los Entry (IntVar para enteros y StringVar para texto).
nombre_paciente=StringVar()
ano_nacimiento=IntVar()
especialidad_medica=StringVar()
edad=IntVar()
# Ingreso del nombre paciente
ingreso_nombre_paciente = Entry(marco, textvariable=nombre_paciente)
ingreso_nombre_paciente.grid(row=1, column=1, sticky="w", padx=10,pady=10)
ingreso_nombre_paciente.config(fg = "white", bg = "blue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del edad del paciente
ingreso_edad_paciente = Entry(marco, textvariable=edad)
ingreso_edad_paciente.grid(row=2, column=1, sticky="w", padx=10, pady=10)
ingreso_edad_paciente.config(fg = "white", bg = "blue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso de la especialidad medica solicitada
ingreso_especialidad_medica = Entry(marco, textvariable=especialidad_medica)
ingreso_especialidad_medica.grid(row=3, column=1, sticky="w", padx=10, pady=10)
ingreso_especialidad_medica.config(fg = "white", bg = "blue", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del año de nacimiento del paciente
ingreso_ano_nacimiento = Entry(marco, textvariable=ano_nacimiento)
ingreso_ano_nacimiento.grid(row=4, column=1, sticky="w", padx=10 ,pady=10)
ingreso_ano_nacimiento.config(fg = "white", bg = "blue", width = 30, font = ("Arial", 14, "italic"))

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
horario_turno=IntVar()
# Opcion de primario completo
turno_manana=Radiobutton(marco, text="Turno MAÑANA", variable=horario_turno, value=1)
turno_manana.grid(row=1, column=2, sticky="w", padx=10, pady=10)
turno_manana.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de secundario completo
turno_tarde=Radiobutton(marco, text="Turno TARDE", variable=horario_turno, value=2)
turno_tarde.grid(row=2, column=2, sticky="w", padx=10, pady=10)
turno_tarde.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de terciario completo
turno_noche=Radiobutton(marco, text="Turno NOCHE", variable=horario_turno, value=3)
turno_noche.grid(row=3, column=2, sticky="w", padx=10, pady=10)
turno_noche.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

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
# Boton de confirmar turno.
boton_confirmar = Button(marco, text="Confirmar turno")
boton_confirmar.grid(row=5, column=0, columnspan=2, padx=10,pady=10)
boton_confirmar.config(fg = "green", bg = "skyblue", width = 30, font = ("Calibri", 14, "italic"))
# Boton de cancelar turno.
boton_cancelar = Button(marco, text="Cancelar")
boton_cancelar.grid(row=6, column=0, columnspan=2, padx=10,pady=10)
boton_cancelar.config(fg = "red", bg = "skyblue", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de salir.
boton_salir = Button(marco, text="Salir", command=lambda:salida())
boton_salir.grid(row=7, column=0, columnspan=2, padx=10,pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()