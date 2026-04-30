
palabra = "manzana"
letra_a = "a"
contador_a = 0

for letra in palabra:
    if letra in letra_a:
        contador_a += 1

print(f"{contador_a}")
