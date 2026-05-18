def sumar(x, y):
    return(x + y)
def restar(x, y):
    return(x - y)
def multiplicar(x, y):
    return(x * y)
def dividir(x, y):
    return(x / y)

def pedirNumeros():
    global numero1, numero2
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

while True:
    print("Operaciones: 1. Sumar    2. Restar    3. Multiplicar    4. Dividir    5. Salir")
    operacion_elegida = input("Elije una operación: ")

    if operacion_elegida == "1":
        print("\n")
        pedirNumeros()
        print(f"\n{numero1} + {numero2} = {sumar(numero1, numero2)}\n")
    elif operacion_elegida == "2":
        print("\n")
        pedirNumeros()
        print(f"\n{numero1} - {numero2} = {restar(numero1, numero2)}\n")
    elif operacion_elegida == "3":
        print("\n")
        pedirNumeros()
        print(f"\n{numero1} * {numero2} = {multiplicar(numero1, numero2)}\n")
    elif operacion_elegida == "4":
        print("\n")
        pedirNumeros()
        if numero2 == 0:
            print("\nOperación inválida. No se puede dividir por 0.\n")
        else:
            print(f"\n{numero1} / {numero2} = {dividir(numero1, numero2)}\n")
    elif operacion_elegida == "5":
        break
    else:
        print("\nOperación inválida. \n")
