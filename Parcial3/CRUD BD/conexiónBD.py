"""OBJETIVO: conectarse a una base datos que ya existe"""

import mysql.connector    #libreria

#Conectar con la base de datos en mysql
conexion=mysql.connector.connect(      
    host='localhost',    #o tambien la url:127.0.0.1
    user='root',         #random
    password='',         #no hay contraseña aún
    database='bd_python'     
)
"""
#Verificar si la conexion fue exitosa
if conexion.is_connected():
    print("Se creo la conexion o base de datos correctamente")
else:     #pq no se instalo la libreria, no hay user, la contra es incorrecta, la base de datos no existe
    print("No fue posible conectar con la base de datos, verifique")
    
""" 
"""
xamp---star apache y mysql
127.0.0.1 phpmyadmin--- bases de datos
"""