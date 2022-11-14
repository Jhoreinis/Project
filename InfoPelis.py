class InfoPelis:
    
    """
    Esta clase se utiliza para buscar informacion
    de alguna pelicula ingresada 
    """
    
    def _init_(self, peli1:str): 
        self.peli1 = peli1
        
        """
        El atributo le permite al usuario ingresar 
        la pelicula de su interes. 
        """
        
    def buscar_plataforma(self): 
        
        """
        Este metodo nos permite buscar en que
        plataforma se encuentra disponible para
        ver cualquier pelicula ingresada 
        """
        
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        contador = 0
        for linea3 in lines3:
            pelicula = linea3.split(',')[0]
            if (self.peli1 ==  pelicula):
                    contador +=1
        file3.close()
        
        """
        Una vez leida y encontrada la informacion
        el contador será mayor o igual a uno
        y nos indica que el usuario ha ingresado
        correctamente la información  
        """
        
        if (contador>=1):
            return True
        return False
    
    def printMoviebyPlam(self):
        
        """
        Una vez verificada la información
        este metodo imprime la plataforma
        en la que se puede ver la pelicula
        """
        
        file3 = open("data.txt", "r")
        lines3 = file3.readlines()
        for linea3 in lines3:
            save_split3 = linea3.split(',')
            plataforma, pelicula, = save_split3[2], save_split3[0]
            if self.peli1 == pelicula:
                print("\t\tse encuentra disponible en:\t" +"\033[1;37m" +plataforma + "\033[0;m")
        file3.close()
        
    def fechaPodruccion(self): 
        
        """
        Este metodo se utiliza para hallar 
        informacion sobre la decha de 
        produccion de la pelicula 
        """
        
        """
        Esta parte del codigo sigue la misma idea
        del codigo del metodo anterior  
        """
        
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
                print("\t\tfue producida el:\t" +"\033[1;37m" + fecha + "\033[0;m")
        file3.close()
        
    def paisPodruccion(self): 
        
        """
        Este metodo se utiliza para hallar 
        informacion sobre el pais en que fue 
        producida la pelicula 
        """
        
        """
        Esta parte del codigo sigue la misma idea
        del codigo del metodo anterior  
        """
        
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
                print("\t\tse produjo en:\t"+"\033[1;37m"  + pais +"\033[0;m")
        file3.close()
        
    def lenguajePodruccion(self): 
        
        """
        Este metodo se utiliza para hallar 
        informacion sobre el lenguaje original 
        de la pelicula 
        """
        
        """
        Esta parte del codigo sigue la misma idea 
        del codigo del metodo anterior  
        """
        
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
                print("\t\tlenguaje original\t" +"\033[1;37m" + lenguaje +"\033[0;m")
        file3.close()
           
