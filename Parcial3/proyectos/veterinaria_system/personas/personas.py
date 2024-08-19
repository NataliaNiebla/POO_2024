class Persona:
    def __init__(self, nombre, apellidos, telefono, domicilio):
        self.nombre=nombre
        self.apellidos=apellidos
        self.telefono=telefono
        self.domicilio=domicilio  
     
    @staticmethod  
    def actualizar_datos(id, nombre, apellidos, telefono, domicilio):
      try:
          cursor.execute(
            "update personas set nombre=%s,apeliidos=%s, telefono=%s, domicilio=%s where id=%s",
            (titulo,descripcion,id)
        )
          conexion.commit()
          return True
      except:
         return False

class Cliente(Persona):
    def _init_(self, nombre, apellidos, telefono, domicilio, metodo_pago, registros):
      super._init_(nombre, apellidos, telefono, domicilio)
      self.metodo_pago=metodo_pago
      self.registros=registros
      
    def visualizar_info(self):
            print(f"Nombre: {self.nombre}")
            print(f"Apellidos: {self.apellidos}")
            print(f"Teléfono: {self.telefono}")
            print(f"Domicilio: {self.domicilio}") 
            print(f"Metodo de pago: {self.metodo_pago}") 
            print(f"Registros previos: {self.registros}") 
            
    def agregar_animal(self):
      pass
      
class Empleado(Persona):
    def _init_(self, nombre, apellidos, telefono, domicilio, salario, puesto):
      super._init_(nombre, apellidos, telefono, domicilio)
      self.salario=salario
      self.puesto=puesto
      
    def visualizar_info(self):
            print(f"Nombre: {self.nombre}")
            print(f"Apellidos: {self.apellidos}")
            print(f"Teléfono: {self.telefono}")
            print(f"Domicilio: {self.domicilio}") 
            print(f"Salario: {self.salario}")
            print(f"Puesto: {self.puesto}") 
            
    def atender_cita(self):
      pass
    