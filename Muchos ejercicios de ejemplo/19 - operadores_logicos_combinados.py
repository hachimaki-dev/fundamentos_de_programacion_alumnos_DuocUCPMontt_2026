# ============================================
# 19 - OPERADORES LÓGICOS (COMBINADOS)
# Tema: Combinando comparaciones y lógica
# Nivel: ⭐⭐⭐ Intermedio
# ============================================
# En la vida real, las decisiones dependen de múltiples factores.
# Aquí practicamos combinaciones más complejas.

# --- Ejemplo: Sistema de préstamo bancario ---
print("=== SIMULADOR DE PRÉSTAMO ===")
print("Requisitos:")
print("  1. Edad entre 21 y 65 años")
print("  2. Sueldo >= $500.000 O tener aval")
print("  3. Sin antecedentes negativos")
print()

edad = int(input("Edad: "))
sueldo = int(input("Sueldo mensual: $"))
tiene_aval = input("¿Tienes un aval? (si/no): ").lower() == "si"
antecedentes_limpios = input("¿Antecedentes limpios? (si/no): ").lower() == "si"

requisito_edad = 21 <= edad <= 65
requisito_ingresos = sueldo >= 500000 or tiene_aval
requisito_antecedentes = antecedentes_limpios

aprobado = requisito_edad and requisito_ingresos and requisito_antecedentes

print("\n--- Evaluación ---")
print(f"  Edad válida (21-65):         {'✅' if requisito_edad else '❌'}")
print(f"  Ingresos suficientes o aval: {'✅' if requisito_ingresos else '❌'}")
print(f"  Antecedentes limpios:        {'✅' if requisito_antecedentes else '❌'}")
print(f"\n{'✅ PRÉSTAMO APROBADO' if aprobado else '❌ PRÉSTAMO RECHAZADO'}")

print()

# --- Ejemplo: Diagnóstico simple ---
print("=== DIAGNÓSTICO DE SÍNTOMAS ===")
fiebre = input("¿Tienes fiebre? (si/no): ").lower() == "si"
tos = input("¿Tienes tos? (si/no): ").lower() == "si"
dolor_cabeza = input("¿Tienes dolor de cabeza? (si/no): ").lower() == "si"
dolor_cuerpo = input("¿Tienes dolor de cuerpo? (si/no): ").lower() == "si"

sintomas = 0
if fiebre: sintomas += 1
if tos: sintomas += 1
if dolor_cabeza: sintomas += 1
if dolor_cuerpo: sintomas += 1

print(f"\nSíntomas reportados: {sintomas}/4")

if fiebre and tos and dolor_cuerpo:
    print("⚠️ Posible gripe. Consulta a un médico.")
elif fiebre and dolor_cabeza and not tos:
    print("⚠️ Podría ser una infección. Consulta a un médico.")
elif sintomas >= 3:
    print("⚠️ Varios síntomas detectados. Es recomendable consultar.")
elif sintomas >= 1:
    print("💊 Síntomas leves. Descansa y mantente hidratado.")
else:
    print("✅ No reportaste síntomas. ¡Estás bien!")
