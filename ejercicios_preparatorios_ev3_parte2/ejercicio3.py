while True:
    try:
        registro_atletas = int(input("¿Cuantos atletas?: "))
        if registro_atletas <= 0:
            print("Dato invalido: Solo se permiten registrar numeros enteros positivos mayor a 0.")
        else:
            break
    except ValueError:
        print("Dato invalido: Ingresa un entero positivo para continuar.")

atleta_elite = 0
atleta_regular = 0

for i in range(registro_atletas):
    print(f"Atleta numero {i+1}")
    while True:
        try:
            codigo = input("Ingrese el codigo del atleta: ")
            if len(codigo) >= 5 and " " not in codigo and codigo.isalnum():
                break
            else:
                print("Código inválido. Debe tener al menos 5 caracteres, sin espacios y solo letras o números.")
        except ValueError:
            print("¡Error! Ingresa un número entero positivo para el puntaje.")

    while True:
        try:
            puntaje_rendimiento = int(input("Ingrese el puntaje de rendimiento del atleta: "))
            if puntaje_rendimiento <= 0:
                print("Dato invalido: Solo se permiten registrar numeros enteros positivos mayor a 0.")
            else:
                break
        except ValueError:
            print("Dato invalido: Ingresa un entero positivo para continuar.")

    if puntaje_rendimiento > 70:
        print("Atleta Élite")
        atleta_elite += 1
    else:
        print("Atleta Regular")
        atleta_regular += 1

print(f"La cantidad de atletas elite son: {atleta_elite}")    
print(f"La cantidad de atletas regular son: {atleta_regular}")   