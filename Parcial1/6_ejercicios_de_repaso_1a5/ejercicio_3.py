"""
3.- # Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
"""

for i in range(1,61):
    resultado=i*i
    print(f"{i} X {i} es igual al {resultado}")


contador=1
while contador<=60:
    resultado=contador*contador
    print(f"{contador} X {contador} es igual al {resultado}")
    contador+=1