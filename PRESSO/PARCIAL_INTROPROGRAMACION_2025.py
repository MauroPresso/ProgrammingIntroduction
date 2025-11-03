#IMPORTAR
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from clasePersonal import Personal

# Funcion para determinar la modalidad en texto
def modalidad_texto(valor):
    if valor == 1:
        return "Virtual"
    elif valor == 2:
        return "Presencial"
    else:
        return "Mixta"
# Funcion para determinar la modalidad en valor numerico
def modalidad_valor(texto):
    if texto == "Virtual":
        return 1
    elif texto == "Presencial":
        return 2
    else:
        return 3
    
#PRINCIPAL
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="lightblue")
raiz.title("** TITULO - PRESSO, MAURO **")
# Icono
try:
    raiz.iconbitmap('Hello.ico')
except Exception:
    pass
raiz.config(bg = "blue") # bg: background (color de fondo).
raiz.config(cursor = "target") # cursor: es el iconito del mouse.

#MARCO
marco=Frame(raiz,width="650",height="350")
marco.pack(fill="none",expand="False")
marco.config(bg = "green", relief= "raised")
titulo=Label(marco,text=" ** ALTA CAPACITACIONES -  **")
titulo.grid(row=0,column=0,columnspan=6,pady=15,padx=15)
titulo.config(width=40,font=("Rockwel",15,"bold"),anchor="center")

#FUNCIONALIDAD A LOS BOTONES // FUNCIONES

def limpiar():
    # Entrys
    nombre.set("")
    apellido.set("")
    email.set("")
    capacitacion.set("")
    # Radiobuttons
    modalidad.set(1) # Valor por defecto
    # Foco en el primer entry
    txtnom.focus()

def hab_desh(estado):
    # Entrys
    txtnom.config(state=estado)
    txtape.config(state=estado)
    txtmail.config(state=estado)
    txtcap.config(state=estado)
    # Radiobuttons
    modalidad1.config(state=estado)
    modalidad2.config(state=estado)
    modalidad3.config(state=estado)

def nuevo():
    global registroNuevo
    registroNuevo=True
    messagebox.showwarning("ATENCIÓN", "Está por ingresar un nuevo registro")
    # Entrys
    limpiar()
    txtnom.focus() #nombre del entry
    # deshabilito Entrys
    hab_desh("normal")
    # Buttons
    botonnuevo.config(state="disabled")
    botonmodi.config(state="disabled")
    botonborrar.config(state="disabled")
    botoncan.config(state="normal")
    botonconf.config(state="normal")

def cancelar():
    messagebox.showwarning("ATENCIÓN", "Está por cancelar esta operación.")
    # Entrys
    txtnom.focus() #nombre del entry
    # limpio los campos
    limpiar()
    # deshabilito Entrys
    hab_desh("disabled")
    # Buttons
    botonnuevo.config(state="normal")
    botonmodi.config(state="normal")
    botonborrar.config(state="normal")
    botoncan.config(state="disabled")
    botonconf.config(state="disabled")

def guardar():
    condicion_nombre = (nombre.get() == "")
    condicion_apellido = (apellido.get() == "")
    condicion_email = (email.get() == "")
    condicion_capacitacion = (capacitacion.get() == "")
    if condicion_nombre or condicion_apellido or condicion_email or condicion_capacitacion:
        if condicion_nombre:
            messagebox.showerror("ERROR", "Por favor, ingresa tu nombre.")
        elif condicion_apellido:
            messagebox.showerror("ERROR", "Por favor, ingresa tu apellido.")
        elif condicion_email:
            messagebox.showerror("ERROR", "Por favor, ingresa tu email.")
        else:
            messagebox.showerror("ERROR", "Por favor, ingresa la capacitación.")
    else:
        global registroNuevo
        if messagebox.askquestion("GUARDAR Inscripción", "Confirmar que desea guardar la inscripción") == "yes":
            if registroNuevo==True:
                miCapacitacion = Personal(nombre=nombre.get(), apellido=apellido.get(), email=email.get(), capacitacion=capacitacion.get(), modalidad=modalidad_texto(modalidad.get()))
                miCapacitacion.Agregar()
                messagebox.showinfo("GUARDAR Inscripción", "La inscripción ha sido agregada")
            else:
                miCapacitacion = Personal(id=int(lista.item(lista.selection())['text']), nombre=nombre.get(), apellido=apellido.get(), email=email.get(), capacitacion=capacitacion.get(), modalidad=modalidad_texto(modalidad.get()))
                miCapacitacion.Modificar()
                messagebox.showinfo("GUARDAR Inscripción", "La inscripción ha sido modificada")
            # limpio los campos
            llenar_lista()
            limpiar()
            hab_desh("disabled")
        else:
            messagebox.showinfo("GUARDAR Inscripción", "La inscripción NO ha sido guardada")
            limpiar()
        # Buttons
        botonnuevo.config(state="normal")
        botonmodi.config(state="normal")
        botonborrar.config(state="normal")
        botoncan.config(state="disabled")
        botonconf.config(state="disabled")

def modificar():
    global registroNuevo
    registroNuevo=False
    try:
        limpiar()
        hab_desh("normal")
        # Cargo los valores en los entrys
        nombre.set(lista.item(lista.selection())['values'][0])
        apellido.set(lista.item(lista.selection())['values'][1])
        email.set(lista.item(lista.selection())['values'][2])
        capacitacion.set((lista.item(lista.selection())['values'][3]))
        modalidad.set(modalidad_valor(lista.item(lista.selection())['values'][4]))
        # Buttons
        botonconf.config(state="normal")
        botoncan.config(state="normal")
        botonnuevo.config(state="disabled")
        botonborrar.config(state="disabled")
        botonmodi.config(state="disabled")
    except:
        messagebox.showerror("ERROR", "Debe seleccionar un registro para modificar.")
        hab_desh("disabled")
        botonconf.config(state="disabled")
        botoncan.config(state="disabled")
        botonnuevo.config(state="normal")
        botonborrar.config(state="normal")
        botonmodi.config(state="normal")

def eliminar():
    try:
        miCapacitacion = Personal(id=int(lista.item(lista.selection())['text']))
        if messagebox.askquestion("ELIMINAR INSCRIPCIÓN","Confirmar que desea eliminar la inscripción")=="yes":
            miCapacitacion.Eliminar()
            limpiar()
            hab_desh("disabled")
            llenar_lista()
        else:
            messagebox.showinfo("ELIMINAR INSCRIPCIÓN","La inscripción NO ha sido eliminada")
    except:
        messagebox.showerror("ERROR", "Debe seleccionar un registro para eliminar.")


def salir():
    respuesta = messagebox.askquestion("SALIDA DE LA APP", "Confirmar que sale de la apicacion")
    if respuesta=="yes":
        raiz.destroy() # cuando destroy lo vinculas a command no se pone parentesis. En este caso, si.
    else:
        messagebox.showinfo("SALIDA DE LA APP", "Aun sigues aqui, gracias por quedarte!")

def vaciar_lista():
    registros=lista.get_children()
    for r in registros:
        lista.delete(r)

def llenar_lista():
    botonnuevo.config(state="normal")
    botonmodi.config(state="normal")
    botonborrar.config(state="normal")
    vaciar_lista()
    registros=Personal.ListaCapacitaciones()
    for r in registros:
        #              VINC.C/CAMPO0(ID) VALORES(OTROS CAMPOS)               
        lista.insert('', 0, text=r[0], values=(r[1], r[2], r[3], r[4], r[5]))




#ETIQUETAS - INGRESO DE DATOS

labnom=Label(marco,text="Nombre ")
labnom.grid(row=1,column=0,sticky="w",pady=15,padx=15)
labnom.config(width=20,font=("Rockwell",10,"bold"),anchor="w")

labape=Label(marco,text="Apellido ")
labape.grid(row=1,column=2,sticky="w",pady=15,padx=15)
labape.config(width=20,font=("Rockwell",10,"bold"),anchor="w")

labmail=Label(marco,text="E-mail ")
labmail.grid(row=1,column=4,sticky="w",pady=15,padx=15)
labmail.config(width=20,font=("Rockwell",10,"bold"),anchor="w")

labcap=Label(marco,text="Capacitación")
labcap.grid(row=2,column=0,sticky="w",pady=5,padx=15)
labcap.config(width=20,font=("Rockwell",10,"bold"),anchor="w")

labmod=Label(marco,text="Modalidad")
labmod.grid(row=2,column=2,sticky="w",pady=5,padx=15)
labmod.config(width=20,font=("Rockwell",10,"bold"),anchor="w")

lableyenda=Label(marco,text="Aplicación creada por Presso - Mauro © 2025")
lableyenda.grid(row=10,column=0,columnspan=4,sticky=" ",pady=15,padx=15)
lableyenda.config(width=40,font=("Rockwell",8,"italic"),anchor="w")


#VARIABLES PARA LOS ENTRYS
nombre=StringVar()
apellido=StringVar()
email=StringVar()
capacitacion=StringVar()


#ENTRYS
txtnom=Entry(marco,textvariable=nombre)
txtnom.grid(row=1,column=1,sticky="w",pady=15,padx=5)
txtnom.config(width=30,font=("Arial",10),justify="left")

txtape=Entry(marco,textvariable=apellido)
txtape.grid(row=1,column=3,sticky="w",pady=15,padx=5)
txtape.config(width=30,font=("Arial",10),justify="left")

txtmail=Entry(marco,textvariable=email)
txtmail.grid(row=1,column=5,sticky="w",pady=15,padx=5)
txtmail.config(width=30,font=("Arial",10),justify="left")

txtcap=Entry(marco,textvariable=capacitacion)
txtcap.grid(row=2, column=1,sticky="w",pady=15,padx=5)
txtcap.config(width=30,font=("Arial",10),justify="left")

#BOTONES DE OPCION DE MODALIDAD
modalidad=IntVar()

modalidad1=Radiobutton(marco,text="Virtual", variable=modalidad, value=1)
modalidad1.grid(row=2,column=3,sticky="w",padx=5,pady=5)

modalidad2=Radiobutton(marco,text="Presencial", variable=modalidad,value=2)
modalidad2.grid(row=2,column=4,sticky="w",padx=5,pady=5)

modalidad3=Radiobutton(marco,text="Mixta", variable=modalidad,value=3)
modalidad3.grid(row=2,column=5,sticky="w",padx=5,pady=5)



#BOTONES
botonnuevo=Button(marco,text="NUEVO",command=lambda:nuevo())
botonnuevo.grid(row=8,column=0)
botonnuevo.config(bg="green",fg="white", state="normal")

botoncan=Button(marco,text="CANCELAR",command=lambda:cancelar())
botoncan.grid(row=8,column=1)
botoncan.config(bg="red",fg="white", state="disabled")

botonconf=Button(marco,text="GUARDAR",command=lambda:guardar())
botonconf.grid(row=8,column=2)
botonconf.config(bg="green",fg="white", state="disabled")

botonmodi=Button(marco,text="MODIFICAR ",command=lambda:modificar())
botonmodi.grid(row=8, column=3)
botonmodi.config(bg="orange",fg="black", state="normal")

botonborrar=Button(marco, text="ELIMINAR", command=lambda:eliminar())
botonborrar.grid(row=8,column=4)
botonborrar.config(bg="red",fg="white", state="normal")

botonsal=Button(marco,text="SALIR",command=lambda:salir())
botonsal.grid(row=8,column=5)
botonsal.config(bg="red",fg="white", state="normal")

#CREAMOS EL TREEVIEW Y CANTIDAD DE COLUMNAS

lista=ttk.Treeview(marco,columns=('Nom','Ape','Mail','Capacitación','Modal'))
lista.grid(row=7,column=1,columnspan=6,sticky="w")
# Scrollbar
barraDespl=ttk.Scrollbar(marco, orient=VERTICAL, command=lista.yview)
barraDespl.grid(row=7, column=4, sticky="ns")
lista.configure(yscrollcommand=barraDespl.set)

lista.heading('#0',text='ID')
lista.column('#0',width=50)
lista.heading('#1',text='Nombre')
lista.column('#1',width=100)
lista.heading('#2',text='Apellido')
lista.column('#2',width=100)
lista.heading('#3',text='Email')
lista.column('#3',width=100)
lista.heading('#4',text='Capacitación')
lista.column('#4',width=150)
lista.heading('#5',text='Modalidad')
lista.column('#5',width=100)

llenar_lista()

raiz.mainloop()

