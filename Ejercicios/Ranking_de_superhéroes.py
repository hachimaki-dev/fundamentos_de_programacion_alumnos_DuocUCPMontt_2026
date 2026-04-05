misiones = int(input("Ingresa la cantidad de misiones exitosas: "))
daños_civiles = int(input("Ingresa el costo monetario de los daños civiles: "))

if misiones >= 10 and daños_civiles == 0:
    print("Héroe Categoría S. Bono máximo!")

elif 5 <= misiones <= 9:
    print("Héroe Categoría A. Cumple promedio")

elif misiones < 5 and daños_civiles > 10000000:
    print("Despedido. Demasiado caos")

else:
    print("Héroe en observación")

