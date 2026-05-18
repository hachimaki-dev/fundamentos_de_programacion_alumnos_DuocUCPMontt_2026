from funciones_calculadora import *

print("Bienvenido a la calculadora básica")

while True:
    try:
        eleccion_usuario = int(input("Que deseas hacer?\n1. Sumar\n2. Restar\n3. Dividir\n4. Multiplicar\n5. Potenciar\nIngrese su elección: "))
        if eleccion_usuario == 1:
            print("Ingresa los números a sumar:")
            num1 = int(input("Ingresa el número 1: "))
            num2 = int(input("Ingresa el número 2: "))
            print(f"El resultado de sumar {num1, num2} es: ")
            print(sumar(num1, num2))
            
        elif eleccion_usuario == 2:
            print("Ingresa los números a restar:")
            num1 = int(input("Ingresa el número 1: "))
            num2 = int(input("Ingresa el número 2: "))
            print(f"El resultado de restar {num1, num2} es: ")
            print(restar(num1, num2))
        elif eleccion_usuario == 3:
            print("Ingresa los números a dividir:")
            num1 = int(input("Ingresa el número 1: "))
            num2 = int(input("Ingresa el número 2: "))
            print(f"El resultado de dividir {num1, num2} es: ")
            print(dividir(num1, num2))

        elif eleccion_usuario == 4:
            print("Ingresa los números a multiplicar:")
            num1 = int(input("Ingresa el número 1: "))
            num2 = int(input("Ingresa el número 2: "))
            print(f"El resultado de multiplicar {num1, num2} es: ")
            print(multiplicar(num1, num2))
        
        elif eleccion_usuario == 5:
            print("Ingresa los números a potenciar:")
            num1 = int(input("Ingresa el número 1: "))
            num2 = int(input("Ingresa el número 2: "))
            print(f"El resultado de potenciar {num1, num2} es: ")
            print(potencia(num1, num2))
        else:
            print("Ingresa una opción valida.")
            continue
        
        seguir = input("Deseas seguir operando? Si/No\nIngrese su elección: ").strip().lower()
        if seguir == "si":
            continue
        else:
            break
            
        
    except ValueError:
        print("Ingresa un valor valido.")
        continue
    
print("Gracias por usar el servicio")