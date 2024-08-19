def borrarPantalla():
    import os
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/Mac
        os.system('clear')

def esperarTecla():
  print("\n \t \t Oprima cualquier tecla para continuar ...")
  input()  
  
