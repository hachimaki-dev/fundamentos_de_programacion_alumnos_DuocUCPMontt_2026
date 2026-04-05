# ============================================
# 16 - CONDICIONALES (PROFUNDO)
# Tema: Operador ternario, match/case, y patrones avanzados
# Nivel: ⭐⭐⭐⭐⭐ Profundo
# ============================================
# Python tiene formas más concisas de escribir condicionales.
# También veremos match/case (Python 3.10+).

# --- Operador ternario (condicional en una línea) ---
print("=== OPERADOR TERNARIO ===")
edad = int(input("Ingresa tu edad: "))

# Forma larga:
# if edad >= 18:
#     estado = "mayor"
# else:
#     estado = "menor"

# Forma corta (ternario):
estado = "mayor de edad" if edad >= 18 else "menor de edad"
print(f"Eres {estado}")

nota = float(input("Ingresa tu nota: "))
resultado = "Aprobado ✅" if nota >= 4.0 else "Reprobado ❌"
print(resultado)

print()

# --- match/case (switch moderno, Python 3.10+) ---
print("=== MATCH/CASE (MENÚ) ===")
print("1. Ver saldo")
print("2. Depositar")
print("3. Retirar")
print("4. Salir")
opcion = input("Selecciona una opción: ")

match opcion:
    case "1":
        print("💰 Tu saldo es: $150.000")
    case "2":
        print("📥 Función de depósito")
    case "3":
        print("📤 Función de retiro")
    case "4":
        print("👋 ¡Hasta luego!")
    case _:
        print("❌ Opción no válida")

print()

# --- Condicionales con múltiples retornos simulados ---
print("=== CALCULADORA CON VALIDACIÓN ===")
num1 = float(input("Número 1: "))
operador = input("Operador (+, -, *, /): ")
num2 = float(input("Número 2: "))

# Usar diccionario como alternativa a múltiples if/elif
# (preparación para cuando vean diccionarios)
es_valido = operador in ("+", "-", "*", "/")
es_division_cero = operador == "/" and num2 == 0

if not es_valido:
    print("❌ Operador no válido")
elif es_division_cero:
    print("❌ No se puede dividir por cero")
else:
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    else:
        resultado = num1 / num2
    
    print(f"{num1} {operador} {num2} = {resultado}")

print()

# --- Encadenamiento de comparaciones (pythonic) ---
print("=== RANGOS PYTHONIC ===")
temperatura = float(input("Temperatura actual (°C): "))

# En vez de: if temperatura >= 15 and temperatura <= 25:
if 15 <= temperatura <= 25:
    print("🌡️ Temperatura agradable")
elif 0 <= temperatura < 15:
    print("🧥 Hace frío, abrígate")
elif -10 <= temperatura < 0:
    print("🥶 ¡Hace mucho frío!")
elif temperatura > 25:
    print("🔥 ¡Hace calor!")
else:
    print("🧊 Temperatura extremadamente baja")
