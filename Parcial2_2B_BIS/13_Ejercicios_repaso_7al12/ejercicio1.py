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
    no_encontre=True

    for i in lista:
        if buscar==i:
            print(buscar)
            print(f"El elemento {i} fue localizado en la posición {lista.index(i)}")
            no_encontre=False
            
    if no_encontre:
        print(f"No encontré el elemento")
        


lista_input=input("Ingresa una lista de números separados por comas: ")
lista= crear_lista(lista_input)
resultado= str_visualizacion(lista)
sorted_list=ordenar_lista(lista)
longitud=long_lista(lista)
buscar=input("Busca el elemento: ")
buscar_el(buscar)

