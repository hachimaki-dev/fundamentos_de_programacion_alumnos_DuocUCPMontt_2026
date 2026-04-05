# Ranking de Superhéroes
# Objetivo: Determinar el rango de clasificación para un afiliado de la agencia.

# 1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos "Daños Civiles (en costo monetario)" tuvo el héroe este mes.
# 2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime "Héroe Categoría S. Bono máximo!".
# 3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: "Héroe Categoría A. Cumple promedio".
# 4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: "Despedido. Demasiado caos".
# 5. Si no cae en lo de arriba: "Héroe en observación".
# 6. Programa las validaciones con los if, elif y else garantizando que todo tiene lógica correcta.

print(" RANKING DE SUPERHEROES ".center(40, "-"))

misiones_exitosas = int(input("Misiones exitosas: "))
danos_civiles = int(input("Danos civiles ($): "))

if misiones_exitosas >= 10 and danos_civiles == 0:
    print("Heroe Categoria S. ¡Bono maximo!")
elif misiones_exitosas >= 5 and misiones_exitosas <= 9:
    print("Heroe Categoría A. Cumple promedio")
elif misiones_exitosas < 5 and danos_civiles > 10000000:
    print("Despedido. Demasiado caos")
else:
    print("Heroe en observacion")
