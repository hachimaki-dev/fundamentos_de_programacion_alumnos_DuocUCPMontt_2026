# ============================================
# 07 - ENTRADA DE DATOS (MEDIO)
# Tema: Convertir input y hacer cálculos
# Nivel: ⭐⭐ Medio
# ============================================
# Como input() siempre devuelve str, debemos convertirlo
# a int o float si queremos hacer operaciones matemáticas.

print("=== CALCULADORA DE EDAD ===")

nombre = input("Ingresa tu nombre: ")
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

edad = 2026 - anio_nacimiento
print(f"{nombre}, tienes (o cumplirás) {edad} años en 2026.")

print()
print("=== CÁLCULO DE PROMEDIO ===")

nota1 = float(input("Ingresa tu nota 1: "))
nota2 = float(input("Ingresa tu nota 2: "))
nota3 = float(input("Ingresa tu nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3
print(f"Tu promedio es: {promedio:.1f}")

print()
print("=== DATOS PERSONALES ===")

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros (ej: 1.75): "))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")
