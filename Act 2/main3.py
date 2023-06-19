import json
import csv
from random import randrange
import  clases 

def obtengo_datos():
    opcion = randrange(2)
    if opcion == 0:
        archi = open("datos.json", "r")
        datos=json.load(archi)
        archi.close()
    elif opcion == 1:
        archi = open("datos.csv", "r")
        csvreader = csv.reader(archi, delimiter=',')
        linea1 = next(csvreader)
        linea2 = next(csvreader)
        datos = dict(zip(linea1, linea2))
        archi.close()
    else:
        datos = {}
    return datos

datos = obtengo_datos()

banda = clases.Banda(datos['nombre'], datos["genero"])

print(banda)
print("FIN DEL PROGRAMA")