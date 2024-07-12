from conexiónBD import*

try:
    micursor=conexion.cursor()
    sql="delete from `clientes2` where id=1"
    micursor.execute(sql)
    conexion.commit()
    
except:
    print("Ha ocurrido un error")
else:
    print("Registro eliminado exitosamente")