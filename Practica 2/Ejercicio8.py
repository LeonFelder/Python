import collections
import string
palabra = input("Ingrese una palabra o frase: ").lower()
lista = []
for elem in palabra.split():
    for el in elem:
        if el in string.ascii_letters:
            lista.append(el)
cant = collections.Counter(lista).most_common(1)
if cant[0][1] == 1:
    print("Correcto")
else:
    print("Incorrecto")