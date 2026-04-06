import random
Numero_Encuestados = print("Numero de personas encuestadas fueron 31")
print("B")
print("A")
print ("Simulacion de Votos")
B = 0
A = 0
nulo = 0
for i in range (31):
    voto = random.choice(["A", "B", "Nulo"])
    if voto == "A" or voto == "a":
        A= A + 1
        print(f"Voto {A+1}: voto para A")
    elif voto == "B" or voto == "b":
        B = B + 1
        print(f"voto {B+1}: voto para B")
    else:
        nulo= nulo + 1
        print(f"voto {nulo+1}: voto nulo")
print(f"resultado finales: ")
print(f"votos para A: {A} ")
print(f"Votos para B: {B} ")
print(f"votos nulos: {nulo} ")
if A> B:
    print("Ha ganado Candidato A")
elif B> A:
    print("Ha ganado Candidato B")
if A == B:
    print("Empate nadie gana")
    
    
    


