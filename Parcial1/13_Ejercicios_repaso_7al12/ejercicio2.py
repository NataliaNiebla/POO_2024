"""
2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for
"""

#WHILE
listota=[]
i=0
while i<120:
    n_elem=int(input("Ingresa un número para la lista por favor: "))
    listota.append(n_elem)
    i+=1
    
if len(listota)==119:
    print(f"La lista creada es: {listota}")
     
#FOR
listota=[]
for i in range(1,121):
    n_elem=int(input("Ingresa un número para la lista por favor: "))
    listota.append(n_elem)
    if len(listota)==120:
        print(f"La lista creada es: {listota}")
