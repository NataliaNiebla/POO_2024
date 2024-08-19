from animales import animal
from citas import cita
from personas import *
from servicios import servicio
from veterinaria import veterinaria
import getpass
from funciones import *


def menu_introVeterinaria():
    while True:
        print("\n\t--- SISTEMA ADMINISTRADOR PETCO ---")
        print("\n Opciones del sistema disponibles \n!-Favor de elegir un número ")
        print("1. VETERINARIA")
        print("2. PERSONAS")
        print("3. ANIMALES")
        print("4. SERVICIO")
        print("5. CITAS")
        opcion = input("OPCIÓN: ").upper()

        if opcion == '1' or opcion == 'VETERINARIA':
            borrarPantalla()
            while True:
                nombre = input("Nombre: ").title()
                direccion = input("Dirección: ").title()
                telefono = input("Teléfono: ").title()
                cita = input("¿Deseas agendar una cita para este cliente? (si/no): ").upper()

            if cita == 'SI':
                borrarPantalla()
                tipo = "agendado"
                obj_cliente=personas.Cliente(nombre, direccion, telefono, tipo)
                cliente_nuevo=obj_cliente.agregar_cliente
                
                print("Gestor de citas")
                fecha = input("Fecha de la cita: ")
                obj_cita=cita.Cita(fecha, id_cliente, id_animal, id_empleado, id_servicio)
                cita_agendada=obj_cita.programar_cita()

            elif cita == 'NO':
                tipo = "noAgendado"
                obj_cliente=personas.Cliente(nombre, direccion, telefono, tipo)
                cliente_nuevo=obj_cliente.agregar_cliente

            else:
                print(f"\n \t \t  ** Favor de intentar nuevamente ** \n Presione ENTER para continuar ")
                

if __name__ == "__main__":
    menu_introVeterinaria()
