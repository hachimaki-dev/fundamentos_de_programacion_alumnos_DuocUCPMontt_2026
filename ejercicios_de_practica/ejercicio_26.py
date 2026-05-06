hojas_por_imprimir = ["TEXT0", "F0T0", "TEXT0", "F0T0"]
hojas_restantes = 5

for hojas in hojas_por_imprimir:
    if hojas_restantes <= 0:
        print("Sin papel")
        break
    if hojas == "TEXT0":
        print(f"Imprimiendo TEXTO")
        hojas_restantes -= 1
    if hojas == "F0T0":
        print(f"Imprimiendo FOTO")
        hojas_restantes -= 3