"""
8.- Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
"""

num=int(input("Ingresa un número: "))
porc=int(input("¿Qué procentaje requieres de este número?: "))

answ=porc*num
answ2=answ/100

print(f"El {porc}% de {num} es {answ2}")

