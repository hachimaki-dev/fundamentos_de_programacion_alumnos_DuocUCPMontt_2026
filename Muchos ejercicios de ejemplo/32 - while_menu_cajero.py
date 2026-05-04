# ============================================
# 32 - CICLO WHILE (AVANZADO)
# Tema: Sistema de menú interactivo
# Nivel: ⭐⭐⭐⭐⭐ Avanzado
# ============================================
# Los menús interactivos son una aplicación clásica del while.
# El programa se mantiene ejecutando hasta que el usuario decide salir.

print("=" * 45)
print("  🏦 SIMULADOR DE CAJERO AUTOMÁTICO")
print("=" * 45)

saldo = 100000  # saldo inicial

while True:
    print(f"\n  💰 Saldo actual: ${saldo:,}")
    print("  ─" * 20)
    print("  1. 💵 Consultar saldo")
    print("  2. 📥 Depositar")
    print("  3. 📤 Retirar")
    print("  4. 📊 Historial")
    print("  5. 🚪 Salir")
    print("  ─" * 20)
    
    opcion = input("  Selecciona una opción: ")
    
    if opcion == "1":
        print(f"\n  💰 Tu saldo es: ${saldo:,}")
        
    elif opcion == "2":
        monto = int(input("  ¿Cuánto deseas depositar? $"))
        if monto > 0:
            saldo += monto
            print(f"  ✅ Depósito exitoso. Nuevo saldo: ${saldo:,}")
        else:
            print("  ❌ Monto inválido")
            
    elif opcion == "3":
        monto = int(input("  ¿Cuánto deseas retirar? $"))
        if monto <= 0:
            print("  ❌ Monto inválido")
        elif monto > saldo:
            print(f"  ❌ Fondos insuficientes. Tu saldo es ${saldo:,}")
        else:
            saldo -= monto
            print(f"  ✅ Retiro exitoso. Nuevo saldo: ${saldo:,}")
            
    elif opcion == "4":
        print("  📊 (Función no implementada aún)")
        print("  💡 Pista: Con listas podrías guardar el historial")
        
    elif opcion == "5":
        print(f"\n  💰 Saldo final: ${saldo:,}")
        print("  👋 ¡Gracias por usar nuestro cajero!")
        break
        
    else:
        print("  ❌ Opción no válida. Intenta de nuevo.")
