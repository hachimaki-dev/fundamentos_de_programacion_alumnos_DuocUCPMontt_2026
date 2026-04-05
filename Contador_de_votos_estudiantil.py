votantes=int(input("Ingrese el número de estudiates que van a votar: "))
a_favor=0
en_contra=0
número_de_votos=0

while número_de_votos<=votantes:
    voto= input("Escriba (A), si vota a favor o (C), si vota en contra: ")
    if voto== "A":
        a_favor+=1
        número_de_votos+=1
    elif voto== "C":
        en_contra+=1
        número_de_votos+=1
    elif voto !="A" or voto !="C":
        print("Voto nulo no contabilizado")
        número_de_votos+=1
if a_favor>en_contra:
    print("Ganó A Favor")
elif a_favor<en_contra:
    print("Ganó En Contra")
elif a_favor==en_contra:
    print("Empate")