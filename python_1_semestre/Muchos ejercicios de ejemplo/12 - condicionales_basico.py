# ============================================
# 12 - CONDICIONALES (BÁSICO)
# Tema: if y else
# Nivel: ⭐ Básico
# ============================================
# Los condicionales permiten que tu programa tome decisiones.
# if = "si se cumple esto, haz esto"
# else = "si no se cumple, haz esto otro"

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad ✅")
else:
    print("Eres menor de edad 🔒")

print()

# --- Otro ejemplo: par o impar ---
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"{numero} es PAR")
else:
    print(f"{numero} es IMPAR")

print()

# --- Otro ejemplo: positivo o negativo ---
valor = float(input("Ingresa un valor: "))

if valor >= 0:
    print("El valor es positivo (o cero)")
else:
    print("El valor es negativo")
