# @file TP5_IPP/codigo_final_text.py
# @brief Ejemplo de uso del widget Text de Tkinter
# @author Mauro Presso
# @date 2025-09-22
# @version 1.0
# @details Este código crea una ventana con un widget Text que permite ingresar y mostrar texto multilínea.

from tkinter import * 

# Configuración de la raíz 
root = Tk() 
texto = Text(root)
# El widget Text se crea y se asocia a la raíz
texto.pack() # El texto se agrega a la raíz
# Configuración del widget Text
texto.config(width=30, height=10, font=("Consolas",12), padx=15, pady=15, selectbackground="red") 
# Finalmente bucle de la aplicación 
root.mainloop()