class Personas:
    def __init__(self, nombre, edad, telefono):
        self.nombre=nombre
        self.edad=edad
        self.telefono=telefono
        
    def info_persona(self):
        print (f"Nombre: {self.getNombre()} \nEdad: {self.getEdad()} \nTelefono:{self.getTelefono()}")
        
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
        
    def getEdad(self):
        return self.edad 
    def setEdad(self, edad):
        self.edad=edad
        
    def getTelefono(self):
        return self.telefono
    def setTelefono(self, telefono):
        self.telefono=telefono
    
class Estudiantes(Personas):
    def __init__(self, nombre, edad, telefono, carrera, matricula):
        super().__init__(nombre, edad, telefono)
        self.__carrera=carrera
        self.__matricula=matricula
        
    def info_persona(self):
        print (f"Nombre: {self.getNombre()} \nEdad: {self.getEdad()} \nTelefono:{self.getTelefono()} \nCarrera: {self.getCarrera()} \nMatricula: {self.getMatricula()}")
        
    def informar_carrera(self):
        print(f"El estudiante {self.getNombre()} esta cursando la carrera de {self.getCarrera()}")
        
    def getCarrera(self):
        return self.__carrera
    def setCarrera(self, carrera):
        self.__carrera=carrera
        
    def getMatricula(self):
        return self.__matricula
    def setMatricula(self, matricula):
        self.__matricula=matricula
        
class Docentes(Personas):
    def __init__(self, nombre, edad, telefono, modalidad, num_empleado):
        super().__init__(nombre, edad, telefono)
        self._modalidad=modalidad
        self._num_empleado=num_empleado
        
    def info_persona(self):
        print (f"Nombre: {self.getNombre()} \nEdad: {self.getEdad()} \nTelefono:{self.getTelefono()} \nModalidad: {self.getModalidad()} \nNúmero de empleado: {self.getNumEmpleado()}")
        
    def informar_modalidad(self):
        print(f"El docente {self.getNombre()} pertenece a la modalidad de {self.getModalidad()}")

    def getModalidad(self):
        return self.__carrera
    def setModalidad(self, modalidad):
        self._modalidad=modalidad
        
    def getNumEmpleado(self):
        return self._num_empleado
    def setModalidad(self, num_empleado):
        self._num_empleado=num_empleado
    
    

    