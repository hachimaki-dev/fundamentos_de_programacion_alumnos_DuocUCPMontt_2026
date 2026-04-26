numero_secreto = 43
respuesta_usuario = 0
intentos = 0
while respuesta_usuario != numero_secreto:
    respuesta_usuario = int(input("Adivina el numero secreto: "))
    intentos = intentos + 1
    if respuesta_usuario < numero_secreto:
        print("El numero es mas bajo que el numero secreto")
    elif respuesta_usuario > numero_secreto:
        print("El numero ingresado es mayor que el numero oculto")
print(f"Has adivinado ganaste en {intentos} intentos")