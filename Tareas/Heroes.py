print("Bienvenido al Ranking de heroes de PYTHONNNNN")
misiones = int(input("¿Cuantas misiones exitosas ha tenido tu heroe? (Responder con numeros) "))
daños = int(input("¿Cuantos es el costo de daño a Civiles? "))

if misiones >=10 and daños == 0:
    print("EXCELENTE. TU HEROE ES CATEGORIA S, como Saitama")
elif misiones <= 9 and misiones >=5:
    print("PERFECTO, Tu HEROE ES CATEGORIA A, como Genos")
elif misiones < 5 and daños > 10000000:
    print("Nada que hacerle, tu heroe esta despedido")
else:
    print("Tu heroe estara siendo analizado, nivel del ciclista sin licencia")