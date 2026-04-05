# ============================================
# 04 - VARIABLES Y TIPOS DE DATOS (MEDIO)
# Tema: Conversión de tipos y asignación múltiple
# Nivel: ⭐⭐ Medio
# ============================================
# A veces necesitas convertir un tipo de dato a otro.
# También puedes asignar varias variables en una sola línea.

# --- Conversión de tipos (casting) ---
numero_texto = "42"
numero_entero = int(numero_texto)     # str -> int
numero_decimal = float(numero_texto)  # str -> float

print("Texto original:", numero_texto, "| Tipo:", type(numero_texto))
print("Convertido a int:", numero_entero, "| Tipo:", type(numero_entero))
print("Convertido a float:", numero_decimal, "| Tipo:", type(numero_decimal))

print()

# --- Convertir número a texto ---
precio = 9990
precio_texto = str(precio)
print("El precio es: $" + precio_texto)   # Concatenar requiere que ambos sean str
# print("El precio es: $" + precio)       # ¡Esto daría ERROR!

print()

# --- Asignación múltiple ---
x, y, z = 10, 20, 30
print("x =", x, "| y =", y, "| z =", z)

# --- Mismo valor a múltiples variables ---
a = b = c = 0
print("a =", a, "| b =", b, "| c =", c)

print()

# --- Intercambiar valores (swap) ---
primero = "manzana"
segundo = "naranja"
print("Antes:  primero =", primero, "| segundo =", segundo)

primero, segundo = segundo, primero  # ¡Python lo hace fácil!
print("Después: primero =", primero, "| segundo =", segundo)

print()

# --- Reasignar variables (cambiar su valor y tipo) ---
dato = 100
print("dato =", dato, "| Tipo:", type(dato))
dato = "ahora soy texto"
print("dato =", dato, "| Tipo:", type(dato))
dato = 3.14
print("dato =", dato, "| Tipo:", type(dato))
