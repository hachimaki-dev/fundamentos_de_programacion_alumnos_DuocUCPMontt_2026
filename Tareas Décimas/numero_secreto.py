'''
1. Guarda en una variable un número secreto (fijo, por ejemplo el 42).
2. Usa un while que se repita MIENTRAS la "respuesta del usuario" sea diferente (!=) al "número secreto".
3. Dentro del while: pide un número al usuario.
- Si el ingresado es menor al secreto, dile "El número secreto es más ALTO".
- Si el ingresado es mayor al secreto, dile "El número secreto es más BAJO".
4. Usa un contador para registrar en cuántos turnos logró adivinar.
5. Imprime al final "¡Ganaste en X intentos!".
'''

numero_secreto = 50
contador_intentos = 0
respuesta_del_usuario = -1

while respuesta_del_usuario != numero_secreto :
    respuesta_del_usuario = int (input("Adivine el número secreto: "))

    if respuesta_del_usuario > numero_secreto :
        print("El número secreto es más BAJO.")
    if respuesta_del_usuario < numero_secreto :
        print("El número secreto es más ALTO")

    contador_intentos += 1

print(f"¡Ganaste en {contador_intentos} intentos!")