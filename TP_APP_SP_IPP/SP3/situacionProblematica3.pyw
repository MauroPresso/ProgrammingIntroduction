# @file situacionProblematica3.pyw
#
# @brief Programa que permite ingresar los datos de un prestamo de un libro de una biblioteca.
# @date 09/22/2025
# @author Mauro Presso
# @version 3.0
# @details
# Situación Problemática Nº3 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
from classPrestamo import Prestamo

"""
FUNCIONES
"""

""" 
 @brief Función que determina la categoría del libro según el valor seleccionado.
 @param valor (int) - Valor seleccionado en el botón de opción.
 @return categoría (str) - Categoría del libro correspondiente al valor.
"""
def determinar_categoria(valor):
    if valor == 1:
        return "Novela"
    elif valor == 2:
        return "Historia"
    elif valor == 3:
        return "Ciencia"
    else:
        return "Infantil"

"""
 @brief Función que convierte la categoría del libro a su valor correspondiente.
 @param categoria (str) - Categoría del libro.
 @return valor (int) - Valor correspondiente a la categoría.
"""
def categoria_a_valor(categoria):
    if categoria == "Novela":
        return 1
    elif categoria == "Historia":
        return 2
    elif categoria == "Ciencia":
        return 3
    else:
        return 4

"""
 @brief Función que cuenta la cantidad de preferencias seleccionadas.
 @param none
 @return contador_preferencias (int) - Cantidad de preferencias seleccionadas.
"""
def contar_preferencias():
    contador_preferencias = 0
    if vencimiento.get() != 0 or extension.get() != 0 or novedades.get() != 0:
        if vencimiento.get() == 1:
            contador_preferencias += 1
        if extension.get() == 1:
            contador_preferencias += 1
        if novedades.get() == 1:
            contador_preferencias += 1
    return contador_preferencias

"""
 @brief Función que convierte el número de servicios seleccionados a los valores de los checkbuttons
 @param servicios (int) - Número de servicios seleccionados.
 @return none
"""
def servicios_a_checkbuttons(servicios):
    if servicios == 0:
        vencimiento.set(0)
        extension.set(0)
        novedades.set(0)
    elif servicios == 1:
        vencimiento.set(1)
        extension.set(0)
        novedades.set(0)
    elif servicios == 2:
        vencimiento.set(1)
        extension.set(1)
        novedades.set(0)
    else:
        vencimiento.set(1)
        extension.set(1)
        novedades.set(1)

"""
 @brief Funcion que vacia los entrys.
 @param none
 @return none
"""
def limpiar_campos():
    # Entrys
    nombre_lector.set("")
    titulo.set("")
    ingreso_fecha_devolucion.set_date(date.today())
    # Radiobuttons
    categoria.set(0)
    # Checkbuttons
    vencimiento.set(0); extension.set(0); novedades.set(0)
    # Foco en el primer entry
    ingreso_nombre_lector.focus()

"""
 @brief Funcion que administra los estados de los entrys y los botones de accion.
 @param estado (string)
 @return none
"""
def state_textbox_and_checkbuttons(estado):
    # Entrys
    ingreso_nombre_lector.config(state=estado)
    ingreso_titulo_libro.config(state=estado)
    ingreso_fecha_devolucion.config(state=estado)
    # Radiobuttons
    categoria_ciencia.config(state=estado)
    categoria_historia.config(state=estado)
    categoria_novela.config(state=estado)
    categoria_infantil.config(state=estado)
    # Checkbuttons
    check_vencimiento.config(state=estado)
    check_extension.config(state=estado)
    check_novedades.config(state=estado)

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
    registros=Prestamo.ListarPrestamos()
    for r in registros:
        #              VINC.C/CAMPO0(ID) VALORES(OTROS CAMPOS)               
        visorBD.insert('', 0, text=r[0], values=(r[1], r[2], r[3], r[4], r[5]))

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
    ingreso_nombre_lector.focus() #nombre del entry
    # deshabilito Entrys
    state_textbox_and_checkbuttons("normal")
    # Botones de accion
    boton_nuevo.config(state="disabled")
    boton_modificar.config(state="disabled")
    boton_eliminar.config(state="disabled")
    boton_cancelar.config(state="normal")
    boton_guardar.config(state="normal")

"""
 @brief Función que maneja la cancelación del prestamo.
 @param none
 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este prestamo")
    # Entrys
    limpiar_campos()
    ingreso_nombre_lector.focus() #nombre del entry
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
    if nombre_lector.get() == "" or titulo.get() == "" or ingreso_fecha_devolucion.get_date() <= date.today() or categoria.get() == 0:
        if nombre_lector.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif titulo.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el título del libro.")
        elif ingreso_fecha_devolucion.get_date() <= date.today():
            messagebox.showerror("ERROR", "Por favor, ingresa la fecha de devolución válida.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa la categoría del libro.")
    else:
        global registroNuevo
        if messagebox.askquestion("CONFIRMAR GUARDADO", "¿Confirma que desea guardar el préstamo?") == "yes":
            if registroNuevo==True:
                miPrestamo = Prestamo(nombre=nombre_lector.get(), titulo=titulo.get(), fecha=ingreso_fecha_devolucion.get_date(), categoria=determinar_categoria(categoria.get()), servicios=contar_preferencias())
                miPrestamo.Agregar()
                messagebox.showinfo("AGREGAR Prestamo", "El préstamo ha sido agregado correctamente.")
            else:
                miPrestamo = Prestamo(id=visorBD.item(visorBD.selection())['text'], nombre=nombre_lector.get(), titulo=titulo.get(), fecha=ingreso_fecha_devolucion.get_date(), categoria=determinar_categoria(categoria.get()), servicios=contar_preferencias())
                miPrestamo.Modificar()
                messagebox.showinfo("MODIFICAR Prestamo", "El préstamo ha sido modificado correctamente.")
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
            messagebox.showinfo("GUARDAR Prestamo", "El préstamo NO ha sido guardado")

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
        nombre_lector.set(visorBD.item(visorBD.selection())['values'][0])
        titulo.set(visorBD.item(visorBD.selection())['values'][1])
        fecha.set(visorBD.item(visorBD.selection())['values'][2])
        categoria.set(categoria_a_valor(visorBD.item(visorBD.selection())['values'][3]))
        servicios_a_checkbuttons(visorBD.item(visorBD.selection())['values'][4])
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
        miAlumno = Prestamo(id=int(visorBD.item(visorBD.selection())['text']))
        if messagebox.askquestion("CONFIRMAR ELIMINACIÓN", "¿Confirma que desea eliminar el préstamo?") == "yes":  
            miAlumno.Eliminar()
            limpiar_campos()
            state_textbox_and_checkbuttons("disabled")
            cargarEnVisorBD()
        else:
            messagebox.showinfo("ELIMINAR Prestamo", "El préstamo NO ha sido eliminado.")
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
raiz.title("**** Registro de prestamos de la biblioteca ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)
raiz.resizable(True, True)
# Icono
try:
    raiz.iconbitmap('TP_APP_SP_IPP\\SP3\\book.ico')
except Exception:
    pass
raiz.config(bg = "brown") # bg: background (color de fondo).
raiz.config(cursor = "spider") # cursor: es el iconito del mouse.

"""
FRAME
"""
marco = Frame(raiz, padx=20, pady=20)
marco.pack(fill="x", expand=True)
marco.config(bg = "orange", relief= "solid") 

"""
ETIQUETAS
"""
# Subtitulo de la app
etiqueta_subtitulo = Label(marco, text = "DATOS DEL LIBRO Y EL LECTOR")
etiqueta_subtitulo.grid(row=0,column=0,sticky="w",padx=10,pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_subtitulo.config(fg = "yellow", bg = "black", width = 40, font = ("Rockell", 14, "italic"))
# Etiqueta del nombre completo
etiqueta_nombre_lector = Label(marco, text="Nombre del lector:")
etiqueta_nombre_lector.grid(row=1, column=0, sticky="w", padx=10, pady=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_lector.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del titulo del libro
etiqueta_titulo_libro = Label(marco, text="Titulo del libro:")
etiqueta_titulo_libro.grid(row=2, column=0, sticky="w", padx=10, pady=8)
etiqueta_titulo_libro.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la fecha de devolucion
etiqueta_fecha_devolucion = Label(marco, text="Fecha de devolucion:")
etiqueta_fecha_devolucion.grid(row=3, column=0, sticky="w", padx=10, pady=8)
etiqueta_fecha_devolucion.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de la categoria del libro
etiqueta_categoria_libro = Label(marco, text="Categoria del libro:")
etiqueta_categoria_libro.grid(row=0, column=2, sticky="w", padx=10, pady=8)
etiqueta_categoria_libro.config(fg = "yellow", bg = "black", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de las opciones de servicios adicionales
etiqueta_servicios_adicionales = Label(marco, text="Servicios adicionales:")
etiqueta_servicios_adicionales.grid(row=0, column=3, sticky="w", padx=10, pady=8)
etiqueta_servicios_adicionales.config(fg = "yellow", bg = "black", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
INGRESOS
"""
# Variables de control de los ingresos
nombre_lector = StringVar()
titulo = StringVar()
fecha = StringVar()
dias = IntVar()                                                
# Ingreso del nombre lector
ingreso_nombre_lector = Entry(marco, textvariable=nombre_lector)
ingreso_nombre_lector.grid(row=1, column=1, sticky="w", pady=8)
ingreso_nombre_lector.config(fg = "yellow", bg = "brown", width = 30, font = ("Arial", 14, "italic"), state="disabled")
# Ingreso del titulo del libro
ingreso_titulo_libro = Entry(marco, textvariable=titulo)
ingreso_titulo_libro.grid(row=2, column=1, sticky="w", pady=8)
ingreso_titulo_libro.config(fg = "yellow", bg = "brown", width = 30, font = ("Arial", 14, "italic"), state="disabled")
# Ingreso de la fecha de devolucion
ingreso_fecha_devolucion = DateEntry(marco, date_pattern='dd/mm/yyyy', textvariable=fecha)
ingreso_fecha_devolucion.grid(row=3, column=1, sticky="w", pady=8)
ingreso_fecha_devolucion.config(width = 30, state="disabled")

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
categoria=IntVar()
# Opcion de categoria novela
categoria_novela=Radiobutton(marco, text="Novela", variable=categoria, value=1)
categoria_novela.grid(row=1, column=2, sticky="w", padx=10, pady=10)
categoria_novela.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# Opcion de categoria historia
categoria_historia=Radiobutton(marco, text="Historia", variable=categoria, value=2)
categoria_historia.grid(row=2, column=2, sticky="w", padx=10, pady=10)
categoria_historia.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# Opcion de categoria ciencia
categoria_ciencia=Radiobutton(marco, text="Ciencia", variable=categoria, value=3)
categoria_ciencia.grid(row=3, column=2, sticky="w", padx=10, pady=10)
categoria_ciencia.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# Opcion de categoria infantil
categoria_infantil=Radiobutton(marco, text="Infantil", variable=categoria, value=4)
categoria_infantil.grid(row=4, column=2, sticky="w", padx=10, pady=10)
categoria_infantil.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")

"""
CASILLAS DE VERIFICACION
"""
# Son TRES porque son INDEPENDIENTES
vencimiento=IntVar()
extension=IntVar()
novedades=IntVar()
# VENCIMIENTO
check_vencimiento = Checkbutton(marco, text="e-mail", variable=vencimiento, onvalue=1, offvalue=0)
check_vencimiento.grid(row=1,column=3,sticky="w",padx=10,pady=10)
check_vencimiento.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# EXTENSION
check_extension = Checkbutton(marco, text="WhatsApp", variable=extension, onvalue=1, offvalue=0)
check_extension.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_extension.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")
# NOVEDADES
check_novedades = Checkbutton(marco, text="SMS", variable=novedades, onvalue=1, offvalue=0)
check_novedades.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_novedades.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w", state="disabled")

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
visorBD=ttk.Treeview(marco, columns=('NombreDelLector', 'Titulo', 'FechaDeDevolucion', 'Categoria', 'ServiciosAdicionales'))
visorBD.grid(row=7, column=0, columnspan=3, sticky="nsew")
# Scrollbar
barraDespl=ttk.Scrollbar(marco, orient=VERTICAL, command=visorBD.yview)
barraDespl.grid(row=7, column=3, sticky="ns")
visorBD.configure(yscrollcommand=barraDespl.set)
# CONFIGURACION
# ID
visorBD.heading('#0', text="ID")
visorBD.column('#0', width=30)
# Nombre
visorBD.heading('#1', text="Nombre Del Lector")
visorBD.column('#1', width=100)
# Titulo
visorBD.heading('#2', text="Titulo")
visorBD.column('#2', width=100)
# Fecha De Devolucion
visorBD.heading('#3', text="Fecha De Devolucion")
visorBD.column('#3', width=100)
# Categoria
visorBD.heading('#4', text="Categoria")
visorBD.column('#4', width=100)
# Servicios Adicionales
visorBD.heading('#5', text="Servicios Adicionales")
visorBD.column('#5', width=100)

# Cargar datos en el visor
cargarEnVisorBD()

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()