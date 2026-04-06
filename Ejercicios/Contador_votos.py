voto_A = 0
voto_C = 0
n_encuestados = int(input("¿Cuantos estudiantes van a votar? "))
contador_n_encuestados = 1
while n_encuestados >= contador_n_encuestados:
    voto = input("¿A quien votaras entre A y C? ")
    if voto == 'A':
        voto_A = voto_A + 1
        contador_n_encuestados = contador_n_encuestados + 1
    elif voto == 'C':
        voto_C = voto_C + 1
        contador_n_encuestados = contador_n_encuestados + 1
    else:
        print("Voto nulo no contabilizado")
        contador_n_encuestados = contador_n_encuestados + 1
if voto_A > voto_C:
    print("Ganó A a favor")
elif voto_C > voto_A:
    print("Ganó C en contra")
elif voto_A == voto_C:
    print("Empate")
