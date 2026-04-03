# Minijuego: El Número Secreto
# Objetivo: Programar un juego clásico de interacción constante.

# 1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
# 2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
# 3. Dentro del while: pide un número al usuario.
# - Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
# - Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
# 4. Usa un contador para registrar en cuántos turnos logró adivinar.
# 5. Imprime al final "¡Ganaste en X intentos!".

numero_secreto = 5
respuesta_del_usuario = 0
contador = 0

print("*****!!!Bienvenido adivina el número secreto!!!*****")
while respuesta_del_usuario != numero_secreto:
    respuesta_del_usuario = int(input("Adivina el número secreto del 1 al 10: "))
    if respuesta_del_usuario > numero_secreto:
        print("Tu número esta más BAJO")
        contador += 1
    elif respuesta_del_usuario < numero_secreto:
        print("El número secreo es más ALTO")
        contador += 1
    else: 
        respuesta_del_usuario == numero_secreto
        print(f"¡Ganasta en {contador} intentos felicidades!! :D")
    
print("Fin del programa")