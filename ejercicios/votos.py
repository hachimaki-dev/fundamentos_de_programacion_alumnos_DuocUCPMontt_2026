print("###bienvenido###")
contra = 0
a_favor = 0
algo = 0
encuestados = int(input("ingrese el numero de encuestados"))
while algo != encuestados :
    voto = (input("elija su voto, A = a favor, C = contra"))
    if voto == "A" :
        print("voto realizado")
        a_favor = a_favor + 1
        algo = algo + 1
    elif voto == "C" :
        print("voto realizado")
        contra = contra + 1
        algo = algo + 1
    elif voto != "A" and "C" :
        print("voto nulo, no contabilizado")
        algo = algo + 1

print("fin de los votos")
if a_favor < contra :
    print(f"gana en contra con {contra} votos")
elif a_favor > contra :
    print(f"gana a favor con {a_favor} votos")
elif a_favor == contra :
    print("empate")