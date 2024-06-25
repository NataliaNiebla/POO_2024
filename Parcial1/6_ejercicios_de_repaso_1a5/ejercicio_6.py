"""
6.- Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

print("\tTABLAS DE MULTIPLICAR")
print()

for i in range(1,11):
    print(f"Tabla del {i}")
    for x in range(1,11):
        resultado=i*x
        print(f"{i}x{x}={resultado}")
        
