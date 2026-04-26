misiones = int(input("ingresa la cantidad de misionsa exitosas: "))
costo_civil = float(input("Ingresa el costo en cantidad monetaria de daños civiles: "))
if misiones >= 10 and costo_civil == 0: 
    print("Heroe tier S. Darle bono maximo")
elif 5 <= misiones <= 9:
    print("Heroe Categoria A. Cumplimiento promedio")
elif misiones < 5 and costo_civil > 10000000:
    print("Despedido, Mucho costo monetario imposible mantener")
else:
    print("Heroe a prueba de lo que haga")