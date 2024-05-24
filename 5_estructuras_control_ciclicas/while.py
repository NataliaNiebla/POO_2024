"""
El ciclo while es una estructura de control que itera o repite la ejecución de una serie de instrucciones tantas veces como la condicion se cumpla "TRUE"
Sintaxis: while condición:
            bloque de instrucciones
"""

#Ej 1. Crear un programa que imprimar 5 veces @
contador=1

while contador <=5:
    print("@")
    contador+=1

#Ej 2. Crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma
contador=1
suma=0

contador=1
suma=0
while contador<=5:
    print(contador)
    suma+=contador
    contador+=1
    print(f"La suma es: {suma}")   

#Ej 3. Crear un programa que solicite un numero int y a continuación imprima la tabla de multiplicar correspondiente
numero=int(input("Ingresa un numero: "))

multi=0
i=1
while i<=10:
    multi=i*numero
    print(f"{numero} X {i} = {multi}")
    i+=1
