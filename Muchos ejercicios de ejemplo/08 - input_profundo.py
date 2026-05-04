# ============================================
# 08 - ENTRADA DE DATOS (PROFUNDO)
# Tema: Validación de input y manejo de errores
# Nivel: ⭐⭐⭐ Profundo
# ============================================
# ¿Qué pasa si el usuario escribe "hola" cuando pides un número?
# Python lanza un error (ValueError). Podemos manejarlo con try/except.

# --- Manejo básico de errores ---
print("=== INGRESO SEGURO DE NÚMERO ===")

try:
    numero = int(input("Ingresa un número entero: "))
    print(f"Ingresaste el número: {numero}")
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("¡Error! Eso no es un número entero válido.")

print()

# --- Validación con while + try/except ---
print("=== INGRESO CON REINTENTO ===")

while True:
    try:
        edad = int(input("Ingresa tu edad (número entero): "))
        break  # Si no hay error, salimos del bucle
    except ValueError:
        print("  ⚠ Debes ingresar un número. Intenta de nuevo.")

print(f"Tu edad es: {edad}")

print()

# --- Validar rango ---
print("=== INGRESO CON RANGO VÁLIDO ===")

while True:
    try:
        nota = float(input("Ingresa una nota (1.0 a 7.0): "))
        if 1.0 <= nota <= 7.0:
            break
        else:
            print("  ⚠ La nota debe estar entre 1.0 y 7.0")
    except ValueError:
        print("  ⚠ Debes ingresar un número válido.")

print(f"Nota registrada: {nota}")

print()

# --- Múltiples valores en una línea con split() ---
print("=== MÚLTIPLES VALORES ===")
entrada = input("Ingresa 3 números separados por espacio: ")
partes = entrada.split()  # Divide el texto por espacios

if len(partes) == 3:
    try:
        n1, n2, n3 = float(partes[0]), float(partes[1]), float(partes[2])
        print(f"Números: {n1}, {n2}, {n3}")
        print(f"Suma: {n1 + n2 + n3}")
    except ValueError:
        print("  ⚠ Alguno de los valores no es un número válido.")
else:
    print(f"  ⚠ Se esperaban 3 números, pero recibí {len(partes)}")
