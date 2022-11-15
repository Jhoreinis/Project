class BuscarPelis:
    def __init__(self, interes1:str, interes2:str, interes3:str): 
        self.interes1 = interes1
        self.interes2 = interes2
        self.interes3 = interes3
        
        """
        Cada atributo le permite al usuario 
        ingresar tres categorias de interes
        para poder buscar las peliculas
        relacionadas a esa categoria  
        """
    
    def buscar_categoria(self): 
        file = open("data.txt", "r")
        lines = file.readlines()
        
        """
        Se utiliza split para poder comparar y buscar
        las peliculas que pertenezcan a cada categoria 
        ingresada
        """
        
        cont1 = 0
        cont2 = 0
        cont3 = 0
        for linea in lines:
            cat = linea.split(',')[1]
            if (self.interes1 == cat):
                    cont1 +=1
                    
            if (self.interes2 == cat):
                    cont2 +=1
                    
            if (self.interes3 == cat):
                    cont3 +=1
        file.close()
        
        """
        Si el contador es mayor o igual a tres
        quiere decir que la informacion suministrada
        por el usuario es correcta y ha sido encontrada
        de lo contrario retornara False y le pedirá
        al usuario volver a ingresar la información
        """
        
        if (cont1+cont2+cont3 >=3):
            return True
        return False
    
    
    def printMoviebyCat(self):
        
        """
        Una vez se hallan buscado y encontrado las 
        peliculas imprimiremos la informacion al usuario
        con este metodo
        """
        
        file = open("data.txt", "r")
        lines = file.readlines()
        for linea in lines:
            save_split = linea.split(',')
            title, cat, = save_split[0], save_split[1]
            if self.interes1 == cat or self.interes2 == cat or self.interes3 == cat:
                print("\t\t\033[3;37m" + title + "\033[0;m" + "\033[1;34m -->" + "\033[0;m"+cat)
        file.close()
