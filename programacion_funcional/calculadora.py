def sumar(numero1:int , numero2:int):
    return numero1 + numero2

def restar(numero1:int , numero2:int):
    return numero1 - numero2

def multiplicar(numero1:int , numero2:int):
    return numero1 * numero2

def dividir(numero1:int , numero2:int):
    if numero2 == 0:
        return "No se puede dividir por 0"
    return numero1 / numero2
    

def SolicitarDosNumeros():
    while True:
        try:
            numero1 = float(input("Ingrese el 1er numero: "))
            numero2 = float(input("INgrese el 2do numero: "))
            return numero1 , numero2
        except ValueError:
            print("Ingrese numero valido!")

print("Bienvenido a la calculadora!")
while True:
    print("\nMENU")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    try:
        eleccion = int(input("Seleccione una opcion 1/2/3/4/5: "))
    except ValueError:
        print("\nIngresa un numero valido!")
        continue

    if eleccion < 1 or eleccion > 5:
        print("Opcion fuera del rango!")
        continue

    if eleccion == 1:
        numero1 , numero2 = SolicitarDosNumeros()
        resultado = sumar(numero1 , numero2)
        print("tu resultado es: ", resultado)
        print("Volviendo al menu\n")
    
    elif eleccion == 2:
        numero1 , numero2 = SolicitarDosNumeros()
        resultado = restar(numero1 , numero2)
        print("Tu resultado es: ", resultado)
        print("Volviendo al menu")
    
    elif eleccion == 3:
        numero1 , numero2 = SolicitarDosNumeros()
        resultado = multiplicar(numero1 , numero2)
        print("Tu resultado es: ", resultado)
        print("Volviendo al menu")

    elif eleccion == 4:
        numero1 , numero2 = SolicitarDosNumeros()
        resultado = dividir(numero1 , numero2)
        print("Tu resultado es: ", resultado)
        print("Volviendo al menu\n")
    
    elif eleccion == 5:
        print("Hasta luego!")
        break
    
    else:
        print("Ingresa algo valido!")
        continue