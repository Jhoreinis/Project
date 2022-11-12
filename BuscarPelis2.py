class BuscarPelis2:
    def __init__(self, edadUsuario:int): 
        self.edadUsuario = edadUsuario
        
    def buscar_edad(self): 
        file = open("data.txt", "r")
        lines2 = file.readlines()
        #lista = []
        conta1 = 0
        for linea2 in lines2:
            edad = linea2.split(',')[2]
            if (self.edadUsuario >= edad):
                conta1 +=1
        file.close()
        if (conta1>=1):
            return True
        return False
    
    def printMoviebyEdad(self):
        file = open("data.txt", "r")
        lines2 = file.readlines()
        for linea2 in lines2:
        #lista.append(linea)
            save_split2 = linea2.split(',')
            title, edad, = save_split2[0], save_split2[2]
            if self.edadUsuario >= edad:
                print(title)
        file.close()