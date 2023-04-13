frase = input("Ingrese una frase: ").split()
search = input("Ingrese una palabra a buscar: ")
cant = 0
for elem in frase:
    if search.lower() in elem.lower():
        cant += 1
print(f"La palabra {search} fue mencionada {cant}")