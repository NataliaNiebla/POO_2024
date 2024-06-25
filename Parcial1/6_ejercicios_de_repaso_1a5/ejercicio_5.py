"""
5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
"""

num=int(input("Ingresa tu numero menor: "))
num2=int(input("Ingresa tu número mayor: "))

while num<=num2:
    print(num)
    num+=1

    
for i in range(num,num2+1):
    print(i)
    