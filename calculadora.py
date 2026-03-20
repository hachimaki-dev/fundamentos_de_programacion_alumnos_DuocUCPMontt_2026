while True:
    print("=======CALCULADORA=======")

    try:
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))
        
        print("Seleccione su operacion: 1. Sumar | 2. Restar | 3. Dividir | 4. Multiplicar")
        operacion = input("Elige una operacion (1-4): ")
        
        if operacion == "1":
            resultado = int(numero1) + int(numero2)
            print(f"El resultado de la suma es: {resultado}")
        
        if operacion == "2":
            resultado = int(numero1) - int(numero2)
            print(f"El resultado de la resta es: {resultado}")
            
        if operacion == "3":
                if int(numero2) == 0:
                    print("Error: ¡No se puede dividr entre cero!")
                    
                else:
                    resultado = int(numero1) / int(numero2)
                    print(f"El resultado de la division es: {resultado}")
                    
        if operacion == "4":
            resultado = int(numero1) * int(numero2)
            print(f"El resultado de la multiplicacion es: {resultado}")
            
            
    except ValueError:
        print("Error: ¡Debes ingresar solo numeros enteros!")
        
    except Exepction as e:
        print(f"Ups, ocurrio algo inesperado: {e}")

    continuar = input("\n¿Quieres hacer otro calculo? (s/n): ")

    if continuar.lower() == "n":
        print("Nos vemos, Usuario!")
        break