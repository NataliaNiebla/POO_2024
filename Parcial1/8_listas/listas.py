"""
List (ARRAY)
son colecciones o conjuntos de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice númerico

Nota: sus valores son modificables

La lista es una colección ordenada y modificable. Permite miembros duplicados
"""
"""
import os
os.system("Cls")

#Ejemplo 1: Crear una lista con datos númericos e imprimir el contendio
lista=[23,34]
print(lista)

#recorre la lista con for
for i in lista:
    print(i)
    
#recorre la lista con while
i=0
while i<=len(lista)-1:
    print(lista[i])
    i+=1
    
    
#Crea una lista de 4 palabras, solicitar una palabra y buscar la coincidencia en la lista, indicar su la encontro o  no en la posición
palabras=["hola", "2024", "bye", "utd"]
palabra_buscar=input("Ingresa la palabra a buscar: ")

no_encontre=True


for i in palabras:
    if palabra_buscar==i:
        print(palabra_buscar)
        print(f"La palabra {i} localizada en la posición {palabras.index(i)}")
        no_encontre=False
        
if no_encontre:
    print(f"No encontré la palabra")
    
    
i=0
while i<len(palabras):
    if palabra_buscar==palabras[i]:
        print(f"Encontre la palabra {palabra_buscar} en la posición {i}")
        no_encontre=False
    i+=1
    
if no_encontre:
    print(f"No se encontro la palabra")
    
#Ejemplo 3: Agregar y eliminar elementos de una lista
numeros=[23,24]
print(numeros)

#agregar un elemento
numeros.append(100)
numeros.insert(3,200)
print(numeros)

#elimina un elemento
numeros.remove(100) #indica el elemento a borrar
print(numeros)
numeros.pop(2)#indicar la posicion a borrar
print(numeros)

# Ejemplo 4 crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

agenda=[["carlos", 6182334567],
        ["Karin", 6182334568],
        ["Leon", 6182334569],
        ["pedro", 6181234578],
 ]

print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.-{i}")
"""

#from funciones_pelis import *


#Ejemplo 5 Crear un programa que permita gestionar(administar) peliculas, colocar un menu de opciones para agregar,remover, consultar peliculas.

# 1-Utilizar funciones y mandar llamar desde otro archivo
# 2-Utilizar listas para almacenar los nombres de peliculas

import os

def insertar_peli():
    pelicula=input("Nombre de la pelicula: ").upper
    pelis.append(pelicula)
    print(f"La pelicula '{pelicula}' ha sido agregada a la cartelera.")
    
def remover_peli():
    peli_baja=input("Nombre de la pelicula a eliminar: ").upper
    if peli_baja in pelis:
        print(f"La pelicula '{peli_baja}' será eliminada de cartelera cinepolis 2024.")
        pelis.remove(peli_baja) #indica el elemento a borrar
    else:
        print(f"La pelicula '{peli_baja}' no está disponible en la cartelera cinepolis 2024.")
        
def consultar_peli():
    consultar_peliculala=input("Ingresa la pelicula a buscar: ").upper
    no_encontrada=True
    for i in pelis:
        if consultar_peliculala==i:
            print=(f"La pelicula {i} esta en la posición {pelis.index(i)+1}")
            no_encontrada=False
    if no_encontrada:
        print=(f"La pelicula {consultar_peliculala} no fue encontrado")
    

pelis=["Inmaculada", "Intensamente 2", "Angeles inesperados", "Furiosa: Mad max", "Haikyu: La batalla del basurero"].upper


opcion="1"
while opcion != "4":
    os.system("cls")
    print("Bienvenido a la edición de la cartelera cinepolis 2024")
    print(f"La cartelera Junio 2024 es \n {pelis}")
    print("\n\t OPCIONES DEL SISTEMA \n 1.-Agregar \n 2.- Remover \n 3.-Consultar \n 4.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    if opcion=="1":
        insertar_peli()
    elif opcion=="2":
        remover_peli()
    elif opcion=="3":
        consultar_peli()
    elif opcion=="4":
        print("gracias por utilizar el sistema")
        break
    else:
        print("Opción no válida, por favor elige una opción válida (1-4).")

        input("\nPresiona Enter para continuar...")      

