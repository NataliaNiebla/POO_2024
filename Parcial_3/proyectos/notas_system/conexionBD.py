import mysql.connector    #libreria/ dependencia a instalar

try:
    conexion=mysql.connector.connect(      #objeto de conexion, 
        host='localhost',    #o tambien la url:127.0.0.1
        user='root',         #random
        password='',         #no hay contraseña aún
        database='bd_notas'     
    )
    
    #Se crea un objetos de tipo cursor con una parametro que permite reutilizar el mismo objeto
    cursor=conexion.cursor(buffered=True) #para todas las conexiones
    
except Exception as e:
    print(f"Error: {e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"Ocurrio un error en el servidor, vuelve a intentar")

else: #si no existe ninguna excepción
    if conexion.is_connected():
        print("Se creo la conexion o base de datos correctamente")
    else:     #pq no se instalo la libreria, no hay user, la contra es incorrecta, la base de datos no existe
        print("No fue posible conectar con la base de datos, verifique")
    
"""
xamp---star apache y mysql
127.0.0.1 phpmyadmin--- bases de datos
"""