# ============================================
# 20 - OPERADORES LÓGICOS (AVANZADO)
# Tema: Short-circuit evaluation y valor de retorno
# Nivel: ⭐⭐⭐⭐ Avanzado
# ============================================
# Python es "perezoso": si ya sabe el resultado, no evalúa el resto.
# Esto se llama "evaluación de cortocircuito" (short-circuit).

# --- Short-circuit con AND ---
# Si el primero es False, no evalúa el segundo
print("=== SHORT-CIRCUIT: AND ===")
x = 0
# x != 0 es False, así que Python NO evalúa 10/x (evita división por cero)
if x != 0 and 10 / x > 2:
    print("Resultado mayor que 2")
else:
    print("x es cero o el resultado no es mayor que 2")

print()

# --- Short-circuit con OR ---
# Si el primero es True, no evalúa el segundo
print("=== SHORT-CIRCUIT: OR ===")
nombre = ""
nombre_mostrar = nombre or "Anónimo"  # Si nombre es vacío (falsy), usa "Anónimo"
print(f"Nombre: {nombre_mostrar}")

usuario = input("Ingresa tu nombre (o deja vacío): ")
saludo = usuario or "Invitado"
print(f"¡Hola, {saludo}!")

print()

# --- Valores Truthy y Falsy ---
print("=== VALORES TRUTHY Y FALSY ===")
print("Los siguientes valores son FALSY (se comportan como False):")
valores_falsy = [0, 0.0, "", None, False]
for valor in valores_falsy:
    print(f"  bool({valor!r:10}) = {bool(valor)}")

print()
print("Los siguientes valores son TRUTHY (se comportan como True):")
valores_truthy = [1, -1, 3.14, "hola", True, " "]
for valor in valores_truthy:
    print(f"  bool({valor!r:10}) = {bool(valor)}")

print()

# --- Aplicación práctica de Truthy/Falsy ---
print("=== USO PRÁCTICO ===")
texto = input("Escribe algo (o deja vacío): ")

# En vez de: if texto != "":
if texto:
    print(f"Escribiste: {texto}")
else:
    print("No escribiste nada")

# En vez de: if len(texto) > 0:
cantidad = len(texto) if texto else 0
print(f"Caracteres: {cantidad}")
