# ============================================
# 17 - OPERADORES DE COMPARACIÓN (BÁSICO)
# Tema: Comparar valores
# Nivel: ⭐ Básico
# ============================================
# Los operadores de comparación comparan dos valores
# y devuelven True o False (un booleano).

a = 10
b = 20

print(f"a = {a}, b = {b}")
print("-" * 30)

print(f"a == b  (igual)          → {a == b}")     # False
print(f"a != b  (diferente)      → {a != b}")     # True
print(f"a > b   (mayor que)      → {a > b}")      # False
print(f"a < b   (menor que)      → {a < b}")      # True
print(f"a >= b  (mayor o igual)  → {a >= b}")     # False
print(f"a <= b  (menor o igual)  → {a <= b}")     # True

print()

# --- Comparar con input ---
numero = int(input("Ingresa un número: "))

print(f"\n¿{numero} es mayor que 100?     {numero > 100}")
print(f"¿{numero} es igual a 42?        {numero == 42}")
print(f"¿{numero} es distinto de 0?     {numero != 0}")
print(f"¿{numero} está entre 1 y 10?    {1 <= numero <= 10}")

print()

# --- Comparar textos ---
nombre1 = "carlos"
nombre2 = "Carlos"
print(f"'{nombre1}' == '{nombre2}' → {nombre1 == nombre2}")   # False (mayúsculas importan)
print(f"Comparación ignorando mayúsculas: {nombre1.lower() == nombre2.lower()}")  # True
