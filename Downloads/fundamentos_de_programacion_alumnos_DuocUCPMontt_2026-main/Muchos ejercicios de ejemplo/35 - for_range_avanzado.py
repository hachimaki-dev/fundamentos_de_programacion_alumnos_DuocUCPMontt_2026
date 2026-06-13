# ============================================
# 35 - CICLO FOR (RANGE AVANZADO)
# Tema: Dominar range() y acumuladores con for
# Nivel: ⭐⭐ Básico-Medio
# ============================================
# range() es más versátil de lo que parece.
# Combinado con acumuladores, resuelve muchos problemas.

# --- Tabla de multiplicar ---
print("=== TABLA DE MULTIPLICAR ===")
tabla = int(input("¿Qué tabla quieres? "))

for i in range(1, 13):
    print(f"  {tabla} x {i:2} = {tabla * i:3}")

print()

# --- Sumar números del 1 al N ---
print("=== SUMA DEL 1 AL N ===")
n = int(input("Ingresa N: "))
suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma del 1 al {n} es: {suma}")
print(f"Verificación con fórmula: {n * (n + 1) // 2}")

print()

# --- Factorial ---
print("=== FACTORIAL ===")
n = int(input("Ingresa un número para calcular su factorial: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

print()

# --- Números pares en un rango ---
print("=== NÚMEROS PARES ===")
inicio = int(input("Desde: "))
fin = int(input("Hasta: "))

print(f"Pares entre {inicio} y {fin}:")
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(f"  {i}", end="")
print()

print()

# --- Potencias de 2 ---
print("=== POTENCIAS DE 2 ===")
for i in range(11):
    print(f"  2^{i:2} = {2**i:5}")
