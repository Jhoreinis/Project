class Registro:
    
    def __init__(self, usuario: str, contraseña: str): 
        self.usuario = usuario
        self.contraseña = contraseña
        self.conectar = False
        self.intento = 3  

    def registrar(self):
        file = open("BaseRegistro.txt", "a")
        registro = (self.usuario + "," + self.contraseña)
        self.usuarioRegistrado()
        file.write(registro + "\n")
        file.close()
      
    def usuarioRegistrado(self):
        file = open("BaseRegistro.txt", "r")
        line = file.readlines()
        for linea in line:
            user = linea.split(",")[0]
        file.close()
        if self.usuario == user:
            return False
        return True






    
    
    
