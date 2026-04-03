misiones = int(input("¿cuantas misiones exitosa este mes?"))
daños = int(input("¿daños civiles (costo monetario) de este mes?"))

if misiones >= 10 and daños == 0:
    print("¡Heroe categoria S bono maximo")
elif misiones >= 5 or misiones <= 7:
    print("Heroe categoria A cumple lo promedio")
if misiones < 5 and daños > 10000000:
    print("despedido demasiado caos")
else:
    print("Heroe en observacion")
