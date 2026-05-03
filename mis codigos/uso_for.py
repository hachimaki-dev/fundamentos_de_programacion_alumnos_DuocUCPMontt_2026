
usuario = input("nombre: ")

for contador in range(9):
    usuario = input("si/no: ")
    if usuario == "si":
        contador += 1
    print(f"Contador: {contador}")