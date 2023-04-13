def crearDiccionario (nombres,notas_1,notas_2):
    nombres = list(map(lambda x: x.replace("\n","").replace("'","").strip(" "), nombres.split(",")))
    return {nombre: (nota1,nota2) for nombre, nota1, nota2 in zip(nombres,notas_1,notas_2)}
def sacarPromedioAlumnos (notasAlumnos):
    return dict((dato[0],(dato[1][0]+dato[1][1])/2) for dato in notasAlumnos.items())
def sacarPromedioGeneral (promediosAlumnos):
    return sum(promediosAlumnos.values())/len(promediosAlumnos)
def notaMasAlta (notasAlumnos):
    return max(notasAlumnos.items(),key = lambda dato: dato[1])[0]
def notaMasBaja (notasAlumnos):
    return min(notasAlumnos.items(),key = lambda dato: dato[1])[0]

nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

notasAlumnos = crearDiccionario(nombres,notas_1,notas_2)
for alumno,notas in notasAlumnos.items():
    print(f"Las notas de {alumno} son {notas[0]} y {notas[1]}")
print('-'*30)
promedios = sacarPromedioAlumnos(notasAlumnos)
for alumno,promedio in promedios.items():
    print(f"El promedio de {alumno} es {promedio}")
print('-'*30)
print(f"El promedio del curso es {sacarPromedioGeneral(promedios):.2f}")
print('-'*30)
print("El alumno con la nota más alta es",notaMasAlta(promedios))
print('-'*30)
print("El alumno con la nota más baja es",notaMasBaja(notasAlumnos))