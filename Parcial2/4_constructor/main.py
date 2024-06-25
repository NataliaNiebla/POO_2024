from coches import*

#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches(("Blanco", "VW", "2022", 220, 150, 5))

coche1.getInfo()


print("Objeto 2")
coche2=Coches("azul", "Nissan", "2020", 180, 150, 6)

coche2.getInfo()


print("Objeto 3")
coche3=Coches("azul", "Audi", "2025", 240, 300, 6)

coche3.getInfo()
coche3.setColor("Gris")
coche3.getInfo()