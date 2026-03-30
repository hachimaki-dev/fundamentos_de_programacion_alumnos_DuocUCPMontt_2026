print("¡Bienvenido a mi súper calculadora en Python!")

numero1 = int(input("\nIngrese el primer número: "))

while(True):
    print("\n1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    operacion = int(input("\nSelecciona una operación: "))

    if(operacion >= 1 and operacion <= 4):
        break
    else:
        print("\n¡El valor introducido no es válido!, por favor, inténtalo de nuevo")

while(True):
    numero2 = int(input("\nIngrese el segundo número: "))

    if(operacion == 4 and numero2 == 0):
        print("¡No puedes dividir por 0!, por favor, ingresa otro número")
    else:
        break

match operacion:
    case 1:
        resultado = numero1 + numero2
    case 2: 
        resultado = numero1 - numero2
    case 3: 
        resultado = numero1 * numero2
    case 4:
        resultado = numero1 / numero2
    
print(f"Resultado: {resultado}")