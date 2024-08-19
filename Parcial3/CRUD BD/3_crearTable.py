"""OBJETVO: crear una tabla"""
from conexiónBD import*

try:
    micursor=conexion.cursor()

    sql='create table clientes (id int primary key auto_increment, nombre varchar(60), direccion varchar(120), tel varchar(10))'

    micursor.execute(sql)
    
except:
    print("Ocurrio un problema, por favor verifica")
else:
    print("Se creo la tabla exitosamente")