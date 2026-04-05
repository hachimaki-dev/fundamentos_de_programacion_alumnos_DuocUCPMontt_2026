print("/////////////ADIVINA EL NUMERO SECRETO/////////////")

numero_secreto = 7
numero_usuario = ""
intentos = 0

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Registra tu numero: "))
    intentos += 1
    if numero_usuario < numero_secreto:
        print("El numero es mas ALTO!")

    if numero_usuario > numero_secreto:
        print("El numero es mas BAJO!")


print(f"¡Ganaste en {intentos} intentos!")