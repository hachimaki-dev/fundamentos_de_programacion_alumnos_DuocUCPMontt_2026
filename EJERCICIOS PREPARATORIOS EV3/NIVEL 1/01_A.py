#Ejercicio 1A — Solo capturar ValueError (calentamiento)
#Escribe un programa que pida al usuario un número entero. Si el usuario ingresa algo que no sea un número (por ejemplo "abc" o "3.7"), el programa debe capturar la excepción ValueError y mostrar:

#"Error: eso no es un número entero."

#Repite la solicitud hasta que el usuario ingrese un entero válido (puede ser cualquier entero, positivo, negativo o cero). Cuando lo logre, muestra:

#"Número recibido: {valor}"
#Objetivo: Entender try/except ValueError de forma aislada, sin combinar aún con validaciones de rango.

#Casos de prueba: "abc", "3.7", "", 0, -5, 42

while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        print(f"Número recibido: {numero}")
        break
    except ValueError:
        print("Error: eso no es un número entero.")