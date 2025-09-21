# @file TP5_IPP/codigo_final_de_menus.py
# @brief Ejemplo de creación de menús en Tkinter
# @author Mauro Presso
# @date 2025-09-22
# @version 1.0
# @details Este código crea una ventana con una barra de menús que incluye opciones de archivo, edición y ayuda.

from tkinter import * 

# Crear la ventana principal
root = Tk() 
menubar = Menu(root) # Crear la barra de menú en la raíz
root.config(menu=menubar) # Configurar la raíz para que use la barra de menú
# Configuración del menú de archivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo") 
filemenu.add_command(label="Abrir") 
filemenu.add_command(label="Guardar") 
filemenu.add_command(label="Cerrar") 
filemenu.add_separator() 
filemenu.add_command(label="Salir", command=root.quit) 
# Configuración del menú de edición
editmenu = Menu(menubar, tearoff=0) 
editmenu.add_command(label="Cortar") 
editmenu.add_command(label="Copiar") 
editmenu.add_command(label="Pegar") 
# Configuración del menú de ayuda
helpmenu = Menu(menubar, tearoff=0) 
helpmenu.add_command(label="Ayuda") 
helpmenu.add_separator() 
helpmenu.add_command(label="Acerca de...")
# Agregar los menús a la barra de menú 
menubar.add_cascade(label="Archivo", menu=filemenu) 
menubar.add_cascade(label="Editar", menu=editmenu) 
menubar.add_cascade(label="Ayuda", menu=helpmenu)
# Finalmente bucle de la aplicación 
root.mainloop()