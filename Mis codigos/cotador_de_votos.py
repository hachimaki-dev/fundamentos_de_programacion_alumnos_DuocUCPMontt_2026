n_de_votantes = int(input("¿Cuantos estudiantes votaran?"))

contador_de_votos_a = 0

contador_de_votos_c = 0

while True:
    voto_de_estudiante = input("Vota A o C")
    if voto_de_estudiante == "A":
        print("Voto para A")
        contador_de_votos_a += 1
    elif voto_de_estudiante == "C":
        print("Voto para C")
        contador_de_votos_c += 1
    elif voto_de_estudiante != "A or C":
        print("Ingrese un voto valido")
    if n_de_votantes == contador_de_votos_a + contador_de_votos_c:
        break

if contador_de_votos_a>contador_de_votos_c:
    print("Gano A favor")
elif contador_de_votos_c>contador_de_votos_a:
    print("Gana En Contra")
elif contador_de_votos_a==contador_de_votos_c:
    print("Hubo un Empate")
    



