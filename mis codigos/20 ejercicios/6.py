palabra = input("Ingrese una palabra ")
contador_a = 0

for letra in palabra:
    if letra == "a":
        contador_a += 1

print(f"Tu palabra tiene {contador_a} a's")
