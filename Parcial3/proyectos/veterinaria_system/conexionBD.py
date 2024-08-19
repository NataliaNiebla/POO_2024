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

    sql="create database Veterinaria_db"
    micursor.execute(sql)  #ejecución de contenido/ consulta

    if micursor:
        print("Se creo la base de datos exitosamente")