# ============================================
# 18 - OPERADORES LÓGICOS (MEDIO)
# Tema: and, or, not
# Nivel: ⭐⭐ Medio
# ============================================
# Los operadores lógicos combinan condiciones booleanas.
# and = Verdadero si AMBAS son verdaderas
# or  = Verdadero si AL MENOS UNA es verdadera
# not = Invierte el valor (True → False, False → True)

print("=== TABLA DE VERDAD: AND ===")
print(f"True  and True  = {True and True}")
print(f"True  and False = {True and False}")
print(f"False and True  = {False and True}")
print(f"False and False = {False and False}")

print()
print("=== TABLA DE VERDAD: OR ===")
print(f"True  or True  = {True or True}")
print(f"True  or False = {True or False}")
print(f"False or True  = {False or True}")
print(f"False or False = {False or False}")

print()
print("=== TABLA DE VERDAD: NOT ===")
print(f"not True  = {not True}")
print(f"not False = {not False}")

print()

# --- Ejemplo práctico: ¿Puede entrar al cine? ---
print("=== ¿PUEDES ENTRAR AL CINE? ===")
edad = int(input("¿Cuántos años tienes? "))
tiene_permiso = input("¿Tienes permiso de tus padres? (si/no): ").lower() == "si"
es_pelicula_terror = input("¿Es película de terror? (si/no): ").lower() == "si"

if es_pelicula_terror:
    if edad >= 18 or (edad >= 14 and tiene_permiso):
        print("✅ Puedes ver la película de terror")
    else:
        print("❌ No puedes ver esta película")
else:
    print("✅ Puedes ver la película")

print()

# --- Ejemplo: Validación de contraseña ---
print("=== VALIDACIÓN DE CONTRASEÑA ===")
clave = input("Crea una contraseña: ")

tiene_largo = len(clave) >= 8
tiene_numero = False
for c in clave:
    if c.isdigit():
        tiene_numero = True
        break

es_valida = tiene_largo and tiene_numero

print(f"  Largo >= 8: {'✅' if tiene_largo else '❌'}")
print(f"  Tiene número: {'✅' if tiene_numero else '❌'}")
print(f"  Contraseña válida: {'✅' if es_valida else '❌'}")
