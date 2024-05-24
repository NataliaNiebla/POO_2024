"""
4.- #Solicitar 2 numeros al usuario
 y realizar todas las operaciones
basicas de una calculadora (+,-,*,/)
y mostrar por pantalla el resultado
"""

n1=int(input("Ingresa un número entero: "))
n2=int(input("Ingresa otro número entero: "))

suma=n1+n2
print(f"{n1} + {n2} = {suma}")
resta=n1-n2
print(f"{n1} - {n2} = {resta}")
resta2=n2-n1
print(f"{n2} - {n1} = {resta2}")
multi=n1*n2
print(f"{n1} x {n2} = {multi}")
div=n1/n2
div2=n2/n1
print(f"{n1} / {n2} = {div}")
print(f"{n2} / {n1} = {div2}")