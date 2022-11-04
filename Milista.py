from Peliculas import Peliculas

class MiLista(Peliculas):
    def init(self, titulos) -> None:
        return super()._init_(titulos)

    def listaFavoritos(self):

       listafav = []
       opcion = input("¿Agregar pelicula a favoritos?")
       while opcion == "si":
         peli = input("¿Ingrese pelicula?")
         if peli == self.titulos:
             listafav.append(peli)
         else:
             print("Pelicula ingresada no disponible")
         opcion = input("¿Agregar pelicula a favoritos?")
       print(listafav)

    def listaPendientes(self):

       listafav = []
       opcion = input("¿Agregar pelicula a pendientes?")
       while opcion == "si":
         peli = input("¿Ingrese pelicula?")
         if peli == self.titulos:
             listafav.append(peli)
         else:
             print("Pelicula ingresada no disponible")
         opcion = input("¿Agregar pelicula a pendientes?")
       print(listafav)

    def listaVistos(self):

       listafav = []
       opcion = input("¿Agregar pelicula a vistos?")
       while opcion == "si":
         peli = input("¿Ingrese pelicula?")
         if peli == self.titulos:
             listafav.append(peli)
         else:
             print("Pelicula ingresada no disponible")
         opcion = input("¿Agregar pelicula a vistos?")
       print(listafav)

titulo = MiLista ("Titanic")
titulo.listaFavoritos()

titulo2 = MiLista ("Avatar")
titulo2.listaPendientes()

titulo3 = MiLista ("Spiderman")
titulo3.listaVistos()
