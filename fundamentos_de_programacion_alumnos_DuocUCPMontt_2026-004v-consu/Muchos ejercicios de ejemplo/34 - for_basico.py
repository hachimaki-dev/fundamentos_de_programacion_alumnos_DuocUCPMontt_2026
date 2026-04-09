# ============================================
# 34 - CICLO FOR (BÁSICO)
# Tema: Tu primer for con range()
# Nivel: ⭐ Básico
# ============================================
# El ciclo for recorre una secuencia elemento por elemento.
# range(n) genera números del 0 al n-1.
# Es más conciso que while para contar.

# --- For con range ---
print("=== CONTAR DEL 0 AL 4 ===")
for i in range(5):       # 0, 1, 2, 3, 4
    print(f"i = {i}")

print()

# --- For con inicio y fin ---
print("=== CONTAR DEL 1 AL 10 ===")
for i in range(1, 11):   # 1, 2, 3, ..., 10
    print(i, end=" ")
print()

print()

# --- For con paso ---
print("=== DE 2 EN 2 ===")
for i in range(0, 20, 2):  # 0, 2, 4, ..., 18
    print(i, end=" ")
print()

print()

# --- Cuenta regresiva ---
print("=== CUENTA REGRESIVA ===")
for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i, end="... ")
print("🚀 ¡Despegue!")

print()

# --- Repetir una acción ---
print("=== REPETIR ACCIÓN ===")
nombre = input("¿Cómo te llamas? ")
veces = int(input("¿Cuántas veces te saludo? "))

for i in range(veces):
    print(f"  ¡Hola, {nombre}! (saludo #{i + 1})")
