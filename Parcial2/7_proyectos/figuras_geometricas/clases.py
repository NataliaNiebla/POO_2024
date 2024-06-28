class Figuras:
    def __init__(self, x, y, visible):
        self.x=x
        self.y=y
        self.visible=visible
        
    #Getters y setters
    def getX (self):
        return self.x

    def setX(self,x):
      self.x=x
      
    def getY (self):
        return self.y

    def setY(self,y):
      self.y=y
      
    def getVisible(self):
        return self.visible

    def setVisible(self, visible):
        self.visible = visible
         
    def getInfo(self):
        pass

    # Metodos
    def esta_visible(self):
        return self.getVisible()

    def mostrar(self):
        self.setVisible(True)

    def ocultar(self):
        self.setVisible(False)

    def mover(self, dx, dy):
        self.setX(self.getX() + dx)
        self.setY(self.getY() + dy)
    
    def calcular_area(self):
        pass
        
        
class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.__alto=alto
        self.__ancho=ancho
        
    def getAlto(self):
        return self.__alto

    def setAlto(self, alto):
        self.__alto = alto
            
    def getAncho(self):
        return self.__ancho

    def setAncho(self, alto):
        self.__ancho = ancho
        
    def calcular_area(self):
        return self.__alto * self.__ancho
    
    def getInfo(self):
        print(f"X: {self.getX()}, Y: {self.getY()}, Visibilidad: {self.getVisible()}, Alto: {self.getAlto()}, Ancho: {self.getAncho()}, Área del rectángulo: {self.calcular_area()}")
    
class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.__radio = radio
        
    def getRadio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio = radio
             
    def calcular_area(self):
        import math
        return math.pi * self.__radio ** 2
    
    def getInfo(self):
        print(f"X: {self.getX()}, Y: {self.getY()}, Visibilidad: {self.getVisible()}, Radio: {self.getRadio()}, Área del círculo: {self.calcular_area()}")

    
    