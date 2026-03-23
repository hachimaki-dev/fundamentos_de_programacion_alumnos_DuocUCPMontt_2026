print("======= CALCULADORA ========")

def sumar(x, y): 
    return x + y

def restar(x, y): 
    return x - y

def multiplicar(x, y): 
    return x * y

def dividir(x, y): 
    if y != 0:
        return x / y
    else:
        return "No dividas por 0 bro"


while True:
    print("=== MENU ===")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. SALIR")

    eleccion = input("QUE OPERACION DESEA REALIZAR? (1/2/3/4/5): ")

    
    if eleccion == "5":
        print("HASTA LUEGO >:3")
        break  

    
    elif eleccion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Introduce el primer numero: "))
            num2 = float(input("Introduce el segundo numero: "))
        except ValueError:
            print("Introduce solo números válidos")
            continue  

        if eleccion == "1":
            print(f"Resultado: {sumar(num1, num2)}")
        elif eleccion == "2":
            print(f"Resultado: {restar(num1, num2)}")
        elif eleccion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif eleccion == "4":
            print(f"Resultado: {dividir(num1, num2)}")

    
    else:
        print("Operacion no valida, introduce un numero del 1 al 5")

    # Preguntar si desea continuar
    continuar = input("¿Quieres realizar otra operacion? (si/no): ").strip().lower()
    if continuar != "si":
        print("HASTA LUEGO >:3")
        break  