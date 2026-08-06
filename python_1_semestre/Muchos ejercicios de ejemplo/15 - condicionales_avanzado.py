# ============================================
# 15 - CONDICIONALES (AVANZADO)
# Tema: Condiciones complejas con and, or, not
# Nivel: ⭐⭐⭐⭐ Avanzado
# ============================================
# Puedes combinar múltiples condiciones usando operadores lógicos.
# and = ambas deben ser verdaderas
# or  = al menos una debe ser verdadera
# not = invierte el resultado

# --- Ejemplo: Requisitos para una beca ---
print("=== SISTEMA DE POSTULACIÓN A BECA ===")
print("Requisitos:")
print("  - Promedio >= 5.5")
print("  - Asistencia >= 80%")
print("  - Sin deuda pendiente")
print()

promedio = float(input("Ingresa tu promedio (1.0 - 7.0): "))
asistencia = int(input("Ingresa tu % de asistencia: "))
tiene_deuda = input("¿Tienes deuda pendiente? (si/no): ").lower() == "si"

if promedio >= 5.5 and asistencia >= 80 and not tiene_deuda:
    print("\n✅ ¡Cumples TODOS los requisitos! Postulación aceptada.")
elif promedio >= 5.5 and asistencia >= 80:
    print("\n⚠️ Buen rendimiento, pero tienes deuda pendiente.")
elif promedio >= 5.5:
    print("\n⚠️ Buen promedio, pero necesitas mejorar tu asistencia.")
else:
    print("\n❌ No cumples los requisitos mínimos.")

# Detalle de cada requisito
print("\n--- Detalle ---")
print(f"Promedio >= 5.5:     {'✅' if promedio >= 5.5 else '❌'} ({promedio})")
print(f"Asistencia >= 80%:   {'✅' if asistencia >= 80 else '❌'} ({asistencia}%)")
print(f"Sin deuda:           {'✅' if not tiene_deuda else '❌'}")

print()

# --- Ejemplo: Calculadora de metabolismo basal ---
print("=== CLASIFICACIÓN DE PRESIÓN ARTERIAL ===")
sistolica = int(input("Presión sistólica (número superior): "))
diastolica = int(input("Presión diastólica (número inferior): "))

if sistolica < 120 and diastolica < 80:
    print("🟢 Normal")
elif sistolica < 130 and diastolica < 80:
    print("🟡 Elevada")
elif sistolica < 140 or diastolica < 90:
    print("🟠 Hipertensión etapa 1")
elif sistolica >= 140 or diastolica >= 90:
    print("🔴 Hipertensión etapa 2")

if sistolica > 180 or diastolica > 120:
    print("🚨 ¡CRISIS HIPERTENSIVA! Busca atención médica inmediata.")
