misiones_exitosas =int(input("ingrese cuantas misiones exitosas tuvo: "))
daños_civiles =int(input("ingrese el costo monetario de los daños civiles: "))
print("~~~RANKING DE SUPERHEROES~~~")

if misiones_exitosas >= 10 and daños_civiles == 0:
    print("Héroe Categoria S. Bono máximo!")

elif misiones_exitosas in range(5,10):
    print("Héroe Categoría A. Cumple promedio")

elif misiones_exitosas < 5 and daños_civiles > 10000000:
    print("Despedido. Demasiado caos")

else:
    print("Héroe en observación")