#IMPORTAR


#PRINCIPAL
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="lightblue")
raiz.title("** TITULO - APELLIDO Y NOMBRE **")

#MARCO
marco=Frame(raiz,width="650",height="350")
marco.pack(fill="none",expand="False")
titulo=Label(marco,text=" ** ALTA CAPACITACIONES -  **")
titulo.grid(row=0,column=0,columnspan=6,pady=15,padx=15)
titulo.config(width=40,font=("Rockwel",15,"bold"),anchor="center")

#FUNCIONALIDAD A LOS BOTONES // FUNCIONES

def limpiar():
    pass

def hab_desh():
    pass

def nuevo():
    pass

def cancelar():
    pass


def guardar():
    pass

def modificar():
    pass

def eliminar():
    pass


def salir():
    pass

def vaciar_lista():
    pass

def llenar_lista():
    pass




#ETIQUETAS - INGRESO DE DATOS

labnom=Label(marco,text="Nombre ")
labnom.grid(row=1,column=0,sticky="w",pady=15,padx=15)

labape=Label(marco,text="Apellido ")
labape.grid(row=1,column=2,sticky="w",pady=15,padx=15)

labmail=Label(marco,text="E-mail ")
labmail.grid(row=1,column=4,sticky="w",pady=15,padx=15)

labcap=Label(marco,text="Capacitación")
labcap.grid(row=2,column=0,sticky="w",pady=5,padx=15)

labmod=Label(marco,text="Modalidad")
labmod.grid(row=2,column=2,sticky="w",pady=5,padx=15)

lableyenda=Label(marco,text="Aplicación creada por Tu apellido y nombre")
lableyenda.grid(row=10,column=0,columnspan=4,sticky=" ",pady=15,padx=15)
lableyenda.config(width=40)


#VARIABLES PARA LOS ENTRYS


#ENTRYS
txtnom=Entry(marco)
txtnom.grid(row=1,column=1,sticky="w",pady=15,padx=5)

txtape=Entry(marco)
txtape.grid(row=1,column=3,sticky="w",pady=15,padx=5)

txtmail=Entry(marco)
txtmail.grid(row=1,column=5,sticky="w",pady=15,padx=5)

txtcap=Entry(marco)
txtcap.grid(row=2, column=1,sticky="w",pady=15,padx=5)



#BOTONES DE OPCION DE MODALIDAD

modalidad1=Radiobutton(marco,text="Virtual")
modalidad1.grid(row=2,column=3,sticky="w",padx=5,pady=5)

modalidad2=Radiobutton(marco,text="Presencial")
modalidad2.grid(row=2,column=4,sticky="w",padx=5,pady=5)

modalidad3=Radiobutton(marco,text="Mixta")
modalidad3.grid(row=2,column=5,sticky="w",padx=5,pady=5)



#BOTONES
botonnuevo=Button(marco,text="NUEVO",command=lambda:nuevo())
botonnuevo.grid(row=8,column=0)

botoncan=Button(marco,text="CANCELAR",command=lambda:cancelar())
botoncan.grid(row=8,column=1)

botonconf=Button(marco,text="GUARDAR",command=lambda:guardar())
botonconf.grid(row=8,column=2)

botonmodi=Button(marco,text="MODIFICAR ",command=lambda:modificar())
botonmodi.grid(row=8, column=3)

botonborrar=Button(marco, text="ELIMINAR")
botonborrar.grid(row=8,column=4)

botonsal=Button(marco,text="SALIR",command=lambda:salir())
botonsal.grid(row=8,column=5)

#CREAMOS EL TREEVIEW Y CANTIDAD DE COLUMNAS

lista=ttk.Treeview(marco,columns=('Nom','Ape','Mail','Capacitación','Modal'))
lista.grid(row=7,column=1,columnspan=6,sticky="w")

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



raiz.mainloop()

