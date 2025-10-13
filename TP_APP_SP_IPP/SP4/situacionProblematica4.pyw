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
from tkcalendar import DateEntry
from datetime import date
from classCompra import Compra

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
FUNCIONES
"""
""" 
 @brief Función que convierte la hora y minutos en formato SQL.
 @param hora (int) - Hora del Compra.
 @param minutos (int) - Minutos del Compra.
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
    nombre.set("")
    producto.set("")
    ingreso_fecha_entrega.set_date(date.today())
    hora_entrega.set(0); minuto_entrega.set(0)
    cuenta.set(0)
    ofertas.set(0); resumen.set(0); sms.set(0)
    ingreso_nombre_cliente.focus()

""" 
 @brief Función que cancela el registro actual, limpiando todos los campos de entrada.
 @param none
 @return none
 """
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este Compra")
    nombre.set("")
    producto.set("")
    ingreso_fecha_entrega.set_date(date.today())
    hora_entrega.set(0); minuto_entrega.set(0)
    ofertas.set(0); resumen.set(0); sms.set(0)
    ingreso_nombre_cliente.focus()
    cuenta.set(0)

"""
 @brief Función que cuenta la cantidad de preferencias seleccionadas.
 @param none
 @return contador_preferencias (int) - Cantidad de preferencias seleccionadas.
"""
def contar_preferencias():
    contador_preferencias = 0
    if ofertas.get() != 0 or resumen.get() != 0 or sms.get() != 0:
        if ofertas.get() == 1:
            contador_preferencias += 1
        if resumen.get() == 1:
            contador_preferencias += 1
        if sms.get() == 1:
            contador_preferencias += 1
    return contador_preferencias

"""
 @brief Función que guarda el registro del Compra del paciente.
 @param none
 @return none
"""
def guardar():
    condicion_hora = (hora_entrega.get() < 0 or hora_entrega.get() > 23)
    condicion_minuto = (minuto_entrega.get() < 0 or minuto_entrega.get() > 59)
    condicion_fecha = ((ingreso_fecha_entrega.get_date()) <= date.today())
    condicion_paciente = (nombre.get() == "")
    condicion_producto = (producto.get() == "")
    condicion_cuenta = (cuenta.get() == 0)
    if condicion_paciente or condicion_producto or condicion_cuenta or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_paciente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_producto:
            messagebox.showerror("ERROR", "Por favor, ingresa el producto del Compra.")
        elif condicion_cuenta:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("GUARDAR Compra", "Confirmar que desea guardar el Compra") == "yes":
            miCompra = Compra(
                nombre=nombre.get(),
                producto=producto.get(),
                fecha=ingreso_fecha_entrega.get_date(),
                horario=time_sql(hora_entrega.get(), minuto_entrega.get()),
                tipoDeCuenta=determinar_tipo_de_cuenta(cuenta.get()),
                preferencias=contar_preferencias()
            )
            miCompra.Agregar()
            messagebox.showinfo("GUARDAR Compra", "El Compra ha sido guardado")
        else:
            messagebox.showinfo("GUARDAR Compra", "El Compra NO ha sido guardado")

""" 
 @brief Función que modifica el registro del Compra del paciente.
 @param none
 @return none
"""
def modificar():
    condicion_hora = (hora_entrega.get() < 0 or hora_entrega.get() > 23)
    condicion_minuto = (minuto_entrega.get() < 0 or minuto_entrega.get() > 59)
    condicion_fecha = ((ingreso_fecha_entrega.get_date()) <= date.today())
    condicion_cliente = (nombre.get() == "")
    condicion_producto = (producto.get() == "")
    condicion_cuenta = (cuenta.get() == 0)
    if condicion_cliente or condicion_producto or condicion_cuenta or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_cliente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_producto:
            messagebox.showerror("ERROR", "Por favor, ingresa el producto del Compra.")
        elif condicion_cuenta:
            messagebox.showerror("ERROR", "Por favor, elige el tipo de cuenta.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("MODIFICAR Compra", "Confirmar que desea modificar el Compra") == "yes":
            miCompra = Compra(
            nombre=nombre.get(),
            producto=producto.get(),
            fecha=ingreso_fecha_entrega.get_date(),
            horario=time_sql(hora_entrega.get(), minuto_entrega.get()),
            tipoDeCuenta=determinar_tipo_de_cuenta(cuenta.get()),
            preferencias=contar_preferencias()
            )
            miCompra.Modificar()
        else:
            messagebox.showinfo("MODIFICAR Compra", "El Compra NO ha sido modificado")

""" 
 @brief Función que elimina el registro del Compra del paciente.
 @param none
 @return none
"""
def eliminar():
    condicion_hora = (hora_entrega.get() < 0 or hora_entrega.get() > 23)
    condicion_minuto = (minuto_entrega.get() < 0 or minuto_entrega.get() > 59)
    condicion_fecha = ((ingreso_fecha_entrega.get_date()) <= date.today())
    condicion_paciente = (nombre.get() == "")
    condicion_producto = (producto.get() == "")
    condicion_especialidad = (cuenta.get() == 0)
    if condicion_paciente or condicion_producto or condicion_especialidad or condicion_fecha or condicion_hora or condicion_minuto:
        if condicion_paciente:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_producto:
            messagebox.showerror("ERROR", "Por favor, ingresa el producto del Compra.")
        elif condicion_especialidad:
            messagebox.showerror("ERROR", "Por favor, elige la especialidad médica.")
        elif condicion_fecha:
            messagebox.showerror("ERROR", "Por favor, ingresa una fecha posterior a hoy.")
        elif condicion_hora:
            messagebox.showerror("ERROR", "Por favor, ingresa una hora válida (0-23).")     
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa minutos válidos (0-59).")
    else:
        if messagebox.askquestion("ELIMINAR Compra", "Confirmar que desea eliminar el Compra") == "yes":
            miCompra = Compra(
                nombre=nombre.get(),
                producto=producto.get(),
                fecha=ingreso_fecha_entrega.get_date(),
                horario=time_sql(hora_entrega.get(), minuto_entrega.get()),
                tipoDeCuenta=determinar_tipo_de_cuenta(cuenta.get()),
                preferencias=contar_preferencias()
            )
            miCompra.Eliminar()
        else:
            messagebox.showinfo("ELIMINAR Compra", "El Compra NO ha sido eliminado")

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
    raiz.iconbitmap('TP_APP_SP_IPP\\SP4\\Hello.ico')
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
# Etiqueta del nombre de producto
etiqueta_nombre_producto = Label(marco, text="Producto:")
etiqueta_nombre_producto.grid(row=2, column=0, sticky="w", pady=10, padx=8)
etiqueta_nombre_producto.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Separador entre hora
etiqueta_separador_hora_minuto = Label(marco, text="Horas:")
etiqueta_separador_hora_minuto.grid(row=5, column=1, sticky="w", padx=0, pady=10)
etiqueta_separador_hora_minuto.config(fg = "yellow", bg = "brown", width = 15, font = ("Rockell", 14, "italic"))
# Separador entre minuto
etiqueta_separador_minuto = Label(marco, text="Minutos:")
etiqueta_separador_minuto.grid(row=5, column=1, sticky="e", padx=0, pady=10)
etiqueta_separador_minuto.config(fg = "yellow", bg = "brown", width = 15, font = ("Rockell", 14, "italic"))
# Etiqueta del boton de opcion
# Etiqueta de la fecha de entrega
etiqueta_fecha_entrega = Label(marco, text="Fecha de entrega:")
etiqueta_fecha_entrega.grid(row=3, column=0, sticky="w", pady=10, padx=8)
etiqueta_fecha_entrega.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la hora de entrega
etiqueta_horario_entrega = Label(marco, text="Horario de entrega:")
etiqueta_horario_entrega.grid(row=6, column=0, sticky="w", pady=10, padx=8)
etiqueta_horario_entrega.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
ENTRYS
"""
# Variables para los Entrys
nombre = StringVar()
producto = StringVar()
fecha_entrega=StringVar()
hora_entrega=IntVar()
minuto_entrega=IntVar()
# Ingreso del nombre completo
ingreso_nombre_cliente = Entry(marco, textvariable=nombre)
ingreso_nombre_cliente.grid(row=1, column=1, sticky="w", padx=8, pady=10)
ingreso_nombre_cliente.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del nombre de producto
ingreso_nombre_producto = Entry(marco, textvariable=producto)
ingreso_nombre_producto.grid(row=2, column=1, sticky="w", padx=8, pady=10)
ingreso_nombre_producto.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del año de la fecha del Compra
ingreso_fecha_entrega = DateEntry(marco, date_pattern='yyyy/mm/dd', textvariable=fecha_entrega)
ingreso_fecha_entrega.grid(row=3, column=1, sticky="w", padx=10 ,pady=10)
ingreso_fecha_entrega.config(width = 30)
# Ingreso de la hora del Compra (timePicker)
ingreso_hora_entrega = Entry(marco, textvariable=hora_entrega)
ingreso_hora_entrega.grid(row=6, column=1, sticky="w", padx=10, pady=10)
ingreso_hora_entrega.config(fg = "brown", bg = "yellow", font = ("Arial", 14, "italic"), width=15)
# Ingreso de los minutos del Compra (timePicker)
ingreso_minuto_entrega = Entry(marco, textvariable=minuto_entrega)
ingreso_minuto_entrega.grid(row=6, column=1, sticky="e", padx=10, pady=10)
ingreso_minuto_entrega.config(fg = "brown", bg = "yellow", font = ("Arial", 14, "italic"), width=15)

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