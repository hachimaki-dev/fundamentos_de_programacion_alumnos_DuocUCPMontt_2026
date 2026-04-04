"""
Objetivo: Determinar el rango de clasificación para un afiliado de la agencia.

1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos "Daños Civiles (en costo monetario)" tuvo el héroe este mes.
2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime "Héroe Categoría S. Bono máximo!".
3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: "Héroe Categoría A. Cumple promedio".
4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: "Despedido. Demasiado caos".
5. Si no cae en lo de arriba: "Héroe en observación".
6. Programa las validaciones con los if, elif y else garantizando que todo tiene lógica correcta.
"""
Mision_exitosa = int(input("Cuantas misiones exitosas tuvo el heroe este mes? "))
Daños_Civiles = int(input("Cuantos fueron los daños Civiles este mes (En millones)? "))
if Mision_exitosa >= 10 and Daños_Civiles == 0:
    print("Héroe Categoría S. Bono máximo!")
elif Mision_exitosa  <= 9 and Mision_exitosa >= 5:
    print("Héroe Categoría A. Cumple promedio")
elif Mision_exitosa < 5 and Daños_Civiles > 10:
    print("Despedido. Demasiado caos")
else:
    print("Heroe en observacion")