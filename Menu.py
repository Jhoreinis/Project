from BuscarPelis import BuscarPelis
from BuscadorStream import BuscadorStream
from Registro import Registro

usuario = input("Cree un nombre de usuario:\n")
contraseña = input ("ingrese una contraseña:\n")

usuarios = Registro(usuario, contraseña)
while Registro.usuarioRegistrado(usuarios) == False:
    print(Registro.usuarioRegistrado(usuarios))
    print("Usuario ya se encuentra registrado")
    usuario = input("Cree un nombre de usuario:\n")
    contraseña = input ("ingrese una contraseña:\n")
    usuarios = Registro(usuario, contraseña)
usuarios.registrar()

###

usuario = input("ingrese nombre de usuario:\n")
contraseña = input ("ingrese contraseña:\n")

usuarios = Registro(usuario, contraseña)
while Registro.verificarLogin(usuarios) == False:
    print(Registro.verificarLogin(usuarios))
    print("usuario o contraseña incorrectos")
    usuario = input("ingrese nombre de usuario:\n")
    contraseña = input ("ingrese contraseña:\n")
    usuarios = Registro(usuario, contraseña)
usuarios.login()



 ####
interes1 = input("Ingrese primera categoria de interes:\n")  
interes2 = input("Ingrese segunda categoria de interes:\n")
interes3 = input("Ingrese tercera categoria de interes:\n")

buscador = BuscarPelis (interes1, interes2, interes3)
while BuscarPelis.buscar_categoria(buscador) == False:
    print(BuscarPelis.buscar_categoria(buscador))
    print('Los géneros ingresados no son correctos')
    interes1 = input("Ingrese primera categoria de interes:\n")  
    interes2 = input("Ingrese segunda categoria de interes:\n")
    interes3 = input("Ingrese tercera categoria de interes:\n")
    buscador = BuscarPelis (interes1, interes2, interes3) 
buscador.printMoviebyCat()

###
peli1 = input("Ingrese pelicula:\n")  

buscador = BuscadorStream (peli1)
while BuscadorStream.buscar_plataforma(buscador) == False:
    print(BuscadorStream.buscar_plataforma(buscador))
    print('La pelicula ingresada no se encuentra disponible')
    peli1= input("Ingrese pelicula de interes:\n") 
    buscador = BuscadorStream (peli1)
buscador.printMoviebyPlam()
