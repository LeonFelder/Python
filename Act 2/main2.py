import json, csv
from random import randrange
import  clases 

def obtengoDatos():
    opcion = randrange(2)
    if opcion == 0:
        archi = open("datos.json", "r")
        Datos=json.load(archi)
        archi.close()
    elif opcion == 1:
        try:
            archi = open("datos.csv", "r")
            csvreader = csv.reader(archi, delimiter=',')
            linea1 = next(csvreader)
            linea2 = next(csvreader)
            Datos = dict(zip(linea1, linea2))
            archi.close()
        except FileNotFoundError:
            print('No se encuentra el archivo deseado')
            raise
    else:
        Datos = {}
    return Datos
try:
    Datos = obtengoDatos()

    banda = clases.Banda(Datos['nombre'], Datos["genero"])

    print(banda)
except:
    print('Ocurrio un error')
else:
    print("FIN DEL PROGRAMA")