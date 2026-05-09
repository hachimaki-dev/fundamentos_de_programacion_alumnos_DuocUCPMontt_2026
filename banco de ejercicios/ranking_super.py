""" Objetivo: Determinar el rango de clasificación para un afiliado de la agencia.

1. El usuario debe ingresar dos cosas: cuántas "Misiones Exitosas" y cuántos 
"Daños Civiles (en costo monetario)" tuvo el héroe este mes.

2. Si tiene 10 o más misiones exitosas Y el costo civil es 0: Imprime 
"Héroe Categoría S. Bono máximo!".

3. Si tiene entre 5 y 9 misiones exitosas, sin importar los daños: 
"Héroe Categoría A. Cumple promedio".

4. Si tiene menos de 5 misiones, pero los daños superaron 10 millones: 
"Despedido. Demasiado caos".

5. Si no cae en lo de arriba: "Héroe en observación".

6. Programa las validaciones con los if, elif y else garantizando que todo tiene 
lógica correcta."""

misiones_exitosas = int(input("ingresa el numero de misones exitosas: "))
daño = int(input("ingresa el valo de daño que hizo en este mes: "))

if misiones_exitosas > 10 and daño == 0:
    print("categoria S . bono maximo")

elif misiones_exitosas > 0 and misiones_exitosas < 10 and daño < 10000000:
    print(" heroe categoria A. cumple promedio")

elif misiones_exitosas < 5 and daño > 10000000:
    print("despedido . demasiado caos")

else:
    print("heroe en observacion")
    