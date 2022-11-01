class Registro:
    numUsuarios = 0
    
    def __init__(self, nombre, contraseña ) -> None:
        self.nombre = nombre
        self.contraseña = contraseña
        
        self.conectar = False
        self.intento = 3
        
        
        Registro.numUsuarios+=1

    def login(self):
        nombreUsuario = input("Ingrese nombre de usuario:")
        contraseñaUsuario = input("Ingrese contraseña:")
        if contraseñaUsuario == self.contraseña and nombreUsuario == self.nombre:
            print ("Ha iniciado sesión con exito")
            self.conectar = True
        else:
            self.intento-=1
            if self.intento > 0:
              print ("Contraseña o nombre de usuario incorrectos, intentelo nuevamente")
              self.login()
            else:
              print ("no se pudo iniciar sesión, excedio numero de intentos")

            
    def close(self):
        if self.conectar:
            print("cerro sesión con exito")
            self.conectar = False
            
user = Registro(input("Registre nombre de usuario"), input("Crea una contraseña"))
print(user)

user.login()
print(user)







    
    
    