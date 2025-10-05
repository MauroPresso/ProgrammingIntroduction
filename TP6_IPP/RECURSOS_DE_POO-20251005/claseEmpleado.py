class Empleado():
    def __init__(self,categoria=0, antiguedad=0,sueldo=0):
        self.categoria=categoria
        self.antiguedad=antiguedad
        self.sueldo=sueldo
    def Actualizarsueldo(self):
        print("Se actualizó el sueldo del empleado ",self.nombre," con una antiguedad de ",self.antiguedad)
    def ActualizarCategoria(self):
        print("Se actualizó la categoria del empleado ",self.nombre," con una antiguedad de ",self.antiguedad)
   