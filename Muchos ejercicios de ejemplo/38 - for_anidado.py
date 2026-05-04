# ============================================
# 38 - CICLO FOR (ANIDADO)
# Tema: For dentro de for
# Nivel: ⭐⭐⭐⭐ Avanzado
# ============================================
# Los for anidados son ideales para trabajar con
# matrices, tablas, y patrones bidimensionales.

# --- Tabla de multiplicar completa ---
print("=== TABLA DE MULTIPLICAR (1-10) ===")
print("    ", end="")
for j in range(1, 11):
    print(f"{j:4}", end="")
print()
print("    " + "----" * 10)

for i in range(1, 11):
    print(f"{i:2} |", end="")
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

print()

# --- Patrón diamante ---
print("=== DIAMANTE ===")
n = int(input("Tamaño del diamante (número impar): "))
if n % 2 == 0:
    n += 1

mitad = n // 2

# Parte superior (incluyendo el centro)
for i in range(mitad + 1):
    espacios = mitad - i
    estrellas = 2 * i + 1
    print(" " * espacios + "✦" * estrellas)

# Parte inferior
for i in range(mitad - 1, -1, -1):
    espacios = mitad - i
    estrellas = 2 * i + 1
    print(" " * espacios + "✦" * estrellas)

print()

# --- Encontrar divisores de cada número ---
print("=== DIVISORES ===")
limite = int(input("Mostrar divisores del 1 al: "))

for num in range(1, limite + 1):
    divisores = []
    for d in range(1, num + 1):
        if num % d == 0:
            divisores.append(d)  # Adelanto de listas
    print(f"  {num:3}: {divisores}")

print()

# --- Coordenadas de un tablero ---
print("=== TABLERO DE COORDENADAS ===")
filas = 5
columnas = 5

print("    ", end="")
for c in range(columnas):
    print(f"  {c} ", end="")
print()

for f in range(filas):
    print(f" {f} |", end="")
    for c in range(columnas):
        if (f + c) % 2 == 0:
            print(" ⬜", end="")
        else:
            print(" ⬛", end="")
    print(" |")
