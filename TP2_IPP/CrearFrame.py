# Importo TKinter
from tkinter import *

# Creo la raiz
raiz = Tk()

# Icono
raiz.iconbitmap('TP2_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\audio.ico')
# Titulo
raiz.title("**** Intro A la Programacion - Año 2025 ****")
# Cursor
raiz.config(cursor="star")

# Resizing window
#raiz.resizable( Ancho (True or False), Alto (True or False))

# Probando combinaciones posibles
raiz.resizable(True, True)

# Configuramos el raiz 
raiz.config(bg = "blue")
marco = Frame()

# Aca le indicamos que el frame va a formar parte de la ventana
marco.pack()

# Configuraciones del marco, color, ancho, alto
marco.config(bg = "pink", width = "650", height = "350")

# Mantengo el ciclo
raiz.mainloop()