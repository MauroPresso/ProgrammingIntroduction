from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana

# Titulo de la ventana
raiz.title("**** Registro de nuevos alumnos de la academia ****")

# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\book.ico')

# El metodo config() es para configurar los widgets.
raiz.config(bg = "green") # bg: background (color de fondo).
raiz.config(cursor = "pencil") # cursor: es el iconito del mouse.
raiz.config(width = "650", height = "350") # Configuro el ancho y el alto respectivamente.
raiz.config(relief= "sunken") # Relieve


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()