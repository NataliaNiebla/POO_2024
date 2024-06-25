"""
5.- 
Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION


  imprimir la información
  """
  

pelis_dict={
    "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4","RAPIDO Y FURIOSO I "],
    "TERROR": ["LA MONJA", "EL CONJURO","LA MALDICIÓN"],
    "DEPORTES": ["ESPN", "MAS DEPORTE","ACCION"],
}

print("Bienvenido a la cartelera Cinepolis junio 2024")
print("Categorias disponibles: \n A) ACCION  \n B) TERROR \n C) DEPORTES")
buscar=input("Elige una categoria: ").upper()

if buscar=="A":
    print(pelis_dict["ACCION"])
elif buscar=="B":
    print(pelis_dict["TERROR"])
elif buscar=="C":
    print(pelis_dict["DEPORTES"])
else:
    print("Categoria no disponible")