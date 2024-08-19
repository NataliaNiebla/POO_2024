from conexionBD import *

class Cliente:
    def __init__(self, nif, nombre, direccion, ciudad, tel):
        self.nif=nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel
        
    def insertar(self):
        try:
            cursor.execute(
                "insert into clientes values(%s,%s,%s,%s,%s)",
                (self.nif, self.nombre, self.direccion, self.ciudad, self.tel)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False  

    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from clientes"
            )
            return cursor.fetchall() # regresa tupla(s)
        except:
            return []   

    @staticmethod
    def actualizar(nombre, direccion, ciudad, tel, nif):
        try:
            cursor.execute(
                "update clientes set nombre=%s, direccion=%s,ciudad=%s, tel=%s where nif=%s",
                (nombre, direccion, ciudad, tel, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
     
    @staticmethod
    def eliminar(nif):
        try:
            cursor.execute(
                "delete from clientes where nif=%s",
                (nif,) #la coma va pq solo asi se puede ejecutar
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False