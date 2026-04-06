print("¡Ranking de superhéroes! Ingresa la información del héroe.")
misiones_exitosas = int(input("Misiones exitosas: "))
costo_civil = int(input("Daños civiles (en costo monetario): $"))

if misiones_exitosas >= 10 and costo_civil == 0:
    print("Héroe categoría S. ¡Bono máximo!")
elif misiones_exitosas >= 5:
    print("Héroe categoría A. Cumple el promedio.")
elif misiones_exitosas < 5 and costo_civil >= 10000000:
    print("Héroe despedido. Demasiado caos.")
else:
    print("Héroe en observación.")
