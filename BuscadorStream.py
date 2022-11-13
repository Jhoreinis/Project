class BuscadorStream:
    def __init__(self, peli1:str): 
        self.peli1 = peli1
        
    def buscar_plataforma(self): 
        file = open("data.txt", "r")
        lines = file.readlines()
        cont1 = 0
        for linea in lines:
            pelicula = linea.split(',')[0]
            if (self.peli1 ==  pelicula):
                    cont1 +=1
        file.close()
        if (cont1>=1):
            return True
        return False
    
    def printMoviebyPlam(self):
        file = open("data.txt", "r")
        lines = file.readlines()
        for linea in lines:
            save_split = linea.split(',')
            plataforma, pelicula, = save_split[2], save_split[0]
            if self.peli1 == pelicula:
                print(self.peli1 + "se encuentra disponible en:" + plataforma)
        file.close()
