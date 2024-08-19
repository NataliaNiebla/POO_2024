#import conexiónBD   #Puedes manipular lo que hay dentro del archivo, SOLO LO QUE NECESITAS
from conexiónBD import*
#No puedes manipular lo que hay dentro del archivo
"""OBJETIVO: Realizar un registro dentro de alguna tabla"""

try:
    micursor=conexion.cursor()
    nombre=input("Favor de ingresar tu nombre: ")
    direccion=input("Favor de ingresar tu dirección: ")
    tel=input("Favor de ingresar tu número por favor: ")
    
    sql= "INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, %s, %s, %s)"
    valores=(nombre, direccion, tel)
    #micursor.execute(sql)
    micursor.execute(sql, valores)

    #Sirve para finalizar la ejecución del SQL de manera exitosa
    micursor=conexion.commit()
    
except:
    print("No se pudo insertar el registro correctamente")
else:
    print("Registro insertado exitosamente")

    """ para devolver el autoincremento a 1"""
    #ALTER TABLE nombre_tabla AUTO_INCREMENT = 1 