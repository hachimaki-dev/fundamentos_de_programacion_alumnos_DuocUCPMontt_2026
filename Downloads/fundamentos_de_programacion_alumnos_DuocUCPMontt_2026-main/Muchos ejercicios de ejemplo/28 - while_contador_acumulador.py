# ============================================
# 28 - CICLO WHILE (CONTADOR Y ACUMULADOR)
# Tema: Patrones comunes con while
# Nivel: ⭐⭐ Básico-Medio
# ============================================
# Dos patrones fundamentales de programación:
# - CONTADOR: cuenta cuántas veces pasa algo
# - ACUMULADOR: va sumando valores

# --- Acumulador: sumar números ---
print("=== ACUMULADOR: SUMA ===")
print("Ingresa números para sumar. Escribe 0 para terminar.")

suma = 0
contador = 0

# Leemos el primer número
numero = int(input("Número: "))

while numero != 0:
    suma += numero       # acumula la suma
    contador += 1        # cuenta cuántos números
    numero = int(input("Número: "))

print(f"\nSumaste {contador} números.")
print(f"La suma total es: {suma}")
if contador > 0:
    print(f"El promedio es: {suma / contador:.2f}")

print()

# --- Contador: contar pares e impares ---
print("=== CONTADOR: PARES E IMPARES ===")
cantidad = int(input("¿Cuántos números vas a ingresar? "))

pares = 0
impares = 0
contador_bucle = 0

while contador_bucle < cantidad:
    num = int(input(f"  Número {contador_bucle + 1}: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador_bucle += 1

print(f"\nPares: {pares}")
print(f"Impares: {impares}")

print()

# --- Encontrar el mayor y menor ---
print("=== MAYOR Y MENOR ===")
n = int(input("¿Cuántos números ingresarás? "))

if n > 0:
    primer_numero = int(input("  Número 1: "))
    mayor = primer_numero
    menor = primer_numero
    puntero = 1

    while puntero < n:
        num = int(input(f"  Número {puntero + 1}: "))
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
        puntero += 1

    print(f"\nMayor: {mayor}")
    print(f"Menor: {menor}")
else:
    print("No se ingresaron números para comparar.")

