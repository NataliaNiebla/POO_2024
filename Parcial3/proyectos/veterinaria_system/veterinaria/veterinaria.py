from conexiónBD import*
from personas import Cliente
from personas import empleados

class Veterinaria:
    def __init__(self, nombre, direccion, telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        
    def agregar_cliente(self):
        try:
            cursor.execute(
                "insert into clientes values (null,%s,%s,%s,%s)",
                (self.nombre,self.direccion,self.telefono,self.tipo)
                )
            conexion.commit()
            return True
        except:
            return False
        
    def agregar_empleado(self):
        try:
            cursor.execute(
                "insert into empleados values (null,%s,%s,%s,%s,%s)",
                (self.fecha,self.direccion,self.telefono,self.puesto,self.salario)
                )
            conexion.commit()
            return True
        except:
            return False
        
    def programar_cita(self, id_cliente, id_animal, id_empleado, id_servicio):
        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into citas values (null, fecha, %s,%s,%s,%s)",
                )
            conexion.commit()
            return True
        except:
            return False   

    def agregar_servicio(self):
        try:
            cursor.execute(
                "insert into servicios values (null,%s,%s,%s,%s,%s)",
                (self.nombre,self.descripcion,self.costo)
                )
            conexion.commit()
            return True
        except:
            return False
    