""" 4.  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
"""

lista=[]
cadena="Hola mundo"
entero=3
logico=True

def tipo_de_dato (dato):
    if type(dato)==bool:
        print("El tipo de dato es booleano")
    elif type(dato)==int:
        print("El tipo de dato es un entero")
    elif type(dato)==list:
        print("El tipo de dato es una lista")
    elif type(dato)==str:
        print("El tipo de dato es una cadena")
    else:
        print("Dato no encontrado")
        
tipo_de_dato(bool)
tipo_de_dato(int)
tipo_de_dato(list)
tipo_de_dato(str)