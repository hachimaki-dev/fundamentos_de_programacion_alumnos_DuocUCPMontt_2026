success_mission = int(input("Ingrese el número de misiones exitosas: ") )
civil_damage = int(input("Ingrese el daño civil: ") )
if success_mission >= 10 and civil_damage == 0:
    print("Héroe Categoría S. Bono máximo!")
elif 5 <=success_mission <= 9:
    print("Héroe Categoría A. Cumple promedio!")
elif success_mission < 5 and civil_damage > 10000000:
    print("Despedido. Demasiado caos")
else:
    print("Héroe en observación")