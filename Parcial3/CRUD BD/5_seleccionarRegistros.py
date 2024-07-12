from conexiónBD import*

try:
    micursor=conexion.cursor()

    sql="select * from clientes2 where id=1"
    micursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecucuón del execute para posteriormente mostrar con un ciclo
    resultado=micursor.fetchall()
    
except:
    print("Ha ocurrido un error")   
else:
    #Se utiliza en el select
    for x in resultado:
        print(x)      #Tupla