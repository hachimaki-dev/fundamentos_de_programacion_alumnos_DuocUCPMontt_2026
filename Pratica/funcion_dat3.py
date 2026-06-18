# --- DEFINICIÓN DE FUNCIONES ---

def saludar_usuario():
    nombre = input("¿Cómo te llamas?: ")
    print(f"\n¡Hola, {nombre}! Qué bueno tenerte por aquí.\n")

def sumar():
    n1 = float(input("Ingresa el primer número: "))
    n2 = float(input("Ingresa el segundo número: "))
    print(f"\nEl resultado de la suma es: {n1 + n2}\n")

def dibujar_cuadrado():
    tamano = int(input("¿De qué tamaño quieres el cuadrado? (ej. 4): "))
    print()
    # Uso de bucles FOR para filas y columnas
    for i in range(tamano):
        for j in range(tamano):
            print("* ", end="") # end="" evita que salte de línea inmediatamente
        print() # Salto de línea al terminar cada fila
    print()

def cuenta_regresiva():
    inicio = int(input("¿Desde qué número empieza la cuenta regresiva?: "))
    print("\n¡Iniciando cuenta!")
    for i in range(inicio, -1, -1): '''Inicio es de donde comienza la cuenta, el primer -1 es para que vaya en descuento y 
    el ultimo -1 es hasta donde tiene que llegar, el caso dice que debe llegar a 0, como el 0 es contable se coloca hasta el -1'''
    print(i)
    print("¡Tiempo!\n")


# --- PROGRAMA PRINCIPAL (MENÚ) ---

def menu_principal():
    continuar = True
    
    while continuar:
        print("=== PANEL DE CONTROL ===")
        print("1. Saludar al usuario")
        print("2. Sumar dos números")
        print("3. Dibujar un cuadrado")
        print("4. Cuenta regresiva")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == "1":
            saludar_usuario()
        elif opcion == "2":
            sumar()
        elif opcion == "3":
            dibujar_cuadrado()
        elif opcion == "4":
            cuenta_regresiva()
        elif opcion == "5":
            print("\n¡Gracias por usar el programa! Hasta luego.")
            continuar = False # Rompe el bucle while para salir
        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

# Ejecutamos el menú para iniciar el programa
menu_principal()