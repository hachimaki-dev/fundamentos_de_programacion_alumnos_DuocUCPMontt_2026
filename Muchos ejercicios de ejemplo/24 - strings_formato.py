# ============================================
# 24 - STRINGS (FORMATO)
# Tema: f-strings, .format() y formateo de números
# Nivel: ⭐⭐⭐ Intermedio
# ============================================
# Hay varias formas de insertar variables dentro de texto.
# Los f-strings (Python 3.6+) son la forma más moderna y recomendada.

nombre = "Carlos"
edad = 21
promedio = 5.678
precio = 15990

# --- Método 1: Concatenación (la forma básica) ---
print("=== CONCATENACIÓN ===")
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años.")

# --- Método 2: f-strings (la forma recomendada) ---
print("\n=== F-STRINGS ===")
print(f"Hola, soy {nombre} y tengo {edad} años.")
print(f"Mi promedio es {promedio}")
print(f"Puedo hacer cálculos: {edad * 2}")
print(f"Y llamar métodos: {nombre.upper()}")

# --- Método 3: .format() ---
print("\n=== .FORMAT() ===")
print("Hola, soy {} y tengo {} años.".format(nombre, edad))
print("Desordenado: {1} tiene {0} años.".format(edad, nombre))
print("Con nombres: {n} tiene {e} años.".format(n=nombre, e=edad))

# --- Formateo de números ---
print("\n=== FORMATEO DE NÚMEROS ===")

# Decimales
print(f"Promedio (sin formato):   {promedio}")
print(f"Promedio (1 decimal):     {promedio:.1f}")
print(f"Promedio (2 decimales):   {promedio:.2f}")
print(f"Promedio (0 decimales):   {promedio:.0f}")

print()

# Separador de miles
print(f"Precio (sin formato):     {precio}")
print(f"Precio (con separador):   {precio:,}")
print(f"Precio (formato local):   ${precio:,.0f}")

print()

# Porcentaje
porcentaje = 0.8567
print(f"Porcentaje: {porcentaje:.1%}")   # 85.7%
print(f"Porcentaje: {porcentaje:.0%}")   # 86%

print()

# --- Alineación y relleno ---
print("=== ALINEACIÓN ===")
print(f"{'Izquierda':<20}|")
print(f"{'Centro':^20}|")
print(f"{'Derecha':>20}|")

print()
print(f"{'Producto':<15} {'Precio':>10}")
print(f"{'-'*15} {'-'*10}")
print(f"{'Café':<15} {'$2.500':>10}")
print(f"{'Sándwich':<15} {'$4.990':>10}")
print(f"{'Agua':<15} {'$990':>10}")
