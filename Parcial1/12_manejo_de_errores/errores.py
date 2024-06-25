#Los errores de excepciones en un leguaje de programación no es otra cosa que los errores en tiempo de ejecución, cuando se maneja los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en el programa en el tiempo de ejecución

#Ejemplo 1. se presenta un error cuando no es generada una variable
"""
try:
    nombre=input("Dame el nombre completo de una persona: ")

    if len(nombre)>0:
        nombre_usuario="El nombre de usuario del sistema es: "+nombre
        
    print(nombre_usuario) 
except:
    print("Es necesario introducir un nombre de una persona")
    
"""
"""
    
#Ejemplo 2. Cuando se solicita un número y se escribe otra cosa
numero=int(input("Ingresa un número entero: "))

try:
    if numero>0:
        print("Número entero positivo")
    else:
        print("Número entero negativo")
except:
    print("No es posible convertir una letra a un número, verifica por favor")
    
"""
    

#Ejemplo 3. Cuando se generan multiples excepciones
try:
    numero=int(input("Ingresa un numero, por favor: "))
    print(f"El cuadrado de el número {numero} es: "+str(numero*numero))
except TypeError:
    print("No es un número entero")
except ValueError:
    print("No es posible convertir una letra a un número, verifica por favor")
else:
    print("Se ejecuto sin errores")
finally:
    print("Accion finalizada")
