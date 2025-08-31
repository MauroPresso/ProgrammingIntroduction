from tkinter import *

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de nuevos alumnos de la academia ****")

# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\icono2.ico')

# El metodo config() es para configurar los widgets.
raiz.config(bg = "black") # bg: background (color de fondo).
raiz.config(cursor = "pencil") # cursor: es el iconito del mouse.
raiz.config(relief= "groove") # Relieve


# Creo el marco (está contenido DENTRO de la ventana raiz).
marco = Frame()
# .pack() porque va a formar parte de la ventana raiz.
marco.pack(fill="y", expand=True)
# fill =x: rellena de forma VERTICAL
# fill=y: rellena de forma horizonal
# fill =both rellena en vertical y horizonal
# expand centraliza el frame dentro de la ventana raiz
marco.config(bg = "purple", width = "850", height = "550") # Configuro el color, el ancho y el alto respectivamente. 
#Las dimensiones ya las tiene el marco, por eso se las quito a la ventana raiz porque es obvio que la raiz va a ser más grande que el marco.


# Mantengo la ventana abierta para que no se cierre hasta que yo le diga
raiz.mainloop()