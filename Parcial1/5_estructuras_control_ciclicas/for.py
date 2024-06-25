""" 
Ciclo iterativo: se ejecuta x veces de acuerdo a los valores numericos establecidos
sintaxis: For variable in elemento_iterable(lista, rango,etc):
        bloque de instrucciones
"""

#Ej 1. Crear un programa que imprimar 5 veces @

contador=1
for contador in range(1,6):
    print ("@")
    
#Ej 2. Crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma

suma=0
for numero in range(1,6):
    print(numero)
    suma+=numero
print(f"La suma es: {suma}")

#Ej 3. Crear un programa que solicite un numero int y a continuación imprima la tabla de multiplicar correspondiente

numero=int(input("Ingresa un numero: "))

multi=0
for i in range (1,11):
    multi=i*numero
    print(f"{numero}X{i}={multi}")
