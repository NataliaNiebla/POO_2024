from conexiónBD import*

micursor=conexion.cursor()

sql="select * from clientes where id=1"
micursor.execute(sql)

#Crear un objeto para enviar el resultado de la ejecucuón del execute para posteriormente mostrar con un ciclo
resultado=micursor.fetchall()
#Se utiliza en el select
for x in resultado:
    print(x)      #Tupla