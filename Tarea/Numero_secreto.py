print("Adivina el numero secreto")
numero_secreto = 42
numero_usuario = 0 
intentos_usuario = 0 
while numero_usuario != numero_secreto:
    numero_usuario = int(input("Ingrese un numero porfavor: "))
    intentos_usuario = intentos_usuario + 1

    if numero_usuario < numero_secreto :
        print("El numero secreto es MAS ALTO")
    elif numero_usuario > numero_secreto :
        print("El numero secreto es MAS BAJO")
print(f"ADIVINASTE EL NUMERO SECRETO!!!Lo hiciste en {intentos_usuario} FELICIDADES!!")

 




















#1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
#2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
#3. Dentro del while: pide un número al usuario.
#- Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
#- Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
#4. Usa un contador para registrar en cuántos turnos logró adivinar.
#5. Imprime al final "¡Ganaste en X intentos!""