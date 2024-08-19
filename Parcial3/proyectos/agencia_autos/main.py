from revisiones import revision
from autos import auto
from clientes import cliente
from funciones import *
from usuarios import usuario
import getpass

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usuario=usuario.Usuario(nombre,apellidos,email,password)
            resultado=obj_usuario.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos} se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")    
            esperarTecla()
        elif opcion == '2':
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo  
            #Crear un objeto para utilizar los metodos 
            registro=usuario.Usuario.iniciar_sesion(email, password)
            if registro:
                menu_secundario(registro)
                
            else:
               print(f"\n\t ** Nombre de usuario y/o contraseña incorrectos, intentalo de nuevo ** ...")
               esperarTecla()          
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()
            
def menu_secundario(registro):
                print("""
                .::  Elige un menu ::. 
                    1.- Menu de AUTOS
                    2.- Menu de CLIENTES
                    3.- Menu de REVISIONES 
                    4.- Salir
                    """)
                opcion = input("\t Elige el número de opción que deseas elegir: ")
                if opcion=='1':
                    menu_autos(registro[0],registro[1],registro[2])
                elif opcion=='2':
                    menu_clientes(registro[0],registro[1],registro[2])
                elif opcion=='3':
                    menu_revisiones(registro[0],registro[1],registro[2])
                elif opcion == '4':
                    print("\n\t.. Regresando a menu principal ...")
                else: 
                    print("\n \t \t Opción no válida. Intenta de nuevo.")
                    esperarTecla()
                    
def menu_clientes(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(""".::  Menu CLIENTES ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion == 'INSERTAR':
            borrarPantalla()
            print(f"\n \t .:: Insertar registro de cliente ::. ")
            nif=int(input("\t NIF (número de identificación fiscal): "))
            nombre=input("\t Nombre: ").upper()
            direccion=input("\t Dirección: ").upper()
            ciudad=(input("\t Ciudad de procedencia: ")).upper()
            tel=int(input("\t Telefono: "))
            obj_cliente=cliente.Cliente(nif, nombre, direccion, ciudad, tel)
            resultado=obj_cliente.insertar()
            if resultado:
                print(f"\n \t \t .:: El registro del cliente {nombre} con NIF:{nif} se creo correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear el registro del cliente, por favor verifique ** ... ")    
            esperarTecla()
            
        elif opcion == '2' or opcion == 'CONSULTAR':
            borrarPantalla()
            print(f"\n \t .:: Consulta de clientes registrados ::. ")
            registros = cliente.Cliente.consultar()
            if len(registros) > 0:
                num_cliente = 1
                for fila in registros:
                    print(f"\n\t #Cliente: {num_cliente} \n\nNIF: {fila[0]} \nNombre: {fila[1]} \nDirección: {fila[2]} \nCiudad: {fila[3]} \nTelefono: {fila[4]}")
                    num_cliente+=1
            else:
                print(f"\n\t ** No hay registros de clientes disponibles** ...")
            esperarTecla()  

        elif opcion == "3" or opcion == 'ACTUALIZAR':
            borrarPantalla()
            print(f"\n \t .:: Actualización de registro de automoviles ::. ")
            nif = (input("Ingrese el NIF del cliente: "))
            nombre = input("Nuevo nombre del cliente: ").upper()
            direccion = input("Nueva dirección: ").upper()
            ciudad = input("Nueva ciudad de procedencia: ").upper()
            tel = int(input("Nuevo número telefonico: "))
            resultado=cliente.Cliente.actualizar(nombre, direccion, ciudad, tel, nif)
            if resultado:
                print("Registro del cliente actualizado correctamente.")
            else:
                print("Error al actualizar el registro del cliente.")
            esperarTecla()

        elif opcion == "4" or opcion == 'ELIMINAR':
            borrarPantalla()
            print(f"\n \t .:: Eliminar registro de automovil ::. ")
            nif = (input("Ingrese el NIF del cliente a eliminar: "))
            resultado=cliente.Cliente.eliminar(nif)
            if resultado:
                print("Registro de cliente eliminado correctamente.")
            else:
                print("Error al eliminar registro de cliente.")
            esperarTecla()
        
        elif opcion == '5' or opcion == 'SALIR':
            
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_autos(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(""".::  Menu AUTOS ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion == 'INSERTAR':
            borrarPantalla()
            print(f"\n \t .:: Insertar registro de automovil ::. ")
            matricula=(input("\t Matricula: ")).upper()
            marca=input("\t Marca: ").upper()
            modelo=input("\t Modelo: ").upper()
            color=input("\t Color: ").upper()
            nif=int(input("\t Nif (número de identificación fiscal): "))
            obj_auto=auto.Auto(matricula, marca, modelo, color, nif)
            resultado=obj_auto.insertar()
            if resultado:
                print(f"\n \t \t .:: El registro automovil con la matricula:{matricula} se creo correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear el registro del automovil, por favor verifique ** ... ")    
            esperarTecla()
            
        elif opcion == '2' or opcion == 'CONSULTAR':
            borrarPantalla()
            print(f"\n \t .:: Consulta de autos registrados ::. ")
            registros = auto.Auto.consultar()
            if len(registros) > 0:
                num_auto = 1
                for fila in registros:
                    print(f"\n\t #Revisión: {num_auto} \n\nMatricula: {fila[0]} \nNIF: {fila[4]} \nMarca: {fila[1]} \nModelo: {fila[2]} \nColor: {fila[3]}")
                    num_auto+=1
            else:
                print(f"\n\t ** No hay registros de automoviles disponibles** ...")
            esperarTecla()  

        elif opcion == "3" or opcion == 'ACTUALIZAR':
            borrarPantalla()
            print(f"\n \t .:: Actualización de registro de automoviles ::. ")
            matricula = (input("Ingrese la matricula del automovil: ")).upper()
            marca = input("Nueva marca del vehiculo: ").upper()
            modelo = input("Nuevo modelo del vehiculo: ").upper()
            color = input("Nuevo color del vehiculo: ").upper()
            nif = input("NIF (número de identificación fiscal): ").upper()
            resultado=auto.Auto.actualizar(marca, modelo, color, nif, matricula)
            if resultado:
                print("Registro del automovil actualizado correctamente.")
            else:
                print("Error al actualizar el registro del automovil.")
            esperarTecla()

        elif opcion == "4" or opcion == 'ELIMINAR':
            borrarPantalla()
            print(f"\n \t .:: Eliminar registro de automovil ::. ")
            matricula = (input("Ingrese la matricula del automovil: "))
            resultado=auto.Auto.eliminar(matricula)
            if resultado:
                print("Registro de automovil eliminado correctamente.")
            else:
                print("Error al eliminar registro de automovil.")
            esperarTecla()
        
        elif opcion == '5' or opcion == 'SALIR':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_revisiones(usuario_id,nombre,apellidos):
    while True:
        borrarPantalla()
        print(""".::  Menu REVISIONES ::. 
                  1.- Insertar
                  2.- Consultar
                  3.- Actualizar
                  4.- Eliminar
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion == 'INSERTAR':
            borrarPantalla()
            print(f"\n \t .:: Insertar revisión ::. ")
            no_revision=input("\t Número de revisión: ").upper()
            cambiofiltro=input("\t Cambio filtro (S/N): ").upper()
            cambioaceite=input("\t Cambio aceite (S/N): ").upper()
            cambiofrenos=input("\t Cambio frenos (S/N): ").upper()
            otros=input("\t Otros: ").upper()
            matricula=int(input(("\t Matricula: ")))
            obj_revision=revision.Revision(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
            resultado=obj_revision.insertar()
            if resultado:
                print(f"\n \t \t .:: La revision {no_revision} se creo correctamente ::. ")
            else:
                print(f"\n \t \t  ** No fue posible crear la revision, por favor verifique ** ... ")    
            esperarTecla()
            
        elif opcion == '2' or opcion == 'CONSULTAR':
            borrarPantalla()
            print(f"\n \t .:: Consulta de revisiones ::. ")
            registros = revision.Revision.consultar()
            if len(registros) > 0:
                num_revision = 1
                for fila in registros:
                    print(f"\n\t #Revisión: {num_revision} \n\nNo. revision: {fila[0]} \nMatricula: {fila[5]} \nCambio de filtro: {fila[1]} \nCambio de aceite: {fila[2]} \nCambio de frenos: {fila[3]} \nOtros: {fila[4]}")
                    num_revision+=1
            else:
                print(f"\n\t ** No hay revisión disponible** ...")
            esperarTecla()  

        elif opcion == "3" or opcion == 'ACTUALIZAR':
            borrarPantalla()
            print(f"\n \t .:: Actualización de revisión ::. ")
            no_revision = int(input("Ingrese el número de revisión a actualizar: "))
            cambiofiltro = input("Nuevo cambio de filtro (S/N): ").upper()
            cambioaceite = input("Nuevo cambio de aceite (S/N): ").upper()
            cambiofrenos = input("Nuevo cambio de frenos (S/N): ").upper()
            otros = input("Otros cambios: ").upper()
            matricula = int(input("Nueva matrícula del vehículo: "))
            resultado=revision.Revision.actualizar(cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
            if resultado:
                print("Revisión actualizada correctamente.")
            else:
                print("Error al actualizar la revisión.")
            esperarTecla()

        elif opcion == "4" or opcion == 'ELIMINAR':
            borrarPantalla()
            print(f"\n \t .:: Eliminar revisión ::. ")
            no_revision = int(input("Ingrese el número de revisión a eliminar: "))
            resultado=revision.Revision.eliminar(no_revision)
            if resultado:
                print("Revisión eliminada correctamente.")
            else:
                print("Error al eliminar la revisión.")
            esperarTecla()
        
        elif opcion == '5' or opcion == 'SALIR':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()
                
if __name__ == "__main__":
  menu_principal()
  