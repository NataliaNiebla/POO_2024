paises=["Mexico", "USA", "Brasil", "Japon"]
numeros=[1,2,3,4,5,6,7,8,1]
texto=["Hola", True, 1,2,10]
"""
#Ordenar una lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#print(texto)  --- No funciona
#texto.sort()
#print(texto)

#Añadir elementos  --- Insert es para insertar en un lugar especifico
print(texto)
texto.insert(len(texto),"True")
print(texto)
texto.insert(len(texto), True)
print(texto)
texto.append(False)
print(texto)

#Eliminar elementos
print(numeros)
numeros.remove(4) #Va a eliminar todas las conscecuencias dentro de la lista #DESVENTAJA
print(numeros)
numeros.pop(0)
print(numeros)

#Dar vuelta a la lista
print(numeros)
numeros.reverse()
print(numeros)

#Buscar un dato dentro de una lista
busqueda=("Brasil" in paises)
print(busqueda)
"""
#Cuantas veces hay un valor en una lista
print(numeros)
numeros.append(1)
cuantos=numeros.count(1)
print(cuantos)

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)