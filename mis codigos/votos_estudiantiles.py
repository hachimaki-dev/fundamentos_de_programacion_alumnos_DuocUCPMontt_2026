# TERMINADO :3


print("===== VOTACIONES ESTUDIANTILES =====")



numero_estudiantes_encuestados = int(input("cuantos estudiantes votaran?:"))

votos_A = 0
votos_B = 0

while votos_A + votos_B < numero_estudiantes_encuestados:
    voto = input("¿a que candidato votaras? (A/B):")

    if voto == "a" or voto == "A":
        votos_A += 1
        print("!voto registrado!")


    elif voto == "b" or voto == "B":
        votos_B += 1
        print("!voto registrado!")

    elif votos_A + votos_B == numero_estudiantes_encuestados:
        print("votacion finalizada")
        break

    elif voto != "a" and voto != "A" and voto != "b" and voto != "B":
        print("opcion invalida, intenta de nuevo")
        continue
    


print("=====================================")
print("===== RESULTADO DE LA VOTACION =====")
print(f"Candidato A: {votos_A} votos")
print(f"Candidato B: {votos_B} votos")

if votos_A > votos_B:
    print(f"El ganador es el candidato A")
elif votos_B > votos_A:
    print(f" El ganador es el candidato B")
else:
    print("¡Es un EMPATE!")
print("=====================================")
