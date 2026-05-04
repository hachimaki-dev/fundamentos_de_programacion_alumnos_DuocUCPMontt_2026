# ============================================
# 21 - OPERADORES LÓGICOS (PROFUNDO)
# Tema: Módulo operator, all(), any(), y buenas prácticas
# Nivel: ⭐⭐⭐⭐⭐ Profundo
# ============================================
# Python tiene funciones integradas y un módulo para trabajar
# con lógica de forma más avanzada.

import operator

# --- Módulo operator: operadores como funciones ---
print("=== MÓDULO OPERATOR ===")
a, b = 10, 20

print(f"operator.eq({a}, {b})  = {operator.eq(a, b)}")    # ==
print(f"operator.ne({a}, {b})  = {operator.ne(a, b)}")    # !=
print(f"operator.gt({a}, {b})  = {operator.gt(a, b)}")    # >
print(f"operator.lt({a}, {b})  = {operator.lt(a, b)}")    # <
print(f"operator.ge({a}, {b})  = {operator.ge(a, b)}")    # >=
print(f"operator.le({a}, {b})  = {operator.le(a, b)}")    # <=
print(f"operator.and_(True, False) = {operator.and_(True, False)}")
print(f"operator.or_(True, False)  = {operator.or_(True, False)}")
print(f"operator.not_(True)        = {operator.not_(True)}")

print()

# --- all() y any() ---
print("=== ALL() Y ANY() ===")
# all() = True si TODOS son True (como and encadenado)
# any() = True si AL MENOS UNO es True (como or encadenado)

notas = [5.5, 6.0, 4.5, 5.0, 6.5]
print(f"Notas: {notas}")

todas_aprobadas = all(nota >= 4.0 for nota in notas)
alguna_sobre_6 = any(nota >= 6.0 for nota in notas)
alguna_reprobada = any(nota < 4.0 for nota in notas)

print(f"¿Todas aprobadas (>= 4.0)? {todas_aprobadas}")
print(f"¿Alguna sobre 6.0?         {alguna_sobre_6}")
print(f"¿Alguna reprobada (< 4.0)? {alguna_reprobada}")

print()

# --- Validación completa con all() ---
print("=== VALIDACIÓN DE FORMULARIO ===")
nombre = input("Nombre: ")
email = input("Email: ")
edad_txt = input("Edad: ")

validaciones = {
    "Nombre no vacío": len(nombre) > 0,
    "Email contiene @": "@" in email,
    "Email contiene .": "." in email,
    "Edad es número": edad_txt.isdigit(),
}

print("\n--- Resultado de validación ---")
for campo, valido in validaciones.items():
    print(f"  {campo}: {'✅' if valido else '❌'}")

if all(validaciones.values()):
    print("\n✅ Formulario válido")
else:
    campos_invalidos = [campo for campo, valido in validaciones.items() if not valido]
    print(f"\n❌ Formulario inválido. Errores: {', '.join(campos_invalidos)}")

print()

# --- Operador in para verificar pertenencia ---
print("=== OPERADOR 'IN' ===")
frutas_disponibles = "manzana, naranja, plátano, uva, fresa"
buscar = input("¿Qué fruta buscas? ").lower()

if buscar in frutas_disponibles:
    print(f"✅ '{buscar}' está disponible")
else:
    print(f"❌ '{buscar}' no está disponible")
