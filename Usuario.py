from Registro import Registro

class Usuario (Registro):
    def __init__(self, nombre, contraseña, intereses, edad) -> None:
        super()._init_(nombre, contraseña)
        self.intereses = intereses
        self.edad = edad
    
    def reseñar(self):
        pass

    def puntuar(self):
        pass