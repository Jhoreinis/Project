from Info import Info    
import io
class List:   
    def _init_(self):
        self.Head = None
        self.ULT = None
        self.contador = 0          
    def append(self, data=''):  
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
            contador+=1
        print("None")
    
    def _repr_(self):
        respuesta = ""
        P = self.Head
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta
