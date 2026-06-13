# ============================================
# 31 - CICLO WHILE (ANIDADO)
# Tema: While dentro de while
# Nivel: ⭐⭐⭐⭐ Avanzado
# ============================================
# Un while anidado es un bucle dentro de otro.
# El bucle interior se ejecuta COMPLETO por cada iteración del exterior.

# --- Tabla de multiplicar ---
print("=== TABLAS DE MULTIPLICAR ===")
num_tabla = int(input("¿Qué tabla quieres ver (1-12)? "))

idx = 1
while idx <= 12:
    print(f"  {num_tabla} x {idx} = {num_tabla * idx}")
    idx += 1

print()

# --- Múltiples tablas ---
print("=== TABLAS DEL 1 AL 5 ===")
tab_ext = 1
while tab_ext <= 5:
    print(f"\n--- Tabla del {tab_ext} ---")
    val_int = 1
    while val_int <= 10:
        print(f"  {tab_ext} x {val_int:2} = {tab_ext * val_int:3}")
        val_int += 1
    tab_ext += 1

print()

# --- Patrón de estrellas (triángulo) ---
print("=== TRIÁNGULO DE ESTRELLAS ===")
limite_filas = int(input("¿Cuántas filas? "))

f_tri = 1
while f_tri <= limite_filas:
    c_tri = 1
    while c_tri <= f_tri:
        print("*", end=" ")
        c_tri += 1
    print()  # nueva línea
    f_tri += 1

print()

# --- Patrón inverso ---
print("=== TRIÁNGULO INVERTIDO ===")
f_inv = limite_filas
while f_inv >= 1:
    c_inv = 1
    while c_inv <= f_inv:
        print("#", end=" ")
        c_inv += 1
    print()
    f_inv -= 1

print()

# --- Patrón cuadrado hueco ---
print("=== CUADRADO HUECO ===")
lado_sq = int(input("Tamaño del cuadrado: "))

f_sq = 1
while f_sq <= lado_sq:
    c_sq = 1
    while c_sq <= lado_sq:
        # Imprime solo si es un borde
        if f_sq == 1 or f_sq == lado_sq or c_sq == 1 or c_sq == lado_sq:
            print("X", end=" ")
        else:
            print(" ", end=" ")
        c_sq += 1
    print()
    f_sq += 1

