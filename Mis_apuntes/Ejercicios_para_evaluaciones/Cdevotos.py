A = 0
C = 0
estudiante = 1
encuestados = int(input("Cuantos estudiantes van a votar? "))
while estudiante <= encuestados:
    voto = input(f"Estudiante {estudiante}, ingrese su voto.    A) Favor    C) Contra. ")
    if voto == "A":
        A += 1
    elif voto == "C":
        C += 1
    else:
        print("Ingrese una opción válida.")
    estudiante += 1
print(f"Resultados a Favor : {A}.")
print(f"Resultados en contra : {C}.")
if A < C:
    print("Ganan los votos en Contra.")
elif A > C:
    print("Ganan los votos a Favor.")
elif A == C:
    print("Empate.")