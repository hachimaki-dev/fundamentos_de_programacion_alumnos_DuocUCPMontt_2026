#pedir datos al usuario 
misiones = (int(input("Ingrese el número de misiones realizadas: ")) )
daños = (int(input("Ingrese el número de años en servicio: ")) )

#evaluar las condiciones 
if misiones >= 10 and daños == 0:
    print(" Héroe categoría S. Bono máximo!!!")
elif 5 <= misiones <= 9:
    print(" Héroe categoría A. cumple promedio!.")
elif misiones < 5 and daños == 10000000:
    print("Despedido. demasiado caos.")
else:
    print("Heroe en observación.")          