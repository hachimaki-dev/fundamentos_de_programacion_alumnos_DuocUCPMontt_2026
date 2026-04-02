votos_a_favor = 0
votos_en_contra = 0
contador_de_votos = 1

cantidad_de_encuestados = int(input("¿Cuántos estudiantes van a votar?: "))

while contador_de_votos <= cantidad_de_encuestados:
    voto = input(f'\nEstudiante {contador_de_votos}, por favor ingrese su voto. Escribe "A" si estás a favor y "C" si estás en contra.\nVoto: ')
    if voto == "A" or voto == "a":
        votos_a_favor += 1
        contador_de_votos += 1
        print("Voto procesado.")
    elif voto == "C" or voto == "c":
        votos_en_contra += 1
        contador_de_votos += 1
        print("Voto procesado.")
    else:
        contador_de_votos += 1
        print("Voto nulo, no contabilizado.")

print(f"\n\n\nVotos a favor: {votos_a_favor}, votos en contra: {votos_en_contra}")

if votos_a_favor > votos_en_contra:
    print("\nGanó la opción A FAVOR.")
elif votos_en_contra > votos_a_favor:
    print("\nGanó la opción EN CONTRA")
else:
    print("\nEMPATE")
