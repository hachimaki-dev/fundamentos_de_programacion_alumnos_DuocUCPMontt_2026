# ============================================
# 13 - CONDICIONALES (MEDIO)
# Tema: if / elif / else
# Nivel: ⭐⭐ Medio
# ============================================
# Cuando hay más de 2 opciones, usamos elif (else if).
# Python evalúa de arriba hacia abajo y ejecuta el primer bloque verdadero.

print("=== CALIFICACIÓN POR NOTA ===")
nota = float(input("Ingresa tu nota (1.0 a 7.0): "))

if nota >= 6.0:
    print("¡Excelente! 🌟")
elif nota >= 5.0:
    print("Muy bien 👍")
elif nota >= 4.0:
    print("Aprobado ✅")
elif nota >= 3.0:
    print("Insuficiente ⚠️")
else:
    print("Reprobado ❌")

print()

# --- Ejemplo: Estaciones del año ---
print("=== ESTACIÓN DEL AÑO ===")
mes = int(input("Ingresa el número del mes (1-12): "))

if mes in (12, 1, 2):
    print("🌞 Es verano (en Chile)")
elif mes in (3, 4, 5):
    print("🍂 Es otoño")
elif mes in (6, 7, 8):
    print("❄️ Es invierno")
elif mes in (9, 10, 11):
    print("🌸 Es primavera")
else:
    print("❌ Mes inválido")

print()

# --- Ejemplo: Categoría de entrada ---
print("=== CATEGORÍA DE EDAD ===")
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
elif edad <= 2:
    print("Bebé 👶")
elif edad <= 12:
    print("Niño/a 🧒")
elif edad <= 17:
    print("Adolescente 🧑")
elif edad <= 64:
    print("Adulto 🧑‍💼")
else:
    print("Adulto mayor 👴")
