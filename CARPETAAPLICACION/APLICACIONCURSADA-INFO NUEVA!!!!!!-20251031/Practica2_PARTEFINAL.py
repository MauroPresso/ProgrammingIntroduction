# IMPORTAR
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from claseAlumnos import Alumnos

#VENTANA RAIZ
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="lightblue")
raiz.title("** SISTEMA EDUCATIVO  - Laura Vidal **")
raiz.config(cursor="star")
#raiz.iconbitmap('Software.ico')

#MARCO
marco=Frame(raiz,bg="pink",width="650",height="350")
marco.pack(fill="none",expand="False")

titulo=Label(marco,text=" ** CARGA DE ALUMNOS **")
titulo.grid(row=0,column=0,columnspan=3,pady=15,padx=15)
titulo.config(bg="pink",width=40,font=("Rockwel",15,"bold"),anchor="center")

#ETIQUETAS - INGRESO DE DATOS
labnom=Label(marco,text="Nombre ")
labnom.grid(row=1,column=0,sticky=" ",pady=15,padx=15)
labnom.config(bg="lightblue",width=15,font=("Rockwell",12,"bold"),anchor="w")

labdom=Label(marco,text="Domicilio ")
labdom.grid(row=2,column=0,sticky=" ",pady=15,padx=15)
labdom.config(bg="lightblue",width=15,font=("Rockwell",12,"bold"),anchor="w")

labdni=Label(marco,text="D.N.I ")
labdni.grid(row=3,column=0,sticky=" ",pady=15,padx=15)
labdni.config(bg="lightblue",width=15,font=("Rockwell",12,"bold"),anchor="w")

labedad=Label(marco,text="Edad ")
labedad.grid(row=4,column=0,sticky=" ",pady=15,padx=15)
labedad.config(bg="lightblue",width=15,font=("Rockwell",12,"bold"),anchor="w")

#VARIABLES PARA LOS ENTRYS
Nombre=StringVar() #StringVar hace referencia a una variable de tipo string
Domicilio=StringVar() 
Dni=IntVar()
Edad=IntVar()

#ENTRYS
txtnom=Entry(marco,textvariable=Nombre)
txtnom.grid(row=1,column=1,columnspan=2,stick="w",padx=15,pady=15)
txtnom.config(bg="white",width=40,font=("rockwell",12),state="disabled")

txtdom=Entry(marco,textvariable=Domicilio)
txtdom.grid(row=2,column=1,columnspan=2,stick="w",padx=15,pady=15)
txtdom.config(bg="white",width=40,font=("rockwell",12),state="disabled")

txtdni=Entry(marco,textvariable=Dni)
txtdni.grid(row=3,column=1,columnspan=2,stick="w",padx=15,pady=15)
txtdni.config(bg="white",width=40,font=("rockwell",12),state="disabled")

txted=Entry(marco,textvariable=Edad)
txted.grid(row=4,column=1,columnspan=2,stick="w",padx=15,pady=15)
txted.config(bg="white",width=40,font=("rockwell",12),state="disabled")

#FUNCIONALIDAD A LOS BOTONES
def Guardar():
    #Mensaje de error por dato mal ingresado
    if Nombre.get()=="" or Domicilio.get()=="" or Dni.get()=="" or Edad.get()==0:
       messagebox.showerror("*ERROR*","Alguno de los datos es erróneo")
    else:
        global esNuevo
        if esNuevo==True: #la variable está en TRUE porque presione el boton NUEVO
            miAlumno=Alumnos(0,Nombre.get(),Domicilio.get(),Dni.get(),Edad.get())
            miAlumno.Agregar()
            limpiar()
            estadotextos("disabled")
            botonconf.config(state="disabled")
            botonnuevo.config(state="normal")
            botoncan.config(state="disabled")
            llenar_Tv()
        else: #la variable está en False porque presione el botón EDITAR
            #tomo los datos del entry que ya modifiqué y voy a guardar esa modificación
            miAlumno=Alumnos(Tv.item(Tv.selection())['text'],Nombre.get(),Domicilio.get(),Dni.get(),Edad.get())
            miAlumno.Modificar()
            limpiar()
            estadotextos("disabled")
            botonconf.config(state="disabled")
            botonnuevo.config(state="normal")
            botoncan.config(state="disabled")
            llenar_Tv()

    #LLAMO A LA FUNCIÓN LIMPIAR
    limpiar()
    
    #Función estadodetextos
    estadotextos("disabled")

    #Habilito/Deshabilito los botones
    botonconf.config(state="disabled")
    botonnuevo.config(state="normal")
    botoncan.config(state="normal")


def Cancelo():
   
    limpiar()
        
    #Función estadodetextos
    estadotextos("disabled")
    
    #Habilito/Deshabilito los botones
    botonconf.config(state="disabled")
    botonnuevo.config(state="normal")
    botoncan.config(state="disabled")

    messagebox.showwarning("Atención","Se cancela la carga")

def Nuevo():
      
    #creo la variable global
    global esNuevo
    esNuevo=True
    #LLAMO A LA FUNCIÓN LIMPIAR
    limpiar()
    
    #Función estadodetextos
    estadotextos("normal")

    
    #Habiito/deshabilito los botones
    botonconf.config(state="normal")
    botonnuevo.config(state="disabled")
    botoncan.config(state="normal")

    #Pongo el foco en txtnom
    txtnom.focus()

    messagebox.showwarning("*ATENCIÓN","Está por ingresar nuevos datos")

def limpiar():
    #Poner en blanco los 4 Entry
    Nombre.set("")
    Domicilio.set("")
    Dni.set(0)
    Edad.set(0) 

def estadotextos(estado):
    txtnom.config(state=estado)
    txtdom.config(state=estado)
    txtdni.config(state=estado)
    txted.config(state=estado)

def editar():
    #pass
    # por que? en false porque no es un registro nuevo, sino 
    #la modificación de un registro existente
    global esNuevo
    esNuevo=False
    try:
        limpiar()
        estadotextos("normal")
        botonconf.config(state="normal")
        botonnuevo.config(state="disabled")
        botoncan.config(state="normal")

        #el ID no pasa a ningun entry porque no hay entry de ID
        #pasar a los entry lo que seleccioné en el tv
        Nombre.set(Tv.item(Tv.selection())['values'][0])
        Domicilio.set(Tv.item(Tv.selection())['values'][1])
        Dni.set(Tv.item(Tv.selection())['values'][2])
        Edad.set(Tv.item(Tv.selection())['values'][3])
    
        txtnom.focus()
    except:
        messagebox.showerror("EDITAR","No se ha seleccionado ningun registro") 
           
def eliminar():
    #pass
    miAlumno=Alumnos(Tv.item(Tv.selection())['text'])
    miAlumno.Eliminar()
    limpiar()
    estadotextos("disabled")
    botonconf.config(state="disabled")
    botonnuevo.config(state="normal")
    botoncan.config(state="disabled")
    #al tener un elemento menos en la tabla.. se debe llenar el TreeView
    llenar_Tv()

def Salir():
    res=messagebox.askquestion("*SALIR*","Confirma que desea salir del programa?")
    if res=="yes":
        raiz.destroy()
    


#BOTONES
botonnuevo=Button(marco,text="NUEVO",command=lambda:Nuevo())
botonnuevo.grid(row=5,column=0,pady=15,padx=15)
botonnuevo.config(fg="white",bg="green",width=15,font=("Rockwell",13))

botonconf=Button(marco,text="GUARDAR",command=lambda:Guardar())
botonconf.grid(row=5,column=1,pady=15,padx=15)
botonconf.config(fg="white",bg="blue",width=15,font=("Rockwell",13),state="disabled")

botoncan=Button(marco,text="CANCELAR",command=lambda:Cancelo())
botoncan.grid(row=5,column=2,pady=15,padx=15)
botoncan.config(fg="white",bg="red",width=15,font=("Rockwell",13),state="disabled")

botoneditar=Button(marco,text="EDITAR",command=lambda:editar())
botoneditar.grid(row=7,column=0,pady=15,padx=15)
botoneditar.config(width=20,font=("Rockwell",13),state="disabled",fg="#FFFFFF",bg="#126b14",cursor="hand2",activebackground='#5EB060')

botonelim=Button(marco,text="ELIMINAR",command=lambda:eliminar())
botonelim.grid(row=7,column=1,pady=15,padx=15)
botonelim.config(width=15,font=("Rockwell",13),state="disabled",fg="#FFFFFF",bg="#CA250C")

botonsal=Button(marco,text="SALIR",command=lambda:Salir())
botonsal.grid(row=8,column=0,columnspan=3,pady=15,padx=15)
botonsal.config(width=40,font=("Rockwell",13))

#BLANQUEAR EL TREEVIEW
def vaciar_Tv():
    botoneditar.config(state="normal")
    botonelim.config(state="normal")
    #get_children es como que cada renglon es como un hijo en la grilla
    #en filas tengo la cantidad de filas
    filas=Tv.get_children()
    #recorro todas las filas de la grilla. 
    for f in filas:
        Tv.delete(f)
        #Se borra una por una

#PONE LOS DATOS DE LA TABLE ALUMNOS EN LA GRILLA
def llenar_Tv():
    botoneditar.config(state="normal")
    botonelim.config(state="normal")
    #función que me permite blanquear el tv
    vaciar_Tv()
    #en datos tengo el resultado de todos los registros
    #llamo al método listaAlumnos - (Select * from....)
    datos=Alumnos.listaAlumno()
    for d in datos:
        #A la primer columna la llama text al resto los traigo con values
        Tv.insert('',0,text=d[0],values=(d[1],d[2],d[3],d[4]))
        #el elemento d[0] es el id
        #a través de values hago referencia al resto de los campos



#EL TREEVIEW NO FORMA PARTE DE LOS WIDGET COMUNES QUE TIENE PYTHON VAMOS A AGREGAR UNA LIBRERIA MAS
#from tkinter import ttk

#CREAMOS EL TREEVIEW Y CANTIDAD DE COLUMNAS
Tv=ttk.Treeview(marco,columns=('NomApe','Dom','Dni','Edad'))
#No hace falta incluir la primer columna (ID) porque ya viene incluida en el TV

#DEFINIR UBICACIÓN Y ANCHO DEL TV
Tv.grid(row=6,column=0,columnspan=4,sticky="w")
scroll=ttk.Scrollbar(marco,orient='vertical',command=Tv.yview)
scroll.grid(row=6,column=4,sticky='nse')
Tv.configure(yscrollcommand=scroll.set)
#DEFINIR NOMBRES DE COLUMNAS
#los nombres los defino con heading - Text sería el título
Tv.heading('#0',text='ID')
Tv.column('#0',width=50)
Tv.heading('#1',text='Nombre y Apellido')
Tv.column('#1',width=150)
Tv.heading('#2',text='Domicilio')
Tv.column('#2',width=150)
Tv.heading('#3',text='Dni')
Tv.column('#3',width=150)
Tv.heading('#4',text='Edad')
Tv.column('#4',width=100)
llenar_Tv()

raiz.mainloop()

