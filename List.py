from Info import Info
import io
class List:   
    def __init__(self):
        self.Head = None
        self.ULT = None  
        
    def AddInfo(self, data=''):  
        P = Info(data)
        if self.Head == None:
            self.Head = P
            return
        last = self.Head
        while last.next:    
            last = last.next
        last.next = P
        
    def WriteList(self):
        Info
        P = self.Head
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.Head
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta
    
    def recomendar_categoria(self): #Recomienda por categoria
        edad = input("Ingrese su edad")
        interes1 = input("Ingrese primera categoria de interes:")  
        interes2 = input("Ingrese segunda categoria de interes:")
        interes3 = input("Ingrese tercera categoria de interes:")
        Info
        P = self.Head
        peliculas = []
        while (P != None):
            string = P.data
            peliculas.append(P)
            P = P.next
            peliculas = string.split(",")
            #print(peliculas[0])
            
            if peliculas[1] .__eq__ (interes1):
                print(peliculas[0])
                    
            if peliculas[1] .__eq__ (interes2):
                print(peliculas[0])
                    
            if peliculas[1] .__eq__ (interes3):
                print(peliculas[0])
          
    def recomendar_edad(self):
        
        pass
