from conexiónBD import*

try:
    micursor=conexion.cursor()
    sql="update clientes2 set direccion='Col. Nueva Vizcaya ', tel='6182341190' where id=1"
    micursor.execute(sql)
    conexion.commit()
    
except:
    print("Ha ocurrido un error")
else:
    print("Registro actualizado exitosamente")