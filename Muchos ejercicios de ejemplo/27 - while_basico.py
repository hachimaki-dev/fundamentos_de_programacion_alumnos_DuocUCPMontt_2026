# ============================================
# 27 - CICLO WHILE (BÁSICO)
# Tema: Tu primer bucle
# Nivel: ⭐ Básico
# ============================================
# El ciclo while repite un bloque de código mientras
# una condición sea verdadera (True).
# ¡CUIDADO! Si la condición nunca es False, el programa se queda pegado.

# --- Contar del 1 al 5 ---
print("=== CONTAR DEL 1 AL 5 ===")
contador = 1

while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # MUY IMPORTANTE: actualizar la variable

print("¡Fin del conteo!")

print()

# --- Cuenta regresiva ---
print("=== CUENTA REGRESIVA ===")
numero = 10

while numero > 0:
    print(numero, end="... ")
    numero -= 1

print("🚀 ¡Despegue!")

print()

# --- Repetir un mensaje ---
print("=== REPETIR MENSAJE ===")
veces = int(input("¿Cuántas veces quieres saludar? "))
i = 0

while i < veces:
    print(f"  ¡Hola! (saludo #{i + 1})")
    i += 1

print("Listo, terminé de saludar.")
