print("Bienvenido a esta calculadora de números primos.")

# Bucle para asegurar el rango máximo
while True:
    maximo_de_range = int(input("Ingrese el número máximo: "))
    respuesta = input(f"¿Estás seguro que {maximo_de_range} sea tu máximo? (SI/NO): ").upper()
    
    if respuesta == "SI":
        print("Perfecto, entonces continuamos...\n")
        break
    print("Perfecto, volveremos a empezar.")

# Lógica para encontrar primos
for num in range(2, maximo_de_range + 1):
    es_primo = True
    # Verificamos divisores desde 2 hasta la raíz del número (optimización)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break  # Si encontramos un divisor, ya no es primo
    
    if es_primo:
        print(num)
