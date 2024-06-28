from clases import Clientes, Empleados

cliente = Clientes("Ana Torres Guzman", "Col. Centro 1500 nte", "6181234567", 1234)
print(cliente.info_usuario())

empleado = Empleados("Daniel Fuentes Loera", "Fracc Alamedas 1300 nte", "6183335678", 1200.90, 123, "A")
print(empleado.info_usuario())