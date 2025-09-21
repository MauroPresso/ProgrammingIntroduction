from tkinter import * 
from tkinter import filedialog as FileDialog 
# No es necesario importar open desde io si usarás el open nativo de Python

ruta = "" # La utilizaremos para almacenar la ruta del fichero

def nuevo(): 
    global ruta
    mensaje.set("Nuevo fichero") 
    ruta = "" 
    texto.delete(1.0, "end") 
    root.title("Mi editor")

def abrir(): 
    global ruta 
    mensaje.set("Abrir fichero") 
    ruta = FileDialog.askopenfilename(initialdir='.', filetypes=(("Ficheros de texto", "*.txt"),), title="Abrir un fichero de texto")

    if ruta != "": 
        # Agregamos encoding='utf-8' para manejar caracteres especiales
        fichero = open(ruta, 'r', encoding='utf-8') 
        contenido = fichero.read() 
        texto.delete(1.0,'end') 
        texto.insert('insert', contenido) 
        fichero.close() 
        root.title(ruta + " - Mi editor")

def guardar(): 
    mensaje.set("Guardar fichero") 
    if ruta != "": 
        contenido = texto.get(1.0,'end-1c') 
        # Agregamos encoding='utf-8'
        fichero = open(ruta, 'w+', encoding='utf-8') 
        fichero.write(contenido) 
        fichero.close() 
        mensaje.set("Fichero guardado correctamente") 
    else: guardar_como() 

def guardar_como(): 
    global ruta 
    mensaje.set("Guardar fichero como") 
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt") 
    if fichero is not None: 
        ruta = fichero.name 
        contenido = texto.get(1.0,'end-1c') 
        # Cerramos primero el archivo que devolvió asksaveasfile
        fichero.close()
        # Abrimos de nuevo con la codificación correcta
        fichero = open(ruta, 'w+', encoding='utf-8') 
        fichero.write(contenido) 
        fichero.close() 
        mensaje.set("Fichero guardado correctamente") 
    else: 
        mensaje.set("Guardado cancelado")
        ruta = "" 
        
# Configuración de la raíz
root = Tk() 
root.title("Mi editor")

# Menú superior 
menubar = Menu(root) 
filemenu = Menu(menubar, tearoff=0) 
# Menu de archivo
filemenu.add_command(label="Nuevo", command=nuevo) 
filemenu.add_command(label="Abrir", command=abrir) 
filemenu.add_command(label="Guardar", command=guardar) 
filemenu.add_command(label="Guardar como", command=guardar_como) 
filemenu.add_separator() 
filemenu.add_command(label="Salir", command=root.quit) 
menubar.add_cascade(menu=filemenu, label="Archivo") 
# Caja de texto central 
texto = Text(root) 
texto.pack(fill="both", expand=1) 
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12)) 
# Monitor inferior 
mensaje = StringVar() 
mensaje.set("Bienvenido a tu Editor") 
monitor = Label(root, textvar=mensaje, justify='left') 
monitor.pack(side="left") 
root.config(menu=menubar) 
# Finalmente bucle de la apliación 
root.mainloop()