# @file: calculoDeSumatoria.pyw
# @brief: Programa que calcula la sumatoria de tres valores ingresados por el usuario.
# @author: Mauro Presso
# @date: 2025-09-02
# @details: TP3 - Introducción a la Programación - IFES.

from tkinter import *
from tkinter import messagebox

"""
 @brief: Funcion que calcula la sumatoria de tres valores ingresados por el usuario.
 @param: No recibe parametros.
 @return: No devuelve nada.
 @details: Si el usuario es cliente se le aplica un descuento del 10%. Si no es cliente se le aplica un recargo del 20%.
"""

def Calcular():
    if valor1.get()>10000 or valor2.get()>10000 or valor3.get()>10000:
        messagebox.showerror("ERROR", "Una de las compras supera los $10000")
    else:
        suma = valor1.get() + valor2.get() + valor3.get() # .get()
        if es_cliente.get()==1:
            suma=suma*0.9
        else:
            suma=suma*1.20

        if flete.get()==1:
            suma=suma*1.1
        if garantia.get()==1:
            suma=suma*1.15
    total.set(suma) # .set()
    messagebox.showinfo("CONFIRMACION", "Compra finalizada!!")

"""
 @brief: Funcion que reinicia todos los campos del formulario.
 @param: No recibe parametros.
 @return: No devuelve nada.
 @details: Muestra un cartel de advertencia al usuario."""
def Nuevo():
    valor1.set(0)
    valor2.set(0)
    valor3.set(0)
    total.set(0)
    flete.set(0)
    garantia.set(0)
    es_cliente.set(1)
    messagebox.showwarning("ATENCIÓN", "Está por empezar una nueva compra")

"""
 @brief: Funcion que cierra la aplicacion.      
 @param: No recibe parametros.
 @return: No devuelve nada.
 @details: Muestra un cartel de confirmacion al usuario.
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
raiz.title("**** CALCULO DE SUMATORIA ****")
raiz.geometry("480x300")
raiz.minsize(420, 260)


# Tamaño de la ventana
raiz.resizable(True, True) # Con resizable(True, True) ambos bordes de la ventana raiz son expansibles. Es lo que pasa ya por defecto.
#raiz.resizable(False, True) # Con resizable(False, True) la ventana se expande SOLAMENTE en ALTURA.
#raiz.resizable(True, False) # Con resizable(True, False) la ventana se expande SOLAMENTE en ANCHURA.
#raiz.resizable(False, False) # Con resizable(False, False) la ventana NO es expansible.

# Icono
try:
    raiz.iconbitmap('TP3_IPP\\CARPETA_DE_ICONOS_amp_PUNTEROS_20250825\\Software.ico')
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
cartel=Label(marco,text="** SUMATORIA DE NÚMEROS **")
cartel.grid(row=0,column=0,sticky="w",pady=10,padx=10)
cartel.config(fg="blue",bg="lightblue")

# Etiqueta del valor UNO.
etiqueta_valor_uno = Label(marco, text="Ingrese valor UNO:")
etiqueta_valor_uno.grid(row=1, column=0, sticky="w", padx=20, pady=30) # .grid() para acomodar el objeto dentro del Frame.
etiqueta_valor_uno.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del valor DOS.
etiqueta_valor_dos = Label(marco, text="Ingrese valor DOS:")
etiqueta_valor_dos.grid(row=2, column=0, sticky="w", padx=20, pady=30) 
etiqueta_valor_dos.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del valor TRES.
etiqueta_valor_tres = Label(marco, text="Ingrese valor TRES:")
etiqueta_valor_tres.grid(row=3, column=0, sticky="w", padx=20, pady=30)
etiqueta_valor_tres.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")
# Etiqueta del TOTAL.
etiqueta_TOTAL = Label(marco, text="TOTAL:")
etiqueta_TOTAL.grid(row=4, column=0, sticky="w", padx=20, pady=30)
etiqueta_TOTAL.config(fg = "blue", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

# Declaro el tipo de dato de los Entry (IntVar para enteros y StringVar para texto).
valor1=IntVar()
valor2=IntVar()
valor3=IntVar()
total=IntVar()

# Ingreso del valor UNO.
ingreso_valor_uno = Entry(marco, textvariable=valor1) #Con  textvariable la vinculo con valor1
ingreso_valor_uno.grid(row=1, column=1, sticky="w", pady=30)
ingreso_valor_uno.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del valor DOS.
ingreso_valor_dos = Entry(marco, textvariable=valor2)
ingreso_valor_dos.grid(row=2, column=1, sticky="w", pady=30)
ingreso_valor_dos.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del valor TRES.
ingreso_valor_tres = Entry(marco, textvariable=valor3)
ingreso_valor_tres.grid(row=3, column=1, sticky="w", pady=30)
ingreso_valor_tres.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))
# Ingreso del valor TOTAL.
ingreso_TOTAL = Entry(marco, textvariable=total)
ingreso_TOTAL.grid(row=4, column=1, sticky="w", pady=30)
ingreso_TOTAL.config(fg = "red", bg = "white", width = 30, font = ("Arial", 14, "italic"))

"""
Termino a ingresar las cosas que me piden
"""

"""
Boton de confirmar ingreso.
"""
boton_confirmar = Button(marco, text="CONFIRMAR", command=lambda:Calcular()) # El lambda va a buscar la funcion.
boton_confirmar.grid(row=5, column=0, columnspan=2, pady=10)
boton_confirmar.config(fg = "green", bg = "white", width = 30, font = ("Arial", 14, "italic"))

"""
Boton de nueva suma.
"""
boton_nueva_suma = Button(marco, text="NUEVA SUMA", command=lambda:Nuevo())
boton_nueva_suma.grid(row=6, column=0, columnspan=2, pady=10)
boton_nueva_suma.config(fg = "red", bg = "white", width = 30, font = ("Times New Roman", 14, "italic"))

"""
Boton de salir.
"""
boton_salir = Button(marco, text="Salir", command=lambda:salida()) # con el command se vincula y con el destroy efecivamente de destruye.
boton_salir.grid(row=7, column=0, columnspan=2, pady=10)
boton_salir.config(fg = "red", bg = "black", width = 30, font = ("Helvetica", 14, "italic"))


"""
CHECKBUTTON
"""
etiqueta_boton = Label(marco, text = "** SERVICIOS ESPECIALES **")
etiqueta_boton.grid(row=1,column=2,sticky="w",padx=10,pady=10)
etiqueta_boton.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))

# Son DOS porque son INDEPENDIENTES
flete=IntVar()
garantia=IntVar()

# Las casillas de verificacion
check_flete = Checkbutton(marco, text="Flete", variable=flete, onvalue=1, offvalue=0)
check_flete.grid(row=2,column=2,sticky="w",padx=10,pady=10)
check_flete.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

check_garantia = Checkbutton(marco, text="Garantia", variable=garantia, onvalue=1, offvalue=0)
check_garantia.grid(row=3,column=2,sticky="w",padx=10,pady=10)
check_garantia.config(fg = "black", bg = "white", width = 25, font = ("Comic Sans", 12, "bold"), anchor = "w")

"""
RADIOBUTTON
"""
# Etiqueta del boton de opcion.
etiqueta_cliente = Label(marco, text = "** ¿ES CLIENTE? **")
etiqueta_cliente.grid(row=1,column=3,sticky="w",padx=10,pady=10)
etiqueta_cliente.config(fg = "white", bg = "black", width = 30, font = ("Rockell", 14, "italic"))

# Funcionalidad del boton de opcion
es_cliente=IntVar()

si_es_cliente=Radiobutton(marco, text="SI es CLIENTE", variable=es_cliente, value=1)
si_es_cliente.grid(row=2, column=3, sticky="w", padx=10, pady=10)

no_es_cliente=Radiobutton(marco, text="NO es CLIENTE", variable=es_cliente, value=2)
no_es_cliente.grid(row=3, column=3, sticky="w", padx=10, pady=10)
# Mantengo la ventana abierta para que no se cierre hasta que yo le diga.
raiz.mainloop()