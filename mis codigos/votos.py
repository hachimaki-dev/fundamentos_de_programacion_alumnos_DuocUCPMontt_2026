print("Bienvenido al contador de votos estudiantil")

encuestados = int(input("¿cuantos estudiantes participan?: "))
votos_c = 0
votos_a = 0
ciclo = 0

while ciclo < encuestados:
    voto = input("ingrese voto a favor (A) / voto en contra (C): ")

    if voto == "a":
        votos_a += 1
    elif voto == "c":
        votos_c += 1
    else:
        print("voto nulo")

    ciclo += 1

print("Resultados")
if votos_a > votos_c:
    print("Ganador, a favor.")
elif votos_c > votos_c:
    print("Ganador, en contra.")
else:
    print("empate")


    

