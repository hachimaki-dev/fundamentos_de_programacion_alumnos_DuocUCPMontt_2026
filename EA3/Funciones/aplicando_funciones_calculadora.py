#Tarea: Implementar esta calculadora con
#Menu de opciones 1 suma. 2 resta. 3 multiplica, 4 divide, 5 sale, cualquier otro numero es invalido utiliza un while para la repetición los numeros deben ser inputs: 

def sumar(numero_1, numero_2):
            return numero_1 + numero_2

def restar(numero_1, numero_2):
            return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
            return numero_1 * numero_2

#division entera //
def division(numero_1, numero_2):
            return numero_1 // numero_2

def solicitar_dos_numeros():
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    return numero_1, numero_2

while True:
    opcion_elegida = int(input("¿Iniciando calculadora.py que desea hacer?\n"
            "1. Sumar\n"
            "2. Restar\n"
            "3. Multiplicar\n"
            "4. Dividir\n"
            "5. Salir\n"
            "Elige una opción: "))
    
    numero_1, numero_2 = solicitar_dos_numeros()

    #parametro numero_1 y parametro numero_2
    if opcion_elegida == 1:
        print(f"{sumar(numero_1, numero_2)}\n")

    elif opcion_elegida == 2:
        print(f"{restar(numero_1, numero_2)}\n")

    elif opcion_elegida == 3:
        print(f"{multiplicar(numero_1, numero_2)}\n")

    elif opcion_elegida == 4:
        #division entera //
        print(f"{division(numero_1, numero_2)}\n")
    elif opcion_elegida == 5:
        print("Saliste de la calculadora")
        break
    else:
        print("Ingrese un opción valida\n")