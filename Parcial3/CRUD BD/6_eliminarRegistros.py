from conexiónBD import*

micursor=conexion.cursor()

sql="delete from `clientes` where id=1"

micursor.execute(sql)

conexion.commit()
print("Registro eliminado exitosamente")