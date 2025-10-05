from ejercicio2POOcreacionClaseHeader import Header

class Register(Header):
    def __init__(self, id=0, tipo="", info=""):
        Header.__init__(self, id, tipo, info)

    # Otros métodos de la clase
    def Agregar_Registro(self):
        print(f"Se agrego el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")
    def Modificar_Registro(self):
        print(f"Se modificó el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")
    def Eliminar_Registro(self):
        print(f"Se eliminó el Header del dispositivo:\n-ID: {self.id}\n-Tipo: {self.tipo}\n-Información: {self.info}")