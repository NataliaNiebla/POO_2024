""" OBJETIVO: crear una base de datos"""

import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    
except:
    print("Ha ocrrido un error por favor verifique máas tarde")        
else:
    #Crear un objeto de tipo cursor que permita ejecutar instrucciones sQL
    micursor=conexion.cursor()

    sql="create database bd_python"
    micursor.execute(sql)  #ejecución de contenido/ consulta

    if micursor:
        print("Se creo la base de datos exitosamente")
    
#Mostrar las bases de datos que existen en el sistema gestor de base de datos (MySQL)
    micursor.execute("show databases")

    for x in micursor:
        print(x)