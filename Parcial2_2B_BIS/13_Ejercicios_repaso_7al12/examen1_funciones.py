import math

def solicitarDatos():
   print("\n")
#    global n1,n2,ope
   n1=(input("Numero #1: "))
   n2=(input("Numero #2: "))
   return n1,n2

def esperaTecla():
    print("Presiona cualquier tecla para continuar") 
    input()



def getCalculadora(num1,num2,operacion):
    
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        resultado=f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        resultado=f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        resultado=f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        resultado=f"{num1}/{num2}={int(num1)/int(num2)}"  
    elif operacion=="5" or operacion=="**" or operacion=="POTENCIA":
        resultado=f"{num1}**{num2}={int(num1)**int(num2)}"  
    elif operacion=="6" or operacion=="**" or operacion=="RAIZ NUMERO":
        resultado=math.sqrt(num1)
        resultado=math.sqrt(num2)
        return resultado