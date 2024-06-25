contador_pacientes=0
reg_totales=[]

while True:
    ("\n Calculo de IMC")

    peso=float(input("Ingrese su peso por favor(kg): "))
    altura=float(input("Ingrese su altura por favor(m): "))

    imc=altura*altura
    imc2=peso/imc

    print()

    if imc2<18.5:
        print(f"Peso inferior al normal \nIMC:{imc2}")
    elif imc2>=18.5 and imc2<25:
        print(f"Peso normal \nIMC:{imc2}")
    elif imc2>=25 and imc2<30:
        print(f"Peso superior al normal \nIMC:{imc2}")
    else:
        print(f"Obesidad \nIMC:{imc2}")

    contador_pacientes+=1
    
    x=input("Desea agregar otro registro? (Si/No)").upper()
    if x!="SI":
        break
    
if contador_pacientes==1:
    print(f"Se regitraron {contador_pacientes} registro")
else:
    print(f"Se regitraron {contador_pacientes} registros")