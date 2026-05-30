# ============================================
# 10 - OPERADORES ARITMÉTICOS (MEDIO)
# Tema: Precedencia de operadores y asignación compuesta
# Nivel: ⭐⭐ Medio
# ============================================
# Las operaciones siguen un orden de precedencia (igual que en matemáticas).
# También existen operadores de asignación compuesta (atajos).

# --- Precedencia de operadores ---
# Orden: () > ** > * / // % > + -
print("=== PRECEDENCIA ===")

resultado1 = 2 + 3 * 4        # 3*4=12, luego 2+12=14
resultado2 = (2 + 3) * 4      # 2+3=5, luego 5*4=20
resultado3 = 10 - 2 ** 3      # 2**3=8, luego 10-8=2
resultado4 = 10 / 2 + 3       # 10/2=5.0, luego 5.0+3=8.0

print(f"2 + 3 * 4     = {resultado1}")
print(f"(2 + 3) * 4   = {resultado2}")
print(f"10 - 2 ** 3   = {resultado3}")
print(f"10 / 2 + 3    = {resultado4}")

print()

# --- Operadores de asignación compuesta ---
print("=== ASIGNACIÓN COMPUESTA ===")

puntos = 100
print(f"Inicio: puntos = {puntos}")

puntos += 50    # equivale a: puntos = puntos + 50
print(f"puntos += 50  → {puntos}")    # 150

puntos -= 30    # equivale a: puntos = puntos - 30
print(f"puntos -= 30  → {puntos}")    # 120

puntos *= 2     # equivale a: puntos = puntos * 2
print(f"puntos *= 2   → {puntos}")    # 240

puntos //= 3    # equivale a: puntos = puntos // 3
print(f"puntos //= 3  → {puntos}")    # 80

puntos %= 7     # equivale a: puntos = puntos % 7
print(f"puntos %= 7   → {puntos}")    # 3

puntos **= 4    # equivale a: puntos = puntos ** 4
print(f"puntos **= 4  → {puntos}")    # 81

print()

# --- Ejemplo práctico: calcular vuelto ---
print("=== CALCULADORA DE VUELTO ===")
precio = 7500
pago = 10000
vuelto = pago - precio

print(f"Precio: ${precio}")
print(f"Pagó:   ${pago}")
print(f"Vuelto: ${vuelto}")

# ¿Cuántas monedas de $500 y $100 necesitas?
monedas_500 = vuelto // 500
resto = vuelto % 500
monedas_100 = resto // 100

print(f"Monedas de $500: {monedas_500}")
print(f"Monedas de $100: {monedas_100}")
