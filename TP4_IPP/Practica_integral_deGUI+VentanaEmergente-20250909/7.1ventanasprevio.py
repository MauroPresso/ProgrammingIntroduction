#Cómo manejar los datos con interfaz gráfica
from tkinter import *
#importar para trabajar con las ventanas emergentes
from tkinter import messagebox

#Creo la ventana Raiz
raiz=Tk()
raiz.resizable(True,True)
raiz.config(bg="pink")
raiz.title("** VENTANAS EMERGENTES **")
raiz.config(cursor="star")
#raiz.iconbitmap('Smile.ico')


#creamos el marco
marco=Frame(raiz,bg="lightblue",width="650",height="350")
marco.pack(fill="none",expand="True")

def informa():
    #ventana de información
    if minombre.get()=="":
        messagebox.showinfo("CONFIRMACION","Debes ingresar tu nombre")
    else:    
        messagebox.showinfo("CONFIRMACIÓN",minombre.get())

def advertir():
    #ventana de error 
    if minombre.get()=="":
        messagebox.showerror("ERROR","No ingresaste tu nombre")
    else:
        messagebox.showinfo("CONFIRMACIÓN","NOMBRE INGRESADO OK")    

def salida():        
#variable=messagebox.pregunta("titulo";"mensaje")
    respuesta=messagebox.askquestion("SALIR DE APLICACIÓN","Confirma que desea salir del programa")
    if respuesta=="yes":
        raiz.destroy()
    else:    
        messagebox.showinfo("SALIDA","AÚN SIGUES AQUI") 


#CREACIÓN DE ETIQUETAS
cartel=Label(marco,text="** MANEJO DE VENTANAS EMERGENTES **")
cartel.grid(row=0,column=0,sticky="w",pady=10,padx=10)

nom=Label(marco,text="Ingrese Su Nombre")
nom.grid(row=1,column=0,sticky="w",pady=10,padx=10)
nom.config(fg="black",bg="lightgrey",width=15,font=("Rockwell",13),anchor="w")

minombre=StringVar() # vincular el nombre

#Cómo asocio estas variables a los entry
nombre1=Entry(marco,textvariable=minombre)
nombre1.grid(row=1,column=1,sticky="w",pady=10,padx=10)
nombre1.config(fg="black",bg="lightblue",width=15,font=("Rockwell",13,"bold","italic"))

#CREACION DE BOTONES
infor=Button(marco,text="INFORMAR",command=lambda:informa())
infor.grid(row=4,column=0,padx=10,pady=10)
infor.config(fg="white",bg="blue",width=15,font=("Rockwell",14,"bold","italic"))

adver=Button(marco,text="ADVERTIR",command=lambda:advertir())
adver.grid(row=4,column=1,padx=10,pady=10)
adver.config(fg="white",bg="green",width=15,font=("Rockwell",14,"bold","italic"))

#Asocio a raiz.destroy que es para salir
#Destroy de la ventana raiz significa destruir esa ventana que es cerrar la ventana general
salir=Button(marco,text="SALIR",command=lambda:salida())
salir.grid(row=6,column=0,columnspan=2,padx=10,pady=10)
salir.config(fg="white",bg="red",width=40,font=("Rockwell",14,"bold","italic"))    
raiz.mainloop()