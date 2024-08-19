from conexionBD import *

class Revision:
    def __init__(self, no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
        self.no_revision=no_revision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiofrenos = cambiofrenos
        self.otros = otros
        self.matricula = matricula
        
    def insertar(self):
        try:
            cursor.execute(
                "insert into revisiones values(%s,%s,%s,%s,%s,%s)",
                (self.no_revision, self.cambiofiltro, self.cambioaceite, self.cambiofrenos, self.otros, self.matricula)
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
                "select * from revisiones"
            )
            return cursor.fetchall() # regresa tupla(s)
        except:
            return []   

    @staticmethod
    def actualizar(cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision):
        try:
            cursor.execute(
                "update revisiones set cambiofiltro=%s, cambioaceite=%s, cambiofrenos=%s, otros=%s, matricula=%s where no_revision=%s",
                (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False
     
    @staticmethod
    def eliminar(no_revision):
        try:
            cursor.execute(
                "delete from revisiones where no_revision=%s",
                (no_revision,) #la coma va pq solo asi se puede ejecutar
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

        
        