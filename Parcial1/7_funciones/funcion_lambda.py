"""
Una función lambda es una pequeña función anónima.
Una función lambda puede tomar cualquier número de argumentos, pero solo puede tener una expresión.
Las funciones Lambda pueden tomar cualquier número de argumentos:
"""

#Sintaxis-- lambda arguments : expression

"""
¿Por qué utilizar funciones Lambda?
El poder de lambda se muestra mejor cuando los usa como una función anónima dentro de otra función.
Digamos que tiene una definición de función que toma un argumento y ese argumento se multiplicará por un número desconocido:
"""

#EJEMPLO 1: Obtenga su propio servidor Python. Agregue 10 al argumento y devuelva el resultado:
x = lambda a : a + 10
print(x(5))

#EJEMPLO 2: Multiplica argumento "a" por argumento "b" y devuelve el resultado:
x = lambda a, b : a * b
print(x(5, 6))

#EJEMPLO 3: Resume el argumento "a", "b" y "c" devuelve el resultado:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#EJEMPLO 4: 
def myfunc(n):
  return lambda a : a * n

#función que siempre duplique el número que envía:
#EJEMPLO 5: 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

#función que siempre triplique el número que envía:
#EEJEMPLO 6:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

#función para crear ambas funciones, en el mismo programa:
#EJEMPLO 7:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#Utilizar funciones lambda cuando se requiera una función anónima durante un período corto de tiempo