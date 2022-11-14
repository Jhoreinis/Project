class Registro:
    
    def __init__(self, usuario: str, contraseña: str): 
        self.usuario = usuario
        self.contraseña = contraseña
        self.conectado = False
        self.intento = 3    
        
        """
        Los atributos usuario y contraseña son 
        necesarios para que existan usuarios y 
        pasar como parametro a cada metodo
        """
        
    def usuarioRegistrado(self):
        """
        Se abre el archivo que contiene la informacion
        de cada usuario como lectura
        """
        file2 = open("BaseRegistro.txt", "r")
        lines2 = file2.readlines()
        """
        Se utiliza un contador para verificar 
        que el usuario ya existe.cada vez que encuentre un usuario
        que ya existe aumenta el contador
        """
        conta = 0
        for linea2 in lines2:
            user = linea2.split(',')[0]
            if self.usuario == user:
                conta +=1 
        file2.close()
        """
        Si el contador es mayor a 1
        quiere decir que ya hay un usuario registrado
        con ese nombre y retornara falso. si retorna False
        le pedirá al usuario que ingrese nuevamente un usuario diferente
        """
        if conta >= 1:
            return False
        return True 
    
    def registrar(self):
        
        """
        Cuando el contador de arriba retorne True el usuario 
        se ha registrado con exito y sus datos han sido guardados
        """
        
        file2 = open("BaseRegistro.txt", "a")
        registro = (self.usuario + "," + self.contraseña)
        file2.write(registro + "\n")
        print("Registro exitoso")
        file2.close() 
    
    def verificarLogin(self):
        
        """
        Abrimos nuevamente el archivo como lectura
        para verificar que el usuario haya ingresado
        correctamente los datos al momento de iniciar sesión
        """
        
        """
        Se utiliza split para poder separar y comparar 
        el usuario ingresado con el usuario anteriormente registrado
        asi mismo se hace con la contraseña. si retorna True la 
        información ingresada es correcta y el usuario podrá ingresar
        """
        
        file2 = open("BaseRegistro.txt", "r")
        lines2 = file2.readlines()
        for linea2 in lines2:
            save_split2 = linea2.split(',')
            user, contraseña, = save_split2[0], save_split2[1]
            if (self.usuario ==  user):
                return True
            if (self.contraseña == contraseña):
                return True
        file2.close()
        if (self.usuario != user and self.contraseña != contraseña):
            return False
    
    
    def login(self):
        
        """
        Luego de verificar anteriormente los datos 
        utilizamos este metodo para ingresar oficialmente
        al sistema.
        """
        
        file2 = open("BaseRegistro.txt", "r")
        lines2 = file2.readlines()
        for linea2 in lines2:
            save_split2 = linea2.split(',')
            user, contraseña, = save_split2[0], save_split2[1]
            if self.usuario == user or self.contraseña == contraseña:
                print("Ha iniciado sesion con exito")
                self.conectado = True
        file2.close() 
    
    
    
