# Tarea: Implementar esta calculador con:
# Menu de opciones: 1 suma, 2 resta, 3 multiplica, 4 divide, 5 sale, cualquier otro numero es invalido
# Pedir numeros por input

def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def resta(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(numero_1, numero_2):
    return numero_1 // numero_2

def solicitar_dos_numeros():
    numero_1 = int(input("\nIngrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    return numero_1, numero_2

print("---- CALCULADORA ----")

while True:
    print("\nOpciones: \n1. Sumar\n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir")
    opcion_usuario = int(input("¿Que operacion quiere realizar? (1/2/3/4/5): "))
    if opcion_usuario == 1:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(f"\n{numero_1} + {numero_2} = {sumar(numero_1, numero_2)}")
    elif opcion_usuario == 2:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(f"\n{numero_1} - {numero_2} = {resta(numero_1, numero_2)}")
    elif opcion_usuario == 3:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(f"\n{numero_1} * {numero_2} = {multiplicacion(numero_1, numero_2)}")
    elif opcion_usuario == 4:
        numero_1, numero_2 = solicitar_dos_numeros()
        print(f"\n{numero_1} // {numero_2} = {division(numero_1, numero_2)}")
    elif opcion_usuario == 5:
        break
    else:
        print("Opcion Invalida. Vuelva a intentar.")
    