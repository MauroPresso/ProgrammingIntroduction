# @file situacionProblematica1.pyw
#
# @brief Programa que permite ingresar los datos de un cliente y calcular el total de su factura.
# @date 09/22/2025
# @author Mauro Presso
# @version 2.0
# @details
# Situación Problemática Nº1 - Práctica Integral - Introducción a la Programación

from tkinter import *
from tkinter import messagebox

"""
 @brief Función que maneja el registro de la inscripción.

 @param none

 @return none
"""
def registrar(): 
    if nombre_completo.get() == "" or nro_documento.get() == 0 or correo_electronico.get() == "":
        # Nombre completo
        if nombre_completo.get() == "": # En el entry del nombre completo no hay nada
            messagebox.showerror("ERROR","No ingresaste tu nombre")
        # Numero de documento
        elif nro_documento.get() == 0: # En el entry del numero de documento no hay nada
            messagebox.showerror("ERROR","No ingresaste tu numero de documento")
        # Correo electronico
        else: # En el entry del correo electronico no hay nada
            messagebox.showerror("ERROR","No ingresaste tu correo electronico")  
    else:
        messagebox.showinfo("SU INSCRIPCION HA SIDO REGISTRADA CON ÉXITO", f"Alumno: {nombre_completo.get()}\nDNI: {nro_documento.get()}\nCorreo: {correo_electronico.get()}")

"""
 @brief Función que maneja la cancelación de la inscripción.

 @param none

 @return none
"""
def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar esta inscripción")
    # Entrys
    nombre_completo.set("")
    nro_documento.set(0)
    correo_electronico.set("")
    # Botones de opción
    nivel_estudios.set(0)
    # Casillas de verificación
    email.set(0)
    whatsapp.set(0)
    encuesta.set(0)

    

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

# Creando la ventana raiz
raiz = Tk()

# Configuro la ventana raiz

# Titulo de la ventana raiz
raiz.title("**** Registro de nuevos alumnos de la academia ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True)

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
ETIQUETAS
"""
# Subtitulo de la app
etiqueta_subtitulo = Label(marco, text = "*** REGISTRO DE NUEVOS ALUMNOS ***")
etiqueta_subtitulo.grid(row=0,column=0,sticky="w",padx=10,pady=10) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_subtitulo.config(fg = "white", bg = "black", width = 40, font = ("Rockell", 14, "italic"))
# Etiqueta del nombre completo
etiqueta_nombre_completo = Label(marco, text="Nombre completo:")
etiqueta_nombre_completo.grid(row=1, column=0, sticky="w", padx=20, pady=30) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_nombre_completo.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del numero de documento
etiqueta_nro_documento = Label(marco, text="N° de documento:")
etiqueta_nro_documento.grid(row=2, column=0, sticky="w", padx=20, pady=30) 
etiqueta_nro_documento.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del correo electronico
etiqueta_correo_electronico = Label(marco, text="Correo electrónico:")
etiqueta_correo_electronico.grid(row=3, column=0, sticky="w", padx=20, pady=30)
etiqueta_correo_electronico.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del boton de opcion
etiqueta_nivel_estudios = Label(marco, text = "*** NIVEL DE ESTUDIOS ***")
etiqueta_nivel_estudios.grid(row=0,column=2,sticky="w",padx=10,pady=10)
etiqueta_nivel_estudios.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
# Etiqueta de la casilla de verificacion
etiqueta_preferencias_contacto = Label(marco, text = "** PREFERENCIAS DE CONTACTO **")
etiqueta_preferencias_contacto.grid(row=0,column=3,sticky="w",padx=10,pady=10)
etiqueta_preferencias_contacto.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))
"""
INGRESOS
"""
# Declaro el tipo de dato de los Entry (IntVar para enteros y StringVar para texto).
nombre_completo=StringVar()
nro_documento=IntVar()
correo_electronico=StringVar()
# Ingreso del nombre completo
ingreso_nombre_completo = Entry(marco, textvariable=nombre_completo)
ingreso_nombre_completo.grid(row=1, column=1, sticky="w", padx=10, pady=10)
ingreso_nombre_completo.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del nnumero de documento
ingreso_nro_documento = Entry(marco, textvariable=nro_documento)
ingreso_nro_documento.grid(row=2, column=1, sticky="w", padx=10,pady=10)
ingreso_nro_documento.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del correo electronico
ingreso_correo_electronico = Entry(marco, textvariable=correo_electronico)
ingreso_correo_electronico.grid(row=3, column=1, sticky="w", padx=10, pady=10)
ingreso_correo_electronico.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))

""" 
BOTONES DE ACCION
"""
# Boton de registrar alumno.
boton_registrar = Button(marco, text="Registrar", command=lambda:registrar())
boton_registrar.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="we")
boton_registrar.config(fg = "green", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Boton de cancelar inscripción.
boton_cancelar = Button(marco, text="Cancelar", command=lambda:cancelar())
boton_cancelar.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="we")
boton_cancelar.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))
# Boton de salir de la app.
boton_salir = Button(marco, text="Salir", command=lambda:salida())
boton_salir.grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky="we")
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))

"""
BOTONES DE OPCION
"""
# Funcionalidad del boton de opcion
nivel_estudios=IntVar()
# Opcion de primario completo
primario_completo=Radiobutton(marco, text="Primario COMPLETO", variable=nivel_estudios, value=1)
primario_completo.grid(row=1, column=2, sticky="w", padx=10, pady=10)
primario_completo.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de secundario completo
secundario_completo=Radiobutton(marco, text="Secundaro COMPLETO", variable=nivel_estudios, value=2)
secundario_completo.grid(row=2, column=2, sticky="w", padx=10, pady=10)
secundario_completo.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Opcion de terciario completo
terciario_completo=Radiobutton(marco, text="Terciario COMPLETO", variable=nivel_estudios, value=3)
terciario_completo.grid(row=3, column=2, sticky="w", padx=10, pady=10)
terciario_completo.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
CASILLAS DE VERIFICACION
"""
# Son TRES porque son INDEPENDIENTES
email=IntVar()
whatsapp=IntVar()
encuesta=IntVar()
# EMAIL
check_email = Checkbutton(marco, text="e-mail", variable=email, onvalue=1, offvalue=0)
check_email.grid(row=1,column=3,sticky="w",padx=10,pady=10)
check_email.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# WHATSAPP
check_whatsapp = Checkbutton(marco, text="WhatsApp", variable=whatsapp, onvalue=1, offvalue=0)
check_whatsapp.grid(row=2,column=3,sticky="w",padx=10,pady=10)
check_whatsapp.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# ENCUESTA
check_encuesta = Checkbutton(marco, text="Encuesta", variable=encuesta, onvalue=1, offvalue=0)
check_encuesta.grid(row=3,column=3,sticky="w",padx=10,pady=10)
check_encuesta.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

# Mantengo la ventana abierta para que no se cierre hasta que yo le diga.
raiz.mainloop()