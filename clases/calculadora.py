# Tarea: Implementar calculadora con menú
# Menú de opciones: 1 sumar, 2 restar, 3 multiplicar, 4 divides, 5 cerrar calculadora, cualquier otro numero será invalido

def sumar(numero_1 , numero_2):
    return numero_1 + numero_2

def resta(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1 , numero_2):
    return numero_1 * numero_2

def division(numero_1 , numero_2):
    return numero_1 // numero_2

while True:

    print("\n===================")
    print("=== CALCULADORA ===")
    print("===================")

    print("\nOpcion 1. Sumar")
    print("Opcion 2. Restar")
    print("Opcion 3. Multiplicar")
    print("Opcion 4. Dividir")
    print("Opcion 5. Cerrar calculadora")
    opcion = int(input("\nSeleccione una opción: "))
    if opcion == 5:
        print("Calculadora cerrada, como dice mi tío: Si ya cerraron entonces tomate un pisco helado")
        break
    if opcion >= 1 and opcion <= 4:
        numero_1 = int(input("Ingrese el primer número: "))
        numero_2 = int(input("Ingrese el segundo número: "))
        if opcion == 1:
            print("Resultado:", sumar(numero_1, numero_2))
        elif opcion == 2:
            print("Resultado:", resta(numero_1, numero_2))
        elif opcion == 3:
            print("Resultado:", multiplicar(numero_1, numero_2))
        elif opcion == 4:
            print("Resultado:", division(numero_1, numero_2))
    else:
        print("Opción inválida... Por favor ingrese un numero valido, no es tan dificil")