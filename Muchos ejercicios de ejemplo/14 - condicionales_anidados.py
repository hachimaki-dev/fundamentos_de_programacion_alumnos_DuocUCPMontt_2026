# ============================================
# 14 - CONDICIONALES (ANIDADOS)
# Tema: if dentro de if
# Nivel: ⭐⭐⭐ Intermedio
# ============================================
# A veces necesitas verificar una condición DENTRO de otra.
# Esto se llama condicionales anidados.

print("=== SISTEMA DE DESCUENTO DE TIENDA ===")
print("Reglas:")
print("  - Clientes VIP: 20% de descuento")
print("  - Clientes normales que compran más de $50.000: 10%")
print("  - Clientes normales que compran más de $20.000: 5%")
print("  - Resto: sin descuento")
print()

es_vip = input("¿Eres cliente VIP? (si/no): ").lower()
monto = int(input("¿Cuánto es el total de tu compra? $"))

if es_vip == "si":
    descuento = 0.20
    print("✨ Descuento VIP aplicado: 20%")
else:
    if monto > 50000:
        descuento = 0.10
        print("Descuento por compra grande: 10%")
    elif monto > 20000:
        descuento = 0.05
        print("Descuento por compra media: 5%")
    else:
        descuento = 0.0
        print("Sin descuento")

ahorro = monto * descuento
total_final = monto - ahorro

print(f"\nMonto original: ${monto}")
print(f"Ahorro:         ${ahorro:.0f}")
print(f"Total a pagar:  ${total_final:.0f}")

print()

# --- Ejemplo: Sistema de acceso ---
print("=== SISTEMA DE ACCESO ===")
usuario = input("Usuario: ")
clave = input("Clave: ")

if usuario == "admin":
    if clave == "1234":
        print("✅ Acceso concedido como ADMINISTRADOR")
    else:
        print("❌ Clave incorrecta para admin")
elif usuario == "alumno":
    if clave == "duocuc":
        print("✅ Acceso concedido como ALUMNO")
    else:
        print("❌ Clave incorrecta para alumno")
else:
    print("❌ Usuario no reconocido")
