"""
Crear un programa que calcule y obtenga el total a pagar por un producto determinado. Se debera de solicitar el nombre o descripción del producto, codigo, cantidad, precio unitario. El total a pagar incluye el iva y el descuento. Si se compran de 1 a 5 productos se otorga el 10% de descuento, si se compran de 6 a 10 el 15% de descuento y si se compran más de 10 el 20% de descuento
""" 
contador_productos=1
while True:
    print("\t Bienevenido a Walmart")
    print()
    producto=input("Ingresa el producto que deseas conprar: ")
    descr=input(f"Ingresa la descripción de {producto}: ")
    codigo=int(input(f"Ingresa el codigo númerico de {producto}: "))
    cantidad=int(input(f"¿Cuál es la cantidad que dispones del producto {producto}: "))
    precio_u=input(f"Ingresa el precio marcado por unidad del producto {producto}: ")
    
    if cantidad>5:
        precio_u2=precio_u-(precio_u)
    
    precio_cantidad=precio_u*cantidad
    precio_iva=precio_cantidad*.16

    print(f"El precio ")
    
