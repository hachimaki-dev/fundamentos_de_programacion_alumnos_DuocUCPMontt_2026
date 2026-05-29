# ============================================
# 25 - STRINGS (AVANZADO)
# Tema: Slicing, operador in, y split/join
# Nivel: ⭐⭐⭐⭐ Avanzado
# ============================================
# El slicing permite extraer porciones de un string.
# Es una de las características más poderosas de Python.

# --- Slicing básico: string[inicio:fin] ---
texto = "Fundamentos de Python"
#        0123456789...

print(f"Texto: '{texto}'")
print(f"texto[0:12]   = '{texto[0:12]}'")      # "Fundamentos "
print(f"texto[:12]    = '{texto[:12]}'")        # mismo (inicio por defecto = 0)
print(f"texto[16:]    = '{texto[16:]}'")        # "ython" (hasta el final)
print(f"texto[-6:]    = '{texto[-6:]}'")        # "Python" (últimos 6)
print(f"texto[0:12:2] = '{texto[0:12:2]}'")    # cada 2 caracteres

print()

# --- Invertir un string ---
print(f"Invertido: '{texto[::-1]}'")

print()

# --- Operador 'in' ---
print("=== OPERADOR IN ===")
email = input("Ingresa tu email: ")

if "@" in email and "." in email:
    print("✅ Parece un email válido")
else:
    print("❌ No parece un email válido")

print()

# --- split(): dividir texto en una lista ---
print("=== SPLIT ===")
frase = "Python es el mejor lenguaje para aprender"
palabras = frase.split()  # divide por espacios
print(f"Frase: '{frase}'")
print(f"Palabras: {palabras}")
print(f"Cantidad de palabras: {len(palabras)}")

print()

csv_data = "Carlos,21,Informática,Puerto Montt"
campos = csv_data.split(",")  # divide por comas
print(f"CSV: '{csv_data}'")
print(f"Campos: {campos}")
print(f"Nombre: {campos[0]}, Edad: {campos[1]}")

print()

# --- join(): unir elementos con un separador ---
print("=== JOIN ===")
partes = ["Python", "es", "genial"]
unido = " ".join(partes)
print(f"Lista: {partes}")
print(f"Unido con espacio: '{unido}'")

ruta = "/".join(["home", "alumno", "documentos"])
print(f"Ruta: '{ruta}'")

guiones = " - ".join(["uno", "dos", "tres"])
print(f"Con guiones: '{guiones}'")

print()

# --- Ejemplo práctico: procesar un nombre completo ---
print("=== PROCESAR NOMBRE ===")
nombre_completo = input("Ingresa tu nombre completo: ")
partes = nombre_completo.strip().split()

if len(partes) >= 2:
    print(f"Nombre: {partes[0].title()}")
    print(f"Apellido: {partes[-1].title()}")
    print(f"Iniciales: {''.join(p[0].upper() for p in partes)}")
else:
    print(f"Nombre: {partes[0].title()}")
