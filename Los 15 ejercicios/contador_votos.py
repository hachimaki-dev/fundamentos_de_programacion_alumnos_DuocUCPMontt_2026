print("B I E N V E N I D O S   A   L A   V O T A C I O N   D E   L A  S E C CI O N  002D ")

votos_a_favor = 0
votos_en_contra = 0

numero_encuestados = int(input("¿Cuantos Estudiantes van a Votar?"))

V = 0

while V < numero_encuestados:
    voto = input("Escribe A (a favor) o C (en contra): ")

    if voto == "A":
        votos_a_favor += 1
    elif voto == "C":
        votos_en_contra += 1
    else:
        print("Voto nulo no contabilizado")

    V += 1


if votos_a_favor > votos_en_contra:
    print("Ganó A favor")
elif votos_en_contra > votos_a_favor:
    print("Ganó En Contra")
else:
    print("Empate")

