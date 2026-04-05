print("Bienvenido al Ranking de Heroes!!!")
print("Descubre en que ranking de heroe estas...")

Misiones_exitosas = 0
Daños_civiles = 0

Misiones_exitosas = int(input("Ingresa la cantidad de misiones exitosas: "))
Daños_civiles = int(input("Ingresa la cantidad de daños civiles en dinero: "))
if Misiones_exitosas >= 10 and Daños_civiles == 0:
    print("Heroe categoria S. Bono maximo!")
elif Misiones_exitosas >= 5 and Misiones_exitosas <= 9:
    print("Heroe categoria A. Cumple promedio")
elif Misiones_exitosas <5 and Daños_civiles > 10000000:
    print("Despedido. Demasiado caosss")
else:
    print("Heroe en observacion...")








#1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos "Daños Civiles (en costo monetario)" tuvo el héroe este mes.
#2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime "Héroe Categoría S. Bono máximo!".
#3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: "Héroe Categoría A. Cumple promedio".
#4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: "Despedido. Demasiado caos".
#5. Si no cae en lo de arriba: "Héroe en observación".
#6. Programa las validaciones con los if, elif y else garantizando que todo tiene lógica correcta.