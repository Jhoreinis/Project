class BuscarPelis:
    def __init__(self, interes1:str, interes2:str, interes3:str): 
        self.interes1 = interes1
        self.interes2 = interes2
        self.interes3 = interes3
    
    def buscar (self): 
        file = open("data.txt", "r")
        lines = file.readlines()
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
        if (cont1+cont2+cont3 >=3):
            return True
        return False
    
    def printMoviebyCat(self):
        file = open("data.txt", "r")
        lines = file.readlines()
        for linea in lines:
        #lista.append(linea)
            save_split = linea.split(',')
            title, cat, = save_split[0], save_split[1]
            if self.interes1 == cat or self.interes2 == cat or self.interes3 == cat:
                print(title)
        file.close()
