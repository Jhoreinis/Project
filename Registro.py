class Registro:
    
    def __init__(self, usuario: str, contraseña: str): 
        self.usuario = usuario
        self.contraseña = contraseña
        self.conectar = False
        self.intento = 3  

    def registrar(self, usuario: str, contraseña: str) -> bool:
        with open("registro_usuario.txt", "w") as archv:
            registro = usuario + "," + contraseña + "\n"
            archv.write(registro)
            #archv.close()
        
    def inisioSesion(self, usuario: str, contraseña: str) -> bool:
        archv = open("registro_usuario.txt", "w")
        archv.read()
        for linea in archv:
            user, contra = linea.split(",")
            if user == usuario and int (contra) == contraseña:
                print ("Ha iniciado sesión con exito")
                self.conectar = True    
            elif self.intento > 0:
                self.intento-=1
                print ("Contraseña o nombre de usuario incorrectos, intentelo nuevamente")
                self.inisioSesion()
            else:
                print ("no se pudo iniciar sesión, excedio numero de intentos")
        return True






    
    
    
