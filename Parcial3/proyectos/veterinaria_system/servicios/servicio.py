class Servicio:
    def __init__(self, nombre, descripcion, costo):
        self.nombre=nombre
        self.descripcion=descripcion
        self.costo=costo
    
    @staticmethod     
    def actualizar_costo(id, costo):
        try:
          cursor.execute(
            "update servicios set costo=%s where id=%s",
            (costo,id)
        )
          conexion.commit()
          return True
        except:
         return False
     
class Vacuna(Servicio):
    def __init__(self, nombre, descripcion, costo, tipo):
        super._init_(tipo) 
        self.tipo=tipo
        
    def administrar_vacuna(self):
        pass
    
class Consulta(Servicio):
    def __init__(self, nombre, descripcion, costo, duracionn):
        super._init_(duración) 
        self.duracion=tipo
        
    def realizar_consulta(self):
        pass
    