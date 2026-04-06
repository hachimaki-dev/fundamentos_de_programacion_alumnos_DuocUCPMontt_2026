# Objetivo: Programar un juego clásico de interacción constante.
# Guarda en una variable un número secreto (fijo, por ejemplo el 42).
numero_secreto = 12
#  Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
respuesta_usuario = int(input("Adivina el número secreto: "))
while respuesta_usuario != numero_secreto:
# entro del while: pide un número al usuario.
    respuesta_usuario = int(input("Número incorrecto. Intenta de nuevo: "))
    # Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
    if respuesta_usuario < numero_secreto:
        print("El número secreto es más ALTO")
        # Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
    elif respuesta_usuario > numero_secreto:
        print("El número secreto es más BAJO")
        #Usa un contador para registrar en cuántos turnos logró adivinar.
contador_turnos = 1
# Imprime al final "¡Ganaste en X intentos!".
print(f"¡Ganaste en {contador_turnos} intentos!")