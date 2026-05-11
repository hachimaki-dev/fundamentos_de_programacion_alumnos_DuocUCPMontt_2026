Desarrolle un programa que solicite dos números enteros para definir un rango. Luego genere un número aleatorio dentro del rango y lo ajuste para que sea par.

Reglas:

    Si el número generado es impar y numero + 1 sigue dentro del rango, usar numero + 1.
    Si numero + 1 se sale del rango, usar numero - 1.
    Si ya es par, no modificar.

El jugador tendrá 3 intentos para adivinar el número.

    Intento 1: indicar si el número es mayor o menor.
    Intento 2: además entregar pista de cercanía.
    Intento 3: si falla, mostrar el número y terminar.

Debe usar randint().