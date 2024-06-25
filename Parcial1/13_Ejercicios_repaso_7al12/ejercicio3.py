""" 3. Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas
"""
lista=[]
i=0

if len(lista)<=0:
   opcion="SI" 
   while opcion=="SI":
       texto=input(f"frase {i}: ").upper()
       lista.append(texto)
       opcion=input("¿Deseas aagregar otra?").upper()
       i+=1
       
print(lista)
