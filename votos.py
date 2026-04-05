n = int(input("¿Cuantos estudiantes van a votar?  "))

contador_A = 0
contador_C = 0
i = 0

while i < n:
    voto = input("escribe por quien vas a votar (A/C):  ")

    if voto == "A":
        contador_A += 1
    elif voto == "C":
        contador_C += 1
    else:
        print("eso no esta permitido, porfavor contesta con las opciones disponibles")
    
    i += 1


    print(f"Votos a favor:", {contador_A} )
    print(f"Votos en contra:", {contador_C} )

if contador_A > contador_C:
        print("Gano la opcion A por mayoria de votos")
elif contador_C > contador_A:
    print("Gano la opcion C por mayoria de votos")
else:
     print("Empate!")