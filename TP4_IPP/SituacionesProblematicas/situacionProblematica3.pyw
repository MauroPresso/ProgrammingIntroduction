from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

"""
 @brief Función que maneja la cancelación del turno.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar esta inscripción")
    # Entrys
    nombre_lector.set("")
    fecha.set(0)
    titulo.set("")
    dias.set(0)
    # Botones de opción
    categoria.set(0)
    # Casillas de verificación
    vencimiento.set(0)
    extension.set(0)
    novedades.set(0)

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
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\book.ico')
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
etiqueta_categoria_libro.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta de las opciones de servicios adicionales
etiqueta_servicios_adicionales = Label(marco, text="Servicios adicionales:")
etiqueta_servicios_adicionales.grid(row=0, column=3, sticky="w", padx=10, pady=8)
etiqueta_servicios_adicionales.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

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
ingreso_nombre_lector.config(fg = "skyblue", bg = "black", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del titulo del libro
ingreso_titulo_libro = Entry(marco, textvariable=titulo)
ingreso_titulo_libro.grid(row=2, column=1, sticky="w", pady=8)
ingreso_titulo_libro.config(fg = "skyblue", bg = "black", width = 30, font = ("Arial", 14, "italic"))
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
#Boton de confirmar turno.
boton_cargar = Button(marco, text="Cargar prestamo")
boton_cargar.grid(row=5, column=0, columnspan=2, pady=12)
boton_cargar.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))
#Boton de cancelar prestamo.
boton_cancelar = Button(marco, text="Cancelar", command=lambda:cancelar())
boton_cancelar.grid(row=6, column=0, columnspan=2, pady=10)
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
#Boton de salir.
boton_salir = Button(marco, text="Salir", command=lambda:salida())
boton_salir.grid(row=7, column=0, columnspan=2, pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()