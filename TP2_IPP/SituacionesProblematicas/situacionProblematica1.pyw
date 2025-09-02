from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de nuevos alumnos de la academia ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
try:
    raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\icono2.ico')
except Exception:
    pass

# El metodo config() es para configurar los widgets.
raiz.config(bg = "purple") # bg: background (color de fondo).
raiz.config(cursor = "pencil") # cursor: es el iconito del mouse.

# Creo el marco (está contenido DENTRO de la ventana raiz).
marco = Frame(raiz, padx=20, pady=20)
# .pack() porque va a formar parte de la ventana raiz.
marco.pack(fill="none", expand=True)
# fill=x : rellena de forma VERTICAL
# fill=y : rellena de forma horizonal
# fill=both: rellena en vertical y horizonal
# expand centraliza el frame dentro de la ventana raiz
marco.config(bg = "grey", relief= "groove") # Configuro el color, el ancho y el alto respectivamente. 
#Las dimensiones ya las tiene el marco, por eso se las quito a la ventana raiz porque es obvio que la raiz va a ser más grande que el marco.

"""
Empiezo a ingresar las cosas que me piden
(TODOS LOS OBJETOS (WIDGETS)TIENEN SU CREACION, UBICACION Y SU CONFIGURACION)
El sticky es la ubicacion del objeto en la celda y el anchor es la ubicacion del texto en el objeto.
"""

# Etiqueta del nombre completo
etiqueta_nombre_completo = Label(marco, text="Nombre completo:")
etiqueta_nombre_completo.grid(row=0, column=0, sticky="w", padx=20, pady=30) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_completo.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del nombre completo
ingreso_nombre_completo = Entry(marco)
ingreso_nombre_completo.grid(row=0, column=1, sticky="w", pady=30)
ingreso_nombre_completo.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta del numero de documento
etiqueta_nro_documento = Label(marco, text="N° de documento:")
etiqueta_nro_documento.grid(row=1, column=0, sticky="w", padx=20, pady=30) 
etiqueta_nro_documento.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del nnumero de documento
ingreso_nro_documento = Entry(marco)
ingreso_nro_documento.grid(row=1, column=1, sticky="w", pady=30)
ingreso_nro_documento.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))

# Etiqueta del correo electronico
etiqueta_correo_electronico = Label(marco, text="Correo electrónico:")
etiqueta_correo_electronico.grid(row=2, column=0, sticky="w", padx=20, pady=30)
etiqueta_correo_electronico.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Ingreso del correo electronico
ingreso_correo_electronico = Entry(marco)
ingreso_correo_electronico.grid(row=2, column=1, sticky="w", pady=30)
ingreso_correo_electronico.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
"""
Termino a ingresar las cosas que me piden
"""

"""
Boton de registrar alumno.
"""
boton_registrar = Button(marco, text="Registrar")
boton_registrar.grid(row=3, column=0, columnspan=2, pady=10)
boton_registrar.config(fg = "green", bg = "white", width = 30, font = ("Arial", 14, "italic"))

"""
Boton de cancelar alumno.
"""
boton_cancelar = Button(marco, text="Cancelar")
boton_cancelar.grid(row=4, column=0, columnspan=2, pady=10)
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga.
raiz.mainloop()