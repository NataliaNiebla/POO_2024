from figuras import*

def main():
    rectangulo = Rectangulo(largo=5.0, ancho=3.0)
    circulo = Circulo(radio=4.0)
    triangulo = Triangulo(altura=6.0, ancho=4.0)

    print(f"Área del rectángulo: {rectangulo.calcular_area()}")
    print(f"Área del círculo: {circulo.calcular_area()}")
    print(f"Área del triángulo: {triangulo.calcular_area()}")

if _figuras_ == "_main_":
    main()
