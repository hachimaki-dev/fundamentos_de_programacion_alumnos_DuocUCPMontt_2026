def restar(a, b):
    return a - b;

def sumar(a, b):
    return a + b;

def dividir(a, b):
    return a / b;

def multiplicar(a, b):
    return a * b;

def potencia(a, b):
    return a ** b;

print("#####################")
print("Calculadora encendida")
print("#####################")

while True:
    try:
        operación = int(input("Operaciones disponibles:\n"
                              "1. Resta\n"
                              "2. Suma\n"
                              "3. Dividir\n"
                              "4. Multiplicar\n"
                              "5. Potencia\n"
                              "Seleccione operación: "))
        # corregi la parte del while con ia porque me quede encerrado y creia que era error mío, pero solo debía cerrar python y volverlo a abrir.
        if operación not in [1,2,3,4,5]:
            print("Opción no válida, intente nuevamente.")
            continue
            
        break   # esot rompe la cadena solo si es 1, 2, 3, 4 o 5.
        
    except ValueError:
        print("Ingrese una opción válida (número).")
        continue

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if operación == 1:
    resultado = restar(num1, num2)
elif operación == 2:
    resultado = sumar(num1, num2)
elif operación == 3:
    resultado = dividir(num1, num2)
elif operación == 4:
    resultado = multiplicar(num1, num2)
elif operación == 5:
    resultado = potencia(num1, num2)
else:
    print("Error")

print(f"El resultado de la operación es: {resultado}")

print("Fin de operación.")
print("Apagando calculadora....")

# esto es una copia de respaldo.