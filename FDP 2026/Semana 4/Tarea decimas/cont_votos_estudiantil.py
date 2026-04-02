cant_votos_A = 0
cant_votos_C = 0
contador = 0

cant_estudiantes = int(input("Ingrese la cantidad de estudaintes que van a votar: "))

while contador < cant_estudiantes:
    voto = input(f"Ingresar voto de la persona {contador + 1}: ")

    if voto.lower() == "a":
        cant_votos_A += 1
    elif voto.lower() == "c":
        cant_votos_C += 1
    else:
        print("Voto nulo no contabilizazdo")

    contador += 1

if cant_votos_A > cant_votos_C:
    print(f"Ganó a favor con {cant_votos_A} votos")
elif cant_votos_C > cant_votos_A:
    print(f"Ganó en contra con {cant_votos_C} votos")
else:
    print(f"Empate con {cant_votos_A} votos cada uno")