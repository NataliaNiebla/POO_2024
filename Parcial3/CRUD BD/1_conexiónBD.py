"""OBJETIVO: conectarse a una base datos que ya existe"""

import mysql.connector    #libreria/ dependencia a instalar

#Conectar con la base de datos en mysql
try:
    conexion=mysql.connector.connect(      #objeto de conexion, 
        host='localhost',    #o tambien la url:127.0.0.1
        user='root',         #random
        password='',         #no hay contraseña aún
        database='bd_python'     
    )   #parametros de la función connect
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error en el servidor, vuelve a intentar")

else: #si no existe ninguna excepción
    
    #Verificar si la conexion fue exitosa
    if conexion.is_connected():
        print("Se creo la conexion o base de datos correctamente")
    else:     #pq no se instalo la libreria, no hay user, la contra es incorrecta, la base de datos no existe
        print("No fue posible conectar con la base de datos, verifique")