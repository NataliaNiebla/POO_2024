"""OBJETIVO: actualizar un dato de la base de datos."""
from conexiónBD import*

try:
    micursor=conexion.cursor()
    sql="update clientes set direccion='Col. Nueva Vizcaya ', tel='6182341190' where id=2"
    micursor.execute(sql)
    conexion.commit()
    
except:
    print("Ha ocurrido un error")
else:
    print("Registro actualizado exitosamente")