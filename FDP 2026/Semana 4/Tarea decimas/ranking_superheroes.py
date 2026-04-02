misiones_exitosas = int(input("Misiones exitosas: "))

costo_civil = int(input("Costo civil (Millones): "))

if misiones_exitosas >= 10 and costo_civil == 0:
    print("Héroe categoría S, ¡Bono máximo!")
elif misiones_exitosas >= 5 and misiones_exitosas <= 9:
    print("Héroe Categoría A. Cumple promedio")
elif misiones_exitosas < 5 and costo_civil > 10:
    print("Despedido. Demasiado caos")
else:
    print("Héroe en observación")