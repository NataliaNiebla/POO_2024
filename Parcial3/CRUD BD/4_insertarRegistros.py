#import conexiónBD   #Puedes manipular lo que hay dentro del archivo, SOLO LO QUE NECESITAS
from conexiónBD import*
#No puedes manipular lo que hay dentro del archivo

micursor=conexion.cursor()

sql= "INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, 'Natalia Niebla', 'Sierra de topia 122 fracc.Los Fresnos', '6183015090')"

micursor.execute(sql)

#Sirve para finalizar la ejecución del SQL de manera exitosa
micursor=conexion.commit()
print("Registro insertado exitosamente")