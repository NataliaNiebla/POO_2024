class Coches:
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #Valores iniciales es posible declarar al principio de una clase
    marca="ferrari"
    color="rojo"
    modelo="2010"
    velocidad=300
    caballaje=500
    plazas=2
    
    #Metodos o acciones o funciones que hace el objeto
    
    def acelerar(self):
        self.velocidad+=1
    
    def frenar(self):
        self.velocidad-=1
        
    #Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches()

"""
#Crear los metodos setters y getters; estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos; digamos que es la manera más adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto.

#En teoria se deberia de crear un metodo Getters y stters por cada atributo que contenga la clase

#Los metodos get siempre regresan un valor es decir, el valor de la propiedad a traves del return

#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestión 
"""

def getColor (self):
    return self.color

def setColor (self, color):
    self.color=color

def getMarca (self):
    return self.marca

def setMarca (self, marca):
    self.marca=marca
    
def getModelo (self):
    return self.modelo

def setModelo (self, modelo):
    self.modelo=modelo
    
def getVelocidad (self):
    return self.marca

def setVelocidad (self, velocidad):
    self.velocidad=velocidad
    
def getCaballaje (self):
    return self.caballaje

def setCaballaje (self, caballaje):
    self.caballaje=caballaje

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2=coches()
coche2.marca="Porsche"
coche2.color="Amarillo"
coche2.modelo="2018"
coche2.velocidad=250
coche2.caballaje=340
coche2.plazas=4

print(f"Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp")