# ============================================
# 33 - CICLO WHILE (PROFUNDO)
# Tema: Patrones algorítmicos y simulaciones
# Nivel: ⭐⭐⭐⭐⭐⭐ Profundo
# ============================================
# Exploramos algoritmos clásicos usando while.
# Estos patrones son la base de la programación algorítmica.

import time
import random

# --- Algoritmo de Euclides (MCD) ---
print("=== MÁXIMO COMÚN DIVISOR (Algoritmo de Euclides) ===")
a = int(input("Número 1: "))
b = int(input("Número 2: "))

# Guardar originales para mostrar después
original_a, original_b = a, b

paso = 1
while b != 0:
    print(f"  Paso {paso}: {a} = {b} × {a // b} + {a % b}")
    a, b = b, a % b
    paso += 1

mcd = a
print(f"MCD({original_a}, {original_b}) = {mcd}")

print()

# --- Número primo ---
print("=== ¿ES PRIMO? ===")
numero = int(input("Ingresa un número: "))

if numero < 2:
    es_primo = False
else:
    es_primo = True
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1

print(f"{numero} {'SÍ' if es_primo else 'NO'} es primo")

print()

# --- Sucesión de Fibonacci ---
print("=== FIBONACCI ===")
n = int(input("¿Cuántos términos de Fibonacci? "))

a, b = 0, 1
i = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
print()

print()

# --- Conversión de decimal a binario ---
print("=== DECIMAL A BINARIO ===")
decimal = int(input("Ingresa un número decimal: "))
original = decimal
binario = ""

if decimal == 0:
    binario = "0"
else:
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal //= 2

print(f"{original} en binario es: {binario}")
print(f"Verificación con bin(): {bin(original)}")

print()

# --- Simulación: lanzar dados hasta sacar doble ---
print("=== SIMULACIÓN: LANZAR DADOS ===")
print("Lanzando dos dados hasta obtener un doble (par)...")

lanzamientos = 0

while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    lanzamientos += 1
    
    emoji1 = "⚀⚁⚂⚃⚄⚅"[dado1 - 1]
    emoji2 = "⚀⚁⚂⚃⚄⚅"[dado2 - 1]
    
    if dado1 == dado2:
        print(f"  Lanzamiento {lanzamientos}: {emoji1} {emoji2} ({dado1}, {dado2}) ← ¡DOBLE! 🎉")
        break
    else:
        print(f"  Lanzamiento {lanzamientos}: {emoji1} {emoji2} ({dado1}, {dado2})")

print(f"Se necesitaron {lanzamientos} lanzamientos para obtener un doble.")
