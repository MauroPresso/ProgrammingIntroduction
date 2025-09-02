from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de prestamos de la biblioteca ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
try:
    raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\book.ico')
except Exception:
    pass

# El metodo config() es para configurar los widgets.
raiz.config(bg = "brown") # bg: background (color de fondo).
raiz.config(cursor = "spider") # cursor: es el iconito del mouse.

# Creo el marco (está contenido DENTRO de la ventana raiz).
marco = Frame(raiz, padx=20, pady=20)
# .pack() porque va a formar parte de la ventana raiz.
marco.pack(fill="y", expand=True)
# fill=x : rellena de forma VERTICAL
# fill=y : rellena de forma horizonal
# fill=both: rellena en vertical y horizonal
# expand centraliza el frame dentro de la ventana raiz
marco.config(bg = "orange", relief= "solid") # Configuro el color, el ancho y el alto respectivamente. 
#Las dimensiones ya las tiene el marco, por eso se las quito a la ventana raiz porque es obvio que la raiz va a ser más grande que el marco.

"""
Empiezo a ingresar las cosas que me piden
"""

# Etiqueta del nombre completo
etiqueta_nombre_lector = Label(marco, text="Nombre del lector:")
etiqueta_nombre_lector.grid(row=0, column=0, sticky="w", padx=10, pady=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_lector.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del nombre lector
ingreso_nombre_lector = Entry(marco)
ingreso_nombre_lector.grid(row=0, column=1, sticky="w", pady=8)
ingreso_nombre_lector.config(fg = "skyblue", bg = "black", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta del titulo del libro
etiqueta_titulo_libro = Label(marco, text="Titulo del libro:")
etiqueta_titulo_libro.grid(row=1, column=0, sticky="w", padx=10, pady=8)
etiqueta_titulo_libro.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del titulo del libro
ingreso_titulo_libro = Entry(marco)
ingreso_titulo_libro.grid(row=1, column=1, sticky="w", pady=8)
ingreso_titulo_libro.config(fg = "skyblue", bg = "black", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta de la fecha de devolucion
etiqueta_fecha_devolucion = Label(marco, text="Fecha de devolucion:")
etiqueta_fecha_devolucion.grid(row=2, column=0, sticky="w", padx=10, pady=8)
etiqueta_fecha_devolucion.config(fg = "purple", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso de la fecha de devolucion
ingreso_fecha_devolucion = Entry(marco)
ingreso_fecha_devolucion.grid(row=2, column=1, sticky="w", pady=8)
ingreso_fecha_devolucion.config(fg = "skyblue", bg = "black", width = 30, font = ("Arial", 14, "italic"))

"""
Termino a ingresar las cosas que me piden
"""

"""
Boton de confirmar turno.
"""
boton_cargar = Button(marco, text="Cargar prestamo")
boton_cargar.grid(row=3, column=0, columnspan=2, pady=12)
boton_cargar.config(fg = "green", bg = "white", width = 30, font = ("Calibri", 14, "italic"))

"""
Boton de cancelar prestamo.
"""
boton_cancelar = Button(marco, text="Cancelar")
boton_cancelar.grid(row=4, column=0, columnspan=2, pady=10)
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))

"""
Boton de cancelar prestamo.
"""
boton_salir = Button(marco, text="Salir")
boton_salir.grid(row=5, column=0, columnspan=2, pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()