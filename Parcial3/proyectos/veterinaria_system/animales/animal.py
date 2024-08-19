class Animal:
    def __init__ (self, nombre, raza, edad, id_cliente):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.id_cliente=id_cliente
        
    @staticmethod   
    def actualizar_historial(id, nombre, raza, edad, id_cliente):
       try:
         cursor.execute(
            "update animal set nombre=%s,raza=%s, edad=%s, id_cliente=%s, where id=%s",
            (nombre,raza,edad, id_cliente, id)
         )
         conexion.commit()
         return True
       except:
         return False  