print("=== Bienvenido seas a la APG, [Aseguracion de Proteccion Gobal] ===")
print("=== Aqui nos aseguramos de que todo flulla y mantener la seguridad de los civiles ===")
print("=== Pero tambien nos aseguramos de que los héroes novatos se mantenga estables ===")

misiones = int(input("Ingrese la cantidad de misiones exitosas: "))
daños = int(input("Ingrese el costo de daños civiles: "))

if misiones > 10 and daños == 0:
    print("Héroe Categoría S. Bono máximo")

elif misiones >= 5 and misiones <= 9:
    print("Héroe Categoría A. Cumple promedio")

elif misiones < 5 and daños > 10000000:
    print("Despedido. Demasiado caos")

else:
    print("Héroe en observación")