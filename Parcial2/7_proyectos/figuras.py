class Figura():
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def _init_(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def getLargo(self):
        return self._largo
    def setLargo(self, value):
        self._largo = value

    def getAncho(self):
        return self._ancho
    def setAncho(self, value):
        self._ancho = value

    def calcular_area(self):
        return self.largo * self.ancho

class Circulo(Figura):
    def _init_(self, radio):
        self.radio = radio

    def getRadio(self):
        return self._radio
    def setRadio(self, value):
        self._radio = value

    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def _init_(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def getAltura(self):
        return self._altura
    def setAltura(self, value):
        self._altura = value

    def getAncho(self):
        return self._ancho
    def setAncho(self, value):
        self._ancho = value

    def calcular_area(self):
        return 0.5 * self.ancho * self.altura