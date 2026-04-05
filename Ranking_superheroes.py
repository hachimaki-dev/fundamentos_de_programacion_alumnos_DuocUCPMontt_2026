misiones= int(input("Ingrese las misiones exitosas del heroe: "))
daños_civiles= int(input("Ingrese los daños civiles (en costo monetario): "))

if misiones>= 10 and daños_civiles==0:
    print("Héroe Categoria S. Bono máximo!")
elif 5<=misiones<=9:
    print("Héroe Categoría A. Cumple promedio")
elif misiones<5 and daños_civiles>= 10000000:
    print("Despedido. Demasiado caos")
else:
    print("Héroe en observación")