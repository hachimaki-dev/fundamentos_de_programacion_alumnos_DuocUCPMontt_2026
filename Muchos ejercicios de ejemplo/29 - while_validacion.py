# ============================================
# 29 - CICLO WHILE (MEDIO)
# Tema: Validación de entrada con while
# Nivel: ⭐⭐ Medio
# ============================================
# Uno de los usos más comunes del while es validar
# que el usuario ingrese datos correctos.

# --- Validar que sea un número positivo ---
print("=== VALIDAR NÚMERO POSITIVO ===")

numero = int(input("Ingresa un número positivo: "))

while numero <= 0:
    print("  ⚠ El número debe ser positivo. Intenta de nuevo.")
    numero = int(input("Ingresa un número positivo: "))

print(f"✅ Ingresaste: {numero}")

print()

# --- Validar opción de menú ---
print("=== VALIDAR OPCIÓN ===")
print("Elige un sabor:")
print("  1. Chocolate")
print("  2. Vainilla")
print("  3. Fresa")

opcion = input("Tu elección (1/2/3): ")

while opcion not in ("1", "2", "3"):
    print("  ⚠ Opción inválida.")
    opcion = input("Tu elección (1/2/3): ")

sabores = {"1": "Chocolate 🍫", "2": "Vainilla 🍦", "3": "Fresa 🍓"}
print(f"✅ Elegiste: {sabores[opcion]}")

print()

# --- Validar texto no vacío ---
print("=== VALIDAR TEXTO ===")

nombre = input("Ingresa tu nombre: ").strip()

while not nombre:
    print("  ⚠ El nombre no puede estar vacío.")
    nombre = input("Ingresa tu nombre: ").strip()

print(f"✅ Hola, {nombre}!")

print()

# --- Validar rango con reintentos contados ---
print("=== ADIVINA EL NÚMERO (1-10) ===")
secreto = 7  # número secreto
intentos = 0
max_intentos = 3

while intentos < max_intentos:
    intento = int(input(f"Intento {intentos + 1}/{max_intentos}: Adivina (1-10): "))
    intentos += 1
    
    if intento == secreto:
        print(f"🎉 ¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    elif intento < secreto:
        print("  📈 Más alto...")
    else:
        print("  📉 Más bajo...")
else:
    # Este else se ejecuta si el while terminó SIN break
    print(f"💀 Se acabaron los intentos. El número era {secreto}.")
