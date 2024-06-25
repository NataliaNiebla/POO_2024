"""
1.- 

 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
 """
 
def crear_lista (lista_input):
    lista=lista_input.split(',')
    lista=[int(i) for i in lista]
    print(f"Tu lista es: {lista}")
    return lista
    
def str_visualizacion (lista):
    lista2 = ', '.join(map(str, lista))
    resultado = lista2
    print(resultado)
    return resultado

def ordenar_lista(lista):
    sorted_list=sorted(lista)
    print(f"La lista ordenada es: {sorted_list}")
    return sorted_list

def long_lista(lista):
    longitud=len(lista)
    print(f"La longitud de la lista es de: {longitud}")
    return longitud


def buscar_el(lista):
    num_buscar=int(input("Escribe el numero a buscar"))
    for i in numeros:
        if num_buscar==i:
            print(f"El numero a buscar es: {num_buscar} y si se encontro")
        

print("MENU")
opcion=input("1.- Recorrer la lista y mostrarla \n 2.- Recorra la lista de numeros y devuelva un string \n 3.- Ordenarla y mostrarla \n 4.- Mostrar su longitud \n 5.-Buscar algun numero dentro de la lista \n ¿Que opción desea?  ")

if opcion=="1":
  lista_input=input("Ingresa una lista de números separados por comas: ")
  lista= crear_lista(lista_input)
elif opcion=="2":
  resultado= str_visualizacion(lista)
elif opcion=="3":
  sorted_list=ordenar_lista(lista)
elif opcion=="4":
  longitud=long_lista(lista)
elif opcion=="5":
  buscar=input("Busca el elemento: ")
  buscar_el(buscar)
else:
  print("Opción invalida ... verifique")


