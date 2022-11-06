from List import List

linkedlist = List()
with open('BaseDate.txt', 'r') as I:
    for line in I:
        linkedlist.append(line.strip())   

#Imprmir Lista Simple Enlazada 
print(linkedlist) #Imprimir Lista con peliculas recomendadas 

        
        
