"""
7.- Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
"""

num=int(input("Ingresa tu numero menor: "))
num2=int(input("Ingresa tu número mayor: "))

for i in range(num,num2):
    if i % 2!=0:
        print(i)
