# ============================================
# 05 - VARIABLES Y TIPOS DE DATOS (PROFUNDO)
# Tema: Identidad, memoria y constantes
# Nivel: ⭐⭐⭐ Profundo
# ============================================
# Cada variable en Python apunta a un objeto en memoria.
# Podemos explorar cómo Python maneja esto internamente.

import sys

# --- id(): dirección de memoria del objeto ---
a = 42
b = 42
c = 43

print("a =", a, "| id(a) =", id(a))
print("b =", b, "| id(b) =", id(b))
print("c =", c, "| id(c) =", id(c))
print("¿a y b apuntan al mismo objeto?", a is b)  # True (Python optimiza enteros pequeños)
print("¿a y c apuntan al mismo objeto?", a is c)  # False

print()

# --- sys.getsizeof(): tamaño en bytes de un objeto ---
entero = 0
decimal = 0.0
texto = ""
texto_largo = "Hola Mundo desde Python en DuocUC Puerto Montt"
booleano = True

print(f"Tamaño de int (0):      {sys.getsizeof(entero)} bytes")
print(f"Tamaño de float (0.0):  {sys.getsizeof(decimal)} bytes")
print(f"Tamaño de str vacío:    {sys.getsizeof(texto)} bytes")
print(f"Tamaño de str largo:    {sys.getsizeof(texto_largo)} bytes")
print(f"Tamaño de bool (True):  {sys.getsizeof(booleano)} bytes")

print()

# --- Convenciones de "constantes" (Python no tiene constantes reales) ---
PI = 3.14159265
GRAVEDAD = 9.81
VELOCIDAD_LUZ = 299_792_458  # Los guiones bajos mejoran legibilidad en números grandes

print(f"PI = {PI}")
print(f"Gravedad = {GRAVEDAD} m/s²")
print(f"Velocidad de la luz = {VELOCIDAD_LUZ} m/s")

print()

# --- Separador de miles con guion bajo ---
poblacion_chile = 19_500_000
presupuesto = 1_000_000_000
print(f"Población de Chile: {poblacion_chile:,}")         # formato con comas
print(f"Presupuesto: ${presupuesto:,.0f}")

print()

# --- None: la ausencia de valor ---
resultado = None
print("resultado =", resultado)
print("Tipo de None:", type(resultado))
print("¿resultado es None?", resultado is None)
