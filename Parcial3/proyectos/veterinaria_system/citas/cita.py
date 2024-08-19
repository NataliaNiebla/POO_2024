from conexionBD import *
class Cita:
    def __init__(self,id_cliente, id_animal, id_empleado, id_servicio):
        self.id_cliente=id_cliente
        self.id_animal=id_animal
        self.id_empleado=id_empleado
        self.id_servicio=id_servicio   

    @staticmethod
    def confirmar(id):
        try:
            cursor.execute(
                "select * from citas where id = %s",
                (id)
            )
            return cursor.fetchall()
        except:
            return None
        
    @staticmethod
    def cancelar(id):
        try:
            cursor.execute(
                "delete from citas where id=%s",
                    (id)
            )
            conexion.commit()
            return True
        except:
            return False