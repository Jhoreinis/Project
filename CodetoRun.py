from List import List

linkedlist = List()
with open('BaseDate.txt', 'r') as I:
    for line in I:
        linkedlist.append(line.strip())   
#print(linkedlist) 

linkedlist.recomendar_categoria()

        
        
