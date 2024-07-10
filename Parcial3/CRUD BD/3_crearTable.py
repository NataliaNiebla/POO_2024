"""OBJETVO: crear una tabla"""

import mysql.connector
conexion=mysql.connector.connect(
    host='localhost',
    user='root',         #random
    password='',         #no hay contraseña aún
    database='bd_python'  
)

micursor=conexion.cursor()

sql='create table clientes (id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))'

micursor.execute(sql)

if micursor:
    print("Se creo la tabla exitosamente")