from BuscarPelis import BuscarPelis

interes1 = input("Ingrese primera categoria de interes:")  
interes2 = input("Ingrese segunda categoria de interes:")
interes3 = input("Ingrese tercera categoria de interes:")
#search = borrador(interes1, interes2, interes3)
#search.buscar()
buscador = BuscarPelis (interes1, interes2, interes3)
while BuscarPelis.buscar(buscador) == False:
    print(BuscarPelis.buscar(buscador))
    print('Los géneros ingresados no son correctos')
    interes1 = input("Ingrese primera categoria de interes:")  
    interes2 = input("Ingrese segunda categoria de interes:")
    interes3 = input("Ingrese tercera categoria de interes:")
    buscador = BuscarPelis (interes1, interes2, interes3) 
buscador.printMoviebyCat()
        
        
