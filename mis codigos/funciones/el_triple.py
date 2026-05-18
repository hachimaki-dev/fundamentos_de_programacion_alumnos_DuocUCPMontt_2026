def sumar(a, b):
    return a + b

def restar(a, b):    
    return a - b

def multiplicar(a, b):  
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"


print("==== calculadora basica ====")

print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
print("5. salir")

while True:

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break
    elif opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", sumar(a, b))

    elif opcion == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", restar(a, b))

    elif opcion == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", multiplicar(a, b))

    elif opcion == '4':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", dividir(a, b))

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        continue

