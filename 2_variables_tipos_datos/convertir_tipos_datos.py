""" Cuando se imprime en pantalla una cadena de caracteres se trabaja por default con cadenas, es decir,
python no puede concatenar otra cosa que no sea un string (str)
"""

texto="soy una cadena de caracteres"
numero=23

#Concatenar Str con Str
print("Soy otra cadena y "+ texto )

#Concatenar un str con un int
num_str=str(numero)
print("El número es "+ num_str)

print("El numero es " +str(numero))

#Concatenar un ont con un str
n1=int("23")
n2=33

suma=n1+n2

print(f"La suma es {suma}")

#Concatenar float y int con str
n1=int("23")
n2=33.0

suma=n1+n2

print(f"La suma es {suma}")
print(type(suma))


n3=29.99
n4=33.0

suma2=int(n3+n4)

print(f"La suma es {suma2}")
print(type(suma2))