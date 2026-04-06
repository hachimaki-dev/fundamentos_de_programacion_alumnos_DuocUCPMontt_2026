import getpass

print("VOTOS ESTUDIANTILES")
contador_a_favor= 0
contador_en_contra= 0
N_encuestados= int(input("cuantas personas votaran? "))
N_votos= 0
while N_votos < N_encuestados:
    votos= getpass.getpass("Ingrese su voto (a favor/en contra)").lower()
    if votos == "a favor":
        contador_a_favor += 1
        N_votos += 1
    elif votos == "en contra":
        contador_en_contra += 1
        N_votos += 1
    else:
        print("voto no valido")
        N_votos += 1
        continue

print("resultados")
print(f"los votos a favor son {contador_a_favor}")
print(f"los votos en contra son {contador_en_contra}")
if contador_a_favor > contador_en_contra:
    print("el ganador es A FAVOR")
elif contador_a_favor == contador_en_contra:
    print("esto queda en EMPATE")
else:
    print("el ganador es EN CONTRA")