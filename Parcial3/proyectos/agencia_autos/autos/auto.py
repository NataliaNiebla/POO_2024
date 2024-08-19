from conexionBD import *

class Auto:
    def __init__(self, matricula, marca, modelo, color, nif):
        self.matricula=matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
        
    def insertar(self):
        try:
            cursor.execute(
                "insert into autos values(%s,%s,%s,%s,%s)",
                (self.matricula, self.marca, self.modelo, self.color, self.nif)
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
                "select * from autos"
            )
            return cursor.fetchall() # regresa tupla(s)
        except:
            return []   

    @staticmethod
    def actualizar(nif, marca, modelo, color, matricula):
        try:
            cursor.execute(
                "update autos set nif=%s, marca=%s, modelo=%s, color=%s where matricula=%s",
                (nif, marca, modelo, color, matricula)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
     
    @staticmethod
    def eliminar(matricula):
        try:
            cursor.execute(
                "delete from autos where matricula=%s",
                (matricula,) #la coma va pq solo asi se puede ejecutar
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False