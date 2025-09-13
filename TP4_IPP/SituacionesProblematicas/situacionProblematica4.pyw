from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de usuarios de la tienda ONLINE ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
try:
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\Hello.ico')
except Exception:
    pass

# El metodo config() es para configurar los widgets.
raiz.config(bg = "blue") # bg: background (color de fondo).
raiz.config(cursor = "target") # cursor: es el iconito del mouse.

# Creo el marco (está contenido DENTRO de la ventana raiz).
marco = Frame(raiz, padx=20, pady=20)
# .pack() porque va a formar parte de la ventana raiz.
marco.pack(fill="x", expand=True)
# fill=x : rellena de forma VERTICAL
# fill=y : rellena de forma horizonal
# fill=both: rellena en vertical y horizonal
# expand centraliza el frame dentro de la ventana raiz
marco.config(bg = "green", relief= "raised") # Configuro el color, el ancho y el alto respectivamente. 
#Las dimensiones ya las tiene el marco, por eso se las quito a la ventana raiz porque es obvio que la raiz va a ser más grande que el marco.

"""
Empiezo a ingresar las cosas que me piden
"""

# Etiqueta del nombre completo
etiqueta_nombre_completo = Label(marco, text="Nombre completo:")
etiqueta_nombre_completo.grid(row=0, column=0, sticky="w", pady=10, padx=8) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_completo.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del nombre completo
ingreso_nombre_completo = Entry(marco)
ingreso_nombre_completo.grid(row=0, column=1, sticky="w", padx=8)
ingreso_nombre_completo.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta del nombre de usuario
etiqueta_nombre_usuario = Label(marco, text="Nombre de usuario:")
etiqueta_nombre_usuario.grid(row=1, column=0, sticky="w", pady=10, padx=8)
etiqueta_nombre_usuario.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del nombre de usuario
ingreso_nombre_usuario = Entry(marco)
ingreso_nombre_usuario.grid(row=1, column=1, sticky="w", padx=8)
ingreso_nombre_usuario.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta del correo electronico
etiqueta_correo_electronico = Label(marco, text="Correo electrónico:")
etiqueta_correo_electronico.grid(row=2, column=0, sticky="w", pady=10, padx=8)
etiqueta_correo_electronico.config(fg = "yellow", bg = "brown", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del correo electronico
ingreso_correo_electronico = Entry(marco)
ingreso_correo_electronico.grid(row=2, column=1, sticky="w", padx=8)
ingreso_correo_electronico.config(fg = "brown", bg = "yellow", width = 30, font = ("Arial", 14, "italic"))

"""
Termino a ingresar las cosas que me piden
"""

"""
Boton de ingesar.
"""
boton_ingresar = Button(marco, text="Ingresar")
boton_ingresar.grid(row=0, column=10, columnspan=2, padx=12)
boton_ingresar.config(fg = "green", bg = "white", width = 10, font = ("Calibri", 14, "italic"))

"""
Boton de cancelar prestamo.
"""
boton_cancelar = Button(marco, text="Cancelar")
boton_cancelar.grid(row=1, column=10, columnspan=2, padx=10)
boton_cancelar.config(fg = "red", bg = "white", width = 10, font = ("Times New Roman", 14, "italic"))

"""
Boton de salir.
"""
boton_salir = Button(marco, text="Salir")
boton_salir.grid(row=2, column=10, columnspan=2, padx=10)
boton_salir.config(fg = "red", bg = "black", width = 10, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()