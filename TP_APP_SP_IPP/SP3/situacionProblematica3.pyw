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
 @brief Función que maneja el cargado del prestamo.

 @param none

 @return none
"""
def cargar_prestamo(): 
    # Entrys
    if nombre_lector.get() == "" or titulo.get() == "":
        if nombre_lector.get() == "":
            messagebox.showerror("ERROR","No ingresaste tu nombre")
        else: 
            messagebox.showerror("ERROR","No ingresaste el titulo del libro")
    # Botones de opción
    elif categoria.get() != 1 and categoria.get() != 2 and categoria.get() != 3 and categoria.get() != 4:
        messagebox.showerror("ERROR","No seleccionaste una categoria del libro")
    else:
        cantidad_preferencias=contar_preferencias()
        categoria_libro=determinar_categoria(categoria.get())
        messagebox.showinfo("SU TURNO FUE REGISTRADO CON ÉXITO", f"Nombre del lector: {nombre_lector.get()}\nTitulo del libro: {titulo.get()}\nFecha de devolucion: {fecha.get()}\nCategoria del libro: {categoria_libro}\nServicios adicionales seleccionados: {cantidad_preferencias}/3")

"""
 @brief Función que maneja la limpieza de los campos de entrada de texto.

 @param none

 @return none
"""
def nuevo():
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    # Entrys
    nombre_lector.set("")
    titulo.set("")
    ingreso_fecha_devolucion.set_date(date.today())
    # Botones de opción
    categoria.set(0)
    # Casillas de verificación
    vencimiento.set(0)
    extension.set(0)
    novedades.set(0)
    ingreso_nombre_lector.focus() #nombre del entry

"""
 @brief Función que maneja la cancelación del prestamo.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar este prestamo")
    # Entrys
    nombre_lector.set("")
    titulo.set("")
    ingreso_fecha_devolucion.set_date(date.today())
    # Botones de opción
    categoria.set(0)
    # Casillas de verificación
    vencimiento.set(0)
    extension.set(0)
    novedades.set(0)
    ingreso_nombre_lector.focus() #nombre del entry

""" 
 @brief Función que maneja la inscripción del alumno.
 @param none
 @return none
"""
def guardar():
    if nombre_lector.get() == "" or titulo.get() == "" or fecha.get() == date.today() or categoria.get() == "":
        if nombre_lector.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif titulo.get() == "":
            messagebox.showerror("ERROR", "Por favor, ingresa el título del libro.")
        elif fecha.get() == date.today():
            messagebox.showerror("ERROR", "Por favor, ingresa la fecha de devolución.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa la categoría del libro.")
    else:
        miPrestamo = Prestamo(nombre=nombre_lector.get(), titulo=titulo.get(), fecha=fecha.get(), categoria=categoria.get(), servicios=contar_preferencias())
        miPrestamo.Agregar()

"""
 @brief Función que maneja la modificación de la inscripción.
 
 @param none
    
 @return none
"""
def modificar():
    if nombre_lector.get() == "" and titulo.get() == "" and fecha.get() == date.today() and categoria.get() == "":
        messagebox.showerror("ERROR", "No hay préstamo para modificar.")
    else:
        respuesta = messagebox.askquestion("MODIFICAR PRESTAMO", "Confirmar que desea modificar el préstamo")
        if respuesta=="yes":
            messagebox.showinfo("MODIFICAR PRESTAMO", "El préstamo ha sido modificado")
            miPrestamo = Prestamo(nombre=nombre_lector.get(), titulo=titulo.get(), fecha=fecha.get(), categoria=categoria.get(), servicios=contar_preferencias())
            miPrestamo.Modificar()

"""
 @brief Función que maneja la eliminación de la inscripción.

 @param none

 @return none
"""
def eliminar():

    if nombre_lector.get() == "" and titulo.get() == "" and fecha.get() == 0 and categoria.get() == "":
        messagebox.showerror("ERROR", "No hay préstamo para eliminar.")
    else:
        respuesta = messagebox.askquestion("ELIMINAR PRESTAMO", "Confirmar que desea eliminar el préstamo")
        if respuesta=="yes":
            messagebox.showinfo("ELIMINAR PRESTAMO", "El préstamo ha sido eliminado")
            miPrestamo = Prestamo(nombre=nombre_lector.get(), titulo=titulo.get(), fecha=fecha.get(), categoria=categoria.get(), servicios=contar_preferencias())
            miPrestamo.Eliminar()


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
marco.pack(fill="y", expand=True)
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
ingreso_nombre_lector.config(fg = "yellow", bg = "brown", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del titulo del libro
ingreso_titulo_libro = Entry(marco, textvariable=titulo)
ingreso_titulo_libro.grid(row=2, column=1, sticky="w", pady=8)
ingreso_titulo_libro.config(fg = "yellow", bg = "brown", width = 30, font = ("Arial", 14, "italic"))
# Ingreso de la fecha de devolucion
ingreso_fecha_devolucion = DateEntry(marco, date_pattern='dd/mm/yyyy', textvariable=fecha)
ingreso_fecha_devolucion.grid(row=3, column=1, sticky="w", pady=8)
ingreso_fecha_devolucion.config(width = 30)

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
categoria=IntVar()
# Opcion de categoria novela
categoria_novela=Radiobutton(marco, text="Novela", variable=categoria, value=1)
categoria_novela.grid(row=1, column=2, sticky="w", padx=10, pady=10)
categoria_novela.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de categoria historia
categoria_historia=Radiobutton(marco, text="Historia", variable=categoria, value=2)
categoria_historia.grid(row=2, column=2, sticky="w", padx=10, pady=10)
categoria_historia.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de categoria ciencia
categoria_ciencia=Radiobutton(marco, text="Ciencia", variable=categoria, value=3)
categoria_ciencia.grid(row=3, column=2, sticky="w", padx=10, pady=10)
categoria_ciencia.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de categoria infantil
categoria_infantil=Radiobutton(marco, text="Infantil", variable=categoria, value=4)
categoria_infantil.grid(row=4, column=2, sticky="w", padx=10, pady=10)
categoria_infantil.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

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
check_vencimiento.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# EXTENSION
check_extension = Checkbutton(marco, text="WhatsApp", variable=extension, onvalue=1, offvalue=0)
check_extension.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_extension.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# NOVEDADES
check_novedades = Checkbutton(marco, text="SMS", variable=novedades, onvalue=1, offvalue=0)
check_novedades.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_novedades.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

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