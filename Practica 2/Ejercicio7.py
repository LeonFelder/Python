import string
def dividir (tex):
    return tex.split()
texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""
cantidades = {"Mayusculas":0,"Minusculas":0,"No letras":0}
for elem in texto.split():
    for el in elem:
        if el in string.ascii_lowercase:
            cantidades["Minusculas"] += 1
        elif el in string.ascii_uppercase:
            cantidades["Mayusculas"] += 1
        elif not(el in string.ascii_letters):
            cantidades["No letras"] += 1
print(cantidades)
print(len(texto.split()))