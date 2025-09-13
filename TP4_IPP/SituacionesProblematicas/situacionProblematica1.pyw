# @file situacionProblematica1.pyw
#
# @brief Programa que permite ingresar los datos de un cliente y calcular el total de su factura.
# @date 09/22/2025
# @author Mauro Presso
# @version 1.0
# @details
# Situación Problemática Nº1 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox

"""
 @brief Función que alerta al usuario de Entry's sin completar.

 @param none

 @return none
"""
def advertir(): 
    # Nombre completo
    if ingreso_nombre_completo.get()=="": # En el entry del nombre completo no hay nada
        messagebox.showerror("ERROR","No ingresaste tu nombre")
    else:
        messagebox.showinfo("CONFIRMACIÓN","NOMBRE INGRESADO OK")
    # Numero de documento
    if ingreso_nro_documento.get()=="": # En el entry del numero de documento no hay nada
        messagebox.showerror("ERROR","No ingresaste tu numero de documento")
    else:
        messagebox.showinfo("CONFIRMACIÓN","NUMERO DE DOCUMENTO INGRESADO OK")
    # Correo electronico
    if ingreso_correo_electronico.get()=="": # En el entry del correo electronico no hay nada
        messagebox.showerror("ERROR","No ingresaste tu correo electronico")
    else:
        messagebox.showinfo("CONFIRMACIÓN","CORREO ELECTRONICO INGRESADO OK")  

"""
 @brief Función que maneja la salida de la aplicación.

 @param none

 @return none
"""

def salida():
    #                                   TITULO DE VENTANA   CARTEL DE LA VENTANA EMERGENTE
    #                                           |                           |
    #                                           V                           V
    respuesta = messagebox.askquestion("SALIDA DE LA APP", "Confirmar que sale de la apicacion")
    if respuesta=="yes":
        raiz.destroy() # cuando destroy lo vinculas a command no se pone parentesis. En este caso, si.
    else:
        messagebox.showinfo("SALIDA DE LA APP", "Aun sigues aqui, gracias por quedarte!")


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
    raiz.iconbitmap('TP4_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\icono2.ico')
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
boton_registrar.grid(row=3, column=0, columnspan=1, padx=10, pady=10)
boton_registrar.config(fg = "green", bg = "white", width = 30, font = ("Arial", 14, "italic"))

"""
Boton de cancelar alumno.
"""
boton_cancelar = Button(marco, text="Cancelar")
boton_cancelar.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))

"""
Boton de salir.
"""
boton_salir = Button(marco, text="Salir")
boton_salir.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga.
raiz.mainloop()