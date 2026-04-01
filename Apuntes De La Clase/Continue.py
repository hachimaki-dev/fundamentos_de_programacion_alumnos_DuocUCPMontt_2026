# continue: salta los pares
i = int(input("Seleccione un numero"))
for i in range(16):
    if i % 2 == 0:
        continue
    print(i)  # Imprime: 1,3,5