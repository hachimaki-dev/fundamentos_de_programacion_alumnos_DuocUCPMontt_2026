# Ranking de Superhéroes
# Objetivo: Determinar el rango de clasificación para un afiliado de la agencia.

# 1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos "Daños Civiles (en costo monetario)" tuvo el héroe este mes.
# 2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime "Héroe Categoría S. Bono máximo!".
# 3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: "Héroe Categoría A. Cumple promedio".
# 4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: "Despedido. Demasiado caos".
# 5. Si no cae en lo de arriba: "Héroe en observación".
# 6. Programa las validaciones con los if, elif y else garantizando que todo tiene lógica correcta.

misiones_exitosas = 0
costo_civiles = 0

print("*****Bienvenidos al ranking de Superhéroes*****")

misiones_exitosas = int(input("¿Cuántas misiones exitosas tiene el Superhéroe?: "))
costo_civiles = int(input("¿Cuánto daños civiles hizo el Superhéroe? (en costo monetario): "))

if misiones_exitosas >= 10 and costo_civiles == 0:
    print("Héroe Categoría S. Bono máximo!")
elif misiones_exitosas >= 5 and misiones_exitosas <= 9:
    print("Héroe Categoría A. Cumple promedio") 
elif misiones_exitosas < 5 and costo_civiles >= 10000000:
    print("Despedido. Demasiado caos")
else:
    print("Héroe en observación")

print("Fin del programa")