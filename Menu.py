from Registro import Registro
from BuscarPelis import BuscarPelis
from InfoPelis import InfoPelis

class Menu:
    def __init__(self):
        
        pass
    
    def inicio(self):
        
        print("\t\t\t\t\033[1;34m"+ "BIENVENIDO" + "\033[0;m")
        print("\t\t\033[0;37m"+"1.Registrarse\n"  + "\033[0;m")
        print("\t\t\033[0;37m"+"2.Iniciar sesión\n"  + "\033[0;m")
        opcion1 = int(input ("\t\t\033[0;37m"+"¿Qué desea hacer?\n" + "\033[0;m\t\t"))
        while opcion1:
            while opcion1 != 1 and opcion1 !=2:
                print("\t\t\033[0;37m"+"Ingrese una opción correcta" + "\033[0;m\t\t")
                print("\t\t\033[0;37m"+"1.Registrarse\n"  + "\033[0;m")
                print("\t\t\033[0;37m"+"2.Iniciar sesión\n"  + "\033[0;m")
                opcion1 = int(input ("\t\t\033[0;37m"+"¿Qué desea hacer?\n" + "\033[0;m\t\t"))
            if opcion1 == 1:
                self.Registrarse()
                opcion1 = False
            else:
                self.inicioSesion()
                opcion1 = False
        
    def Registrarse(self):
 
        usuario = input("\t\t\033[0;37m"+"Cree un nombre de usuario:\n" + "\033[0;m\t\t")
        contraseña = input ("\t\t\033[0;37m"+"ingrese una contraseña:\n" + "\033[0;m\t\t")
        usuarios = Registro(usuario, contraseña)
        while Registro.usuarioRegistrado(usuarios) == False:
            print("\t\t\033[0;37m"+"Usuario ya se encuentra registrado"+ "\033[0;m\t\t")
            usuario = input("\t\t\033[0;37m"+"Cree un nombre de usuario:\n" + "\033[0;m\t\t")
            contraseña = input ("\t\t\033[0;37m"+"ingrese una contraseña:\n" + "\033[0;m\t\t")
            usuarios = Registro(usuario, contraseña)
        usuarios.registrar()
        self.inicioSesion()
                
    def inicioSesion(self):
        
        usuario = input("\t\t\033[0;37m"+"ingrese nombre de usuario:\n" + "\033[0;m\t\t")
        contraseña = input ("\t\t\033[0;37m"+"ingrese contraseña:\n" + "\033[0;m\t\t")
        usuarios = Registro(usuario, contraseña)
        while Registro.verificarLogin(usuarios) == False:
            print("\t\t\033[0;37m"+"usuario o contraseña incorrectos"+ "\033[0;m\t\t")
            usuario = input("\t\t\033[0;37m"+"ingrese nombre de usuario:\n" + "\033[0;m\t\t")
            contraseña = input ("\t\t\033[0;37m"+"ingrese contraseña:\n" + "\033[0;m\t\t")
            usuarios = Registro(usuario, contraseña)
        usuarios.login()  
        self.inicio2()   
                    
    def inicio2(self):
        print("\t\t\t\t\033[1;34m"+ "MOVIE" + "\033[0;m")
        print("\t\t\033[0;37m"+ "1.Buscar peliculas por categorias\n" + "\033[0;m")
        print("\t\t\033[0;37m"+"2.Buscar disponibilidad de pelicula en plataforma stream\n"+ "\033[0;m")   
        print("\t\t\033[0;37m"+"3.Ver fecha de pelicula\n"+ "\033[0;m")
        print("\t\t\033[0;37m"+"4.Ver pais de produccion\n"+ "\033[0;m")
        print("\t\t\033[0;37m"+"5.Ver lenguaje de pelicula\n"+ "\033[0;m")
        print("\t\t\033[0;37m"+"6.Salir\n"+ "\033[0;m")
        opcion2 = int(input("\t\t\033[0;37m"+"¿Qué desea hacer?\n" + "\033[0;m\t\t"))
        while opcion2:
            while opcion2 != 1 and opcion2 !=2 and opcion2 != 3 and opcion2 !=4 and opcion2 !=5 and opcion2 !=6:
                print("\t\t\t\t\033[1;34m"+ "MOVIE" + "\033[0;m")
                print("\t\t\033[0;37m"+ "1.Buscar peliculas por categorias\n" + "\033[0;m")
                print("\t\t\033[0;37m"+"2.Buscar disponibilidad de pelicula en plataforma stream\n"+ "\033[0;m")   
                print("\t\t\033[0;37m"+"3.Ver fecha de pelicula\n"+ "\033[0;m")
                print("\t\t\033[0;37m"+"4.Ver pais de produccion\n"+ "\033[0;m")
                print("\t\t\033[0;37m"+"5.Ver lenguaje de pelicula\n"+ "\033[0;m")
                print("\t\t\033[0;37m"+"6.Salir\n"+ "\033[0;m")
                opcion2 = int(input("\t\t\033[0;37m"+"¿Qué desea hacer?\n" + "\033[0;m\t\t"))
                
            if opcion2 == 1:
                self.peliCat()
                opcion2 = False
            elif opcion2 == 2:
                self.peliPlam()
                opcion2 = False
            elif opcion2 == 3:
                self.peliFecha()
                opcion2 = False
            elif opcion2 == 4:
                self.peliPais()
                opcion2 = False
            elif opcion2 == 5:
                self.peliLeng()
                opcion2 = False
            else:
                self.salir()
                opcion2 = False
                         
    def peliCat(self):
        
        print("\t\t\033[3;44m"+'CATEGORIAS DISPONIBLES'+ "\033[0;m")
        print("\t\t\033[3;36m"+"Fiction - Fantasy - Adventure\n"+"\033[0;m")
        print("\t\t\033[3;36m"+"Musical - Mistery - Thriller\n"+"\033[0;m") 
        print("\t\t\033[3;36m"+"Crime - Romance - Animation\n"+"\033[0;m")
        print("\t\t\033[3;36m"+"Comedy - Science Fiction\n"+"\033[0;m")
        print("\t\t\033[3;36m"+"Drama - Action - Kids\n"+"\033[0;m") 
                
        interes1 = input("\t\t\033[0;37m"+"Ingrese primera categoria de interes:\n" + "\033[0;m\t\t")  
        interes2 = input("\t\t\033[0;37m"+"Ingrese segunda categoria de interes:\n"+ "\033[0;m\t\t")
        interes3 = input("\t\t\033[0;37m"+"Ingrese tercera categoria de interes:\n"+ "\033[0;m\t\t")
        buscador = BuscarPelis (interes1, interes2, interes3)
        while BuscarPelis.buscar_categoria(buscador) == False:
            print("\t\t\033[0;37m"+'Los géneros ingresados no son correctos'+ "\033[0;m")
            interes1 = input("\t\t\033[0;37m"+"Ingrese primera categoria de interes:\n" + "\033[0;m\t\t")  
            interes2 = input("\t\t\033[0;37m"+"Ingrese segunda categoria de interes:\n"+ "\033[0;m\t\t")
            interes3 = input("\t\t\033[0;37m"+"Ingrese tercera categoria de interes:\n"+ "\033[0;m\t\t")
            buscador = BuscarPelis (interes1, interes2, interes3) 
        buscador.printMoviebyCat()
        self.inicio2()
                
    def peliPlam(self):
         
        peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t")  
        buscador = InfoPelis (peli1)
        while InfoPelis.buscar_plataforma(buscador) == False:
            print("\t\t\033[0;37m"+'La pelicula ingresada no se encuentra disponible'+ "\033[0;m")
            peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t") 
            buscador = InfoPelis (peli1)
        buscador.printMoviebyPlam() 
        self.inicio2()
                
                
    def peliFecha(self):
             
        peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t")
        buscador = InfoPelis (peli1)
        while InfoPelis.fechaPodruccion(buscador) == False:
            print("\t\t\033[0;37m"+'La pelicula ingresada no se encuentra disponible'+ "\033[0;m")
            peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t")
            buscador = InfoPelis (peli1)
        buscador.printFecha()
        self.inicio2()
           
                        
    def peliPais(self):
                
        peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t") 
        buscador = InfoPelis (peli1)
        while InfoPelis.paisPodruccion(buscador) == False:
            print("\t\t\033[0;37m"+'La pelicula ingresada no se encuentra disponible'+ "\033[0;m")
            peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t") 
            buscador = InfoPelis (peli1)
        buscador.printpais()
        self.inicio2()
               

    def peliLeng(self):
         
        peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t") 
        buscador = InfoPelis (peli1)
        while InfoPelis.lenguajePodruccion(buscador) == False:
            print("\t\t\033[0;37m"+'La pelicula ingresada no se encuentra disponible'+ "\033[0;m")
            peli1 = input("\t\t\033[0;37m"+"Ingrese pelicula:\n"+ "\033[0;m\t\t") 
            buscador = InfoPelis (peli1)
        buscador.printLenguaje()
        self.inicio2()
               
    def salir(self):
        
        self.inicio()
          
            
