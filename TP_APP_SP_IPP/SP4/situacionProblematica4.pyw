# @file situacionProblematica4.pyw
#
# @brief Programa que permite ingresar los datos de un usuario de una tienda online.
# @date 09/22/2025
# @author Mauro Presso
# @version 3.0
# @details
# Situación Problemática Nº4 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox

"""
 @brief Función que determina el costo segun el tipo de cuenta seleccionado.
 @param tipo_cuenta (int) - Valor del tipo de cuenta seleccionado.
 @return costo (float) - Costo mensual de la cuenta.
"""
def calcular_costo(tipo_cuenta):
    if tipo_cuenta == 1:
        costo.set(100.0)
    elif tipo_cuenta == 2:
        costo.set(200.0)
    else:
        costo.set(300.0)

"""
 @brief Función que determina el tipo de cuenta seleccionado.
 @param tipo_cuenta (int) - Valor del tipo de cuenta seleccionado.
 @return tipo_de_cuenta (str) - Descripción del tipo de cuenta.
"""
def determinar_tipo_de_cuenta(tipo_cuenta):
    if tipo_cuenta == 1:
        return "Basica"
    elif tipo_cuenta == 2:
        return "Premium"
    else:
        return "Administrador"



"""
 @brief Función que cuenta la cantidad de preferencias seleccionadas.

 @param none

 @return contador_preferencias (int) - Cantidad de preferencias seleccionadas.
"""
def contar_preferencias():
    contador_preferencias = 0
    if ofertas.get() != 0 or sms.get() != 0 or resumen.get() != 0:
        if ofertas.get() == 1:
            contador_preferencias += 1
        if sms.get() == 1:
            contador_preferencias += 1
        if resumen.get() == 1:
            contador_preferencias += 1
    return contador_preferencias

"""
 @brief Función que maneja el ingreso del registro.
 @param none
 @return none
"""
def ingresar_registro(): 
    # Entrys
    if nombre.get() == "" or usuario.get() == "" or correo.get() == "" or edad.get() < 18:
        
        if nombre.get() == "": 
            messagebox.showerror("ERROR","No ingresaste tu nombre")
        elif usuario.get() == "": 
            messagebox.showerror("ERROR","No ingresaste tu usuario")
        elif correo.get() == "": 
            messagebox.showerror("ERROR","No ingresaste tu correo electronico")
        else: # edad.get() < 18
            messagebox.showerror("ERROR","Debes ser mayor de edad para registrarte")
    # Botones de opción
    elif cuenta.get() != 1 and cuenta.get() != 2 and cuenta.get() != 3:
        messagebox.showerror("ERROR","No seleccionaste un tipo de cuenta")
    else:
        cantidad_preferencias=contar_preferencias()
        tipo_de_cuenta=determinar_tipo_de_cuenta(cuenta.get())
        messagebox.showinfo("SU TURNO FUE REGISTRADO CON ÉXITO", f"Nombre del lector: {nombre.get()}\nNombre de usuario: {usuario.get()}\nCorreo electronico: {correo.get()}\nTipo de cuenta: {tipo_de_cuenta}\nServicios adicionales seleccionados: {cantidad_preferencias}/3")

"""
 @brief Función que maneja la cancelación del ingreso.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar el registro de usuario")
    # Entrys
    nombre.set("")
    usuario.set("")
    correo.set("")
    edad.set(0)
    costo.set(0.0)
    # Botones de opción
    cuenta.set(0)
    # Casillas de verificación
    ofertas.set(0)
    sms.set(0)
    resumen.set(0)

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
raiz.title("**** Registro de usuarios de la tienda ONLINE ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
# Icono
try:
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\Hello.ico')
except Exception:
    pass
raiz.config(bg = "blue") # bg: background (color de fondo).
raiz.config(cursor = "target") # cursor: es el iconito del mouse.

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20) # padx y pady: son los espacios internos del frame.
marco.pack(fill="x", expand=True)
marco.config(bg = "green", relief= "raised")

"""
ETIQUETAS
"""
# Subtitulo de la app
etiqueta_subtitulo = Label(marco, text = "*** DATOS DEL USUARIO ***")
etiqueta_subtitulo.grid(row=0,column=0,sticky="w",padx=10,pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_subtitulo.config(fg = "yellow", bg = "brown", width = 40, font = ("Rockell", 14, "italic"))
# Etiqueta de los botones de opcion
etiqueta_botones_opcion = Label(marco, text="Seleccione el tipo de cuenta:")
etiqueta_botones_opcion.grid(row=0, column=2, sticky="w", pady=10, padx=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_botones_opcion.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de las casillas de verificacion
etiqueta_casillas_verificacion = Label(marco, text="Seleccione las preferencias de contacto:")
etiqueta_casillas_verificacion.grid(row=0, column=3, sticky="w", pady=10, padx=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_casillas_verificacion.config(fg = "yellow", bg = "brown", width = 35, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del nombre completo
etiqueta_nombre_completo = Label(marco, text="Nombre completo:")
etiqueta_nombre_completo.grid(row=1, column=0, sticky="w", pady=10, padx=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_completo.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del nombre de usuario
etiqueta_nombre_usuario = Label(marco, text="Nombre de usuario:")
etiqueta_nombre_usuario.grid(row=2, column=0, sticky="w", pady=10, padx=8)
etiqueta_nombre_usuario.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del correo electronico
etiqueta_correo_electronico = Label(marco, text="Correo electrónico:")
etiqueta_correo_electronico.grid(row=3, column=0, sticky="w", pady=10, padx=8)
etiqueta_correo_electronico.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la edad
etiqueta_edad = Label(marco, text="Edad:")
etiqueta_edad.grid(row=4, column=0, sticky="w", pady=10, padx=8)
etiqueta_edad.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
ENTRYS
"""
# Variables para los Entrys
nombre = StringVar()
usuario = StringVar()
correo = StringVar()
edad = IntVar()
costo = DoubleVar()
# Ingreso del nombre completo
ingreso_nombre_completo = Entry(marco, textvariable=nombre)
ingreso_nombre_completo.grid(row=1, column=1, sticky="w", padx=8, pady=10)
ingreso_nombre_completo.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del nombre de usuario
ingreso_nombre_usuario = Entry(marco, textvariable=usuario)
ingreso_nombre_usuario.grid(row=2, column=1, sticky="w", padx=8, pady=10)
ingreso_nombre_usuario.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del correo electronico
ingreso_correo_electronico = Entry(marco, textvariable=correo)
ingreso_correo_electronico.grid(row=3, column=1, sticky="w", padx=8, pady=10)
ingreso_correo_electronico.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Ingreso de la edad
ingreso_edad = Entry(marco, textvariable=edad)
ingreso_edad.grid(row=4, column=1, sticky="w", padx=8, pady=10)
ingreso_edad.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Entry para el costo de la cuenta
ingreso_costo_cuenta = Entry(marco, textvariable=costo)
ingreso_costo_cuenta.grid(row=5, column=2, sticky="w", padx=8, pady=10)
ingreso_costo_cuenta.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
cuenta=IntVar()
# Opcion de cuenta basica
cuenta_basica=Radiobutton(marco, text="Basica", variable=cuenta, value=1)
cuenta_basica.grid(row=1, column=2, sticky="w", padx=10, pady=10)
cuenta_basica.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de cuenta premium
cuenta_premium=Radiobutton(marco, text="Premium", variable=cuenta, value=2)
cuenta_premium.grid(row=2, column=2, sticky="w", padx=10, pady=10)
cuenta_premium.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de cuenta administrador
cuenta_admin=Radiobutton(marco, text="Administrador", variable=cuenta, value=3)
cuenta_admin.grid(row=3, column=2, sticky="w", padx=10, pady=10)
cuenta_admin.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
CASILLAS DE VERIFICACION
"""
# Son TRES porque son INDEPENDIENTES
ofertas=IntVar()
sms=IntVar()
resumen=IntVar()
# VENCIMIENTO
check_ofertas = Checkbutton(marco, text="e-mail", variable=ofertas, onvalue=1, offvalue=0)
check_ofertas.grid(row=1,column=3,sticky="w",padx=10,pady=10)
check_ofertas.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# EXTENSION
check_sms = Checkbutton(marco, text="WhatsApp", variable=sms, onvalue=1, offvalue=0)
check_sms.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_sms.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# NOVEDADES
check_resumen = Checkbutton(marco, text="SMS", variable=resumen, onvalue=1, offvalue=0)
check_resumen.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_resumen.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
BOTONES DE ACCION
"""
#Boton de ingesar.
boton_ingresar = Button(marco, text="Ingresar", command=lambda:ingresar_registro())
boton_ingresar.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=10)
boton_ingresar.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))
#Boton de cancelar prestamo.
boton_cancelar = Button(marco, text="Cancelar", command=lambda:cancelar())
boton_cancelar.grid(row=6, column=0, columnspan=2, sticky="w", padx=10, pady=10)
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
#Boton de salir.
boton_salir = Button(marco, text="Salir", command=lambda:salida())
boton_salir.grid(row=7, column=0, columnspan=2, sticky="w", padx=10, pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))
# Boton para calcular el costo de la cuenta
boton_calcular_costo = Button(marco, text="Calcular costo mensual", command=lambda:calcular_costo(cuenta.get()))
boton_calcular_costo.grid(row=4, column=2, columnspan=2, sticky="w", padx=20, pady=20)
boton_calcular_costo.config(fg = "blue", bg = "white", width = 30, font = ("Calibri", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()