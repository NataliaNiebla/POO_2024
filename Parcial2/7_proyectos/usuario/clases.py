class Usuarios:
    def __init__ (self, nombre, direccion, telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        
    def info_usuario(self):
       print(f"Nombre: {self.getNombre()}, Dirección: {self.getDireccion()}, Teléfono: {self.getTelefono()}")
        
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre
        
    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self, direccion):
        self.direccion=direccion
        
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono=telefono
        
class Clientes(Usuarios):
    def __init__(self, nombre, direccion, telefono, num_cliente):
        super().__init__(nombre, direccion, telefono)
        self.__num_cliente=num_cliente
        
    def getNum_cliente(self):
        return self.__num_cliente
    
    def setNum_cliente(self, num_cliente):
        self.__num_cliente=num_cliente  
        
    def info_usuario(self):
        print (f"Nombre: {self.getNombre()}, Dirección: {self.getDireccion()}, Teléfono: {self.getTelefono()}, No. Cliente: {self.getNum_cliente()}")
    
###
class Empleados(Usuarios):
    def __init__(self, nombre, direccion, telefono, salario, num_empleado, tipo):
        super().__init__(nombre, direccion, telefono)
        self._salario=salario
        self._num_empleado=num_empleado
        self._tipo=tipo
        
    def getSalario(self):
        return self._salario
    
    def setSalario(self, salario):
        self._salario=salario
        
    def getNum_empleado(self):
        return self._num_empleado
    
    def setNum_empleado(self, num_empleado):
        self._num_empleado=num_empleado
        
    def getTipo(self):
        return self._tipo
    
    def setTipo(self, tipo):
        self._tipo=tipo
        
    def info_usuario(self):
        print( f"Nombre: {self.getNombre()}, Dirección: {self.getDireccion()}, Teléfono: {self.getTelefono()}, Salario: {self.getSalario()}, No. Empleado: {self.getNum_empleado()}, Tipo: {self.getTipo()}")
        