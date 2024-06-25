contador_estu=0
promedios_totales=[]

while True:
    print(" \t BIENVENIDO AL REGISTRO ESCOLAR")
    a_nombre=input("Ingrese por favor el nombre del alumno: ").upper()
    a_carrera=input(f"Ingrese por favor la carrera del alumno {a_nombre}: ")
    
    suma_parciales=0
    for parcial in range(1,4):
        print(f"Registro de calificación parcial {parcial}")
        calificacion=int(input(f"Ingrese por favor la calificación obtenida en el parcial {parcial}: "))
        suma_parciales+=calificacion
    
    p_final=int(input("Ingrese por favor la calificación del proyecto final: "))
    
    promedio_parciales=suma_parciales/3 
    promedio_total=(promedio_parciales+p_final)/2  
    
    print(f"El promedio final del alumno es: {promedio_parciales} \n La calificación del proyecto final es: {p_final} \n La calificación final es {promedio_total} ")
    if promedio_total<80 and p_final<50:
        print("Presenta examen extraordinario")
    else:
        print("Cuatrimestre aprobado")
        
    promedios_totales.append(promedio_total)
    contador_estu+=1

    x=input("Desea agregar otro registro? (Si/No)").upper()
    if x!="SI":
        break

promedio_todos2=sum(promedios_totales)
promedio_todos3=promedio_todos2/contador_estu
print(f"Se regitraron {contador_estu} \n El promedio de calificación total de los estudiantes registrados es de {promedio_todos3}")