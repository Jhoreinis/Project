class InfoPelis:
    def __init__(self, peli1:str): 
        self.peli1 = peli1
        
    def buscar_plataforma(self): 
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        contador = 0
        for linea3 in lines3:
            pelicula = linea3.split(',')[0]
            if (self.peli1 ==  pelicula):
                    contador +=1
        file3.close()
        if (contador>=1):
            return True
        return False
    
    def printMoviebyPlam(self):
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        for linea3 in lines3:
            save_split3 = linea3.split(',')
            plataforma, pelicula, = save_split3[2], save_split3[0]
            if self.peli1 == pelicula:
                print("se encuentra disponible en:" + plataforma)
        file3.close()
        
    def fechaPodruccion(self): 
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        contador = 0
        for linea3 in lines3:
            pelicula = linea3.split(',')[0]
            if (self.peli1 ==  pelicula):
                contador +=1
        file3.close()
        if (contador>=1):
            return True
        return False
    
    def printFecha(self):
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        for linea3 in lines3:
            save_split3 = linea3.split(',')
            fecha, pelicula, = save_split3[3], save_split3[0]
            if self.peli1 == pelicula:
                print("fue producida el:" + fecha)
        file3.close()
        
    def paisPodruccion(self): 
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        contador = 0
        for linea3 in lines3:
            pelicula = linea3.split(',')[0]
            if (self.peli1 ==  pelicula):
                contador +=1
        file3.close()
        if (contador>=1):
            return True
        return False
    
    def printpais(self):
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        for linea3 in lines3:
            save_split3 = linea3.split(',')
            pais, pelicula, = save_split3[4], save_split3[0]
            if self.peli1 == pelicula:
                print("se produjo en:" + pais)
        file3.close()
        
    def lenguajePodruccion(self): 
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        contador = 0
        for linea3 in lines3:
            pelicula = linea3.split(',')[0]
            if (self.peli1 ==  pelicula):
                contador +=1
        file3.close()
        if (contador>=1):
            return True
        return False
    
    def printLenguaje(self):
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        for linea3 in lines3:
            save_split = linea3.split(',')
            lenguaje, pelicula, = save_split[5], save_split[0]
            if self.peli1 == pelicula:
                print("lenguaje original" + lenguaje )
        file3.close()
