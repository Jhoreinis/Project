class Registro:
    
    def __init__(self, usuario: str, contraseña: str): 
        self.usuario = usuario
        self.contraseña = contraseña
        self.conectado = False
        self.intento = 3    
        
        
    def usuarioRegistrado(self):
        file = open("BaseRegistro.txt", "r")
        line = file.readlines()
        conta = 0
        for linea in line:
            user = linea.split(',')[0]
            if self.usuario == user:
                conta +=1 
        file.close()
        if conta >= 1:
            return False
        return True 
    
    def registrar(self):
        file = open("BaseRegistro.txt", "a")
        registro = (self.usuario + "," + self.contraseña)
        file.write(registro + "\n")
        print("Registro exitoso")
        file.close() 
    
    def verificarLogin(self):
        file = open("BaseRegistro.txt", "r")
        lines = file.readlines()
        for linea in lines:
            save_split = linea.split(',')
            user, contraseña, = save_split[0], save_split[1]
            if (self.usuario ==  user):
                return True
            if (self.contraseña == contraseña):
                return True
        file.close()
        if (self.usuario != user and self.contraseña != contraseña):
            return False
    
    def login(self):
        file = open("BaseRegistro.txt", "r")
        line = file.readlines()
        for linea in line:
            save_split = linea.split(',')
            user, contraseña, = save_split[0], save_split[1]
            if self.usuario == user or self.contraseña == contraseña:
                print("Ha iniciado sesion con exito")
                self.conectado = True
        file.close() 
    
    
    
