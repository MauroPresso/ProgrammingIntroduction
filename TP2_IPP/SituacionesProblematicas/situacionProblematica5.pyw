from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de alumnos del instituto de idiomas ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
try:
    raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\audio.ico')
except Exception:
    pass

# El metodo config() es para configurar los widgets.
raiz.config(bg = "red") # bg: background (color de fondo).
raiz.config(cursor = "star") # cursor: es el iconito del mouse.

# Creo el marco (está contenido DENTRO de la ventana raiz).
marco = Frame(raiz, padx=20, pady=20)
# .pack() porque va a formar parte de la ventana raiz.
marco.pack(fill="y", expand=True)
# fill=x : rellena de forma VERTICAL
# fill=y : rellena de forma horizonal
# fill=both: rellena en vertical y horizonal
# expand centraliza el frame dentro de la ventana raiz
marco.config(bg = "yellow", relief= "ridge") # Configuro el color, el ancho y el alto respectivamente. 
#Las dimensiones ya las tiene el marco, por eso se las quito a la ventana raiz porque es obvio que la raiz va a ser más grande que el marco.

"""
Empiezo a ingresar las cosas que me piden
"""

# Etiqueta del nombre completo
etiqueta_nombre_alumno = Label(marco, text="Nombre del alumno:")
etiqueta_nombre_alumno.grid(row=0, column=0, sticky="w", padx=(0,10), pady=(0,8)) # .grid() para acomodar el objeto dentro del Frame.
# Ingreso del nombre del alumno
ingreso_nombre_alumno = Entry(marco)
ingreso_nombre_alumno.grid(row=0, column=1, sticky="ew", pady=(0,8))

# Etiqueta del Idioma que desea aprender
etiqueta_idioma_alumno = Label(marco, text="Idioma que desea aprender:")
etiqueta_idioma_alumno.grid(row=1, column=0, sticky="w", padx=(0,10), pady=(0,8))
# Ingreso del Idioma que desea aprender
ingreso_idioma_alumno = Entry(marco)
ingreso_idioma_alumno.grid(row=1, column=1, sticky="ew", pady=(0,8))

# Etiqueta del Nivel de conocimiento
etiqueta_nivel_conocimiento = Label(marco, text="Nivel de conocimiento:")
etiqueta_nivel_conocimiento.grid(row=2, column=0, sticky="w", padx=(0,10), pady=(0,8))
# Ingreso del Nivel de conocimiento
ingreso_nivel_conocimiento = Entry(marco)
ingreso_nivel_conocimiento.grid(row=2, column=1, sticky="ew", pady=(0,8))

"""
Termino a ingresar las cosas que me piden
"""

"""
Boton de confirmar turno.
"""
boton_inscribir = Button(marco, text="Inscribir")
boton_inscribir.grid(row=3, column=0, columnspan=2, pady=(12,0))


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()