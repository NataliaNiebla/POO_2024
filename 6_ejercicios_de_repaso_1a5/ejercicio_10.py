"""
10.- Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron
"""

reprobados=0
aprobados=0

for i in range(1,16):
    alumno=int(input(f"Ingrese la calificación del alumno número {i}: "))
    if alumno<80:
        reprobados+=1
    elif alumno>=80:
        aprobados+=1
    
print(f"Hay {reprobados} calificaciones reprobatorias")
print(f"Hay {aprobados} calificaciones aprobatorias")