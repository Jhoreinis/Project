from List import List
from Registro import Registro

print("Bienvenido\n 1.Registrarse\n 2.Iniciar sesión\n 3.salir")
opcion = int(input("Ingrese opción:\n"))
while opcion:
    while opcion!= 1 and opcion !=2 and opcion !=3:
            print("Opción incorrecta.\n Elija una opción nuevamente")
            print("1.Registrarse\n 2.Iniciar sesión\n 3.salir")
            opcion = int(input("Ingrese opción:\n"))
            
    if opcion  == 1:
        usuario = (input("Cree un nombre de usuario:\n"))
        contraseña = (input("Digite una contraseña:\n"))
        Registro.registrar = (usuario, contraseña)
        registro = Registro.registrar
        print ("Registro exitoso")
        opcion = False
        
    elif opcion == 2:
        user = input("ingrese nombre de usuario:\n")
        contra = input("ingrese contraseña:\n")
        Registro.inisioSesion = (user, contra)
        login = Registro.inisioSesion
        print ("Ha iniciado sesión con exito")
        opcion = False
    else:
        print("Ha salido con exito")
        break

#linkedlist = List()
#with open('BaseDate.txt', 'r') as I:
    #for line in I:
        #linkedlist.append(line.strip())   
#print(linkedlist) 

#linkedlist.recomendar_categoria()

        
        
