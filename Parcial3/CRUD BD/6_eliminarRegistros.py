"""OBJETIVO: eliminar un registro de la base de datos."""
from conexiónBD import*

try:
    micursor=conexion.cursor()
    sql="delete from `clientes` where id=1"
    micursor.execute(sql)
    conexion.commit()
    
except:
    print("Ha ocurrido un error")
else:
    print("Registro eliminado exitosamente")