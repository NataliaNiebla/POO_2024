#formas de concatenación en python
nombre="Natalia Niebla Rosales"
especialidad= "Área de software multiplataforma"
carrera="Ingeniería en gestión y desarrollo de SW"

#1er forma
print("1. Mi nombre es "+ nombre + " estoy en la especialidad de "+ especialidad + " en la carrera de "+ carrera )
print("\n")
#print("\n")  :salto de linea
#print(\t)  :tabulación
#print("\"")  :comillas

#2da forma
print("2. Mi nombre es ", nombre , " estoy en la especialidad de ", especialidad , " en la carrera de ", carrera )
print("\n")

#3ra forma  MÁS COMÚN EN PYTHON
print(f"3. Mi nombre es , {nombre} , estoy en la especialidad de , {especialidad} ,  en la carrera de , {carrera}")
print("\n")

#4ta forma PROPIA DE PYTHON
print("4. Mi nombre es , {} , estoy en la especialidad de , {} ,  en la carrera de , {}".format(nombre, especialidad,carrera))
print("\n")

#5ta forma
print('5. Mi nombre es '+ nombre + ' estoy en la especialidad de '+ especialidad + ' en la carrera de '+ carrera )
print("\n")