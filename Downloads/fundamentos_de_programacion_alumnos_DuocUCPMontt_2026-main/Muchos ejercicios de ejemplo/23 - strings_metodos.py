# ============================================
# 23 - STRINGS (MEDIO)
# Tema: Métodos de string más usados
# Nivel: ⭐⭐ Medio
# ============================================
# Los strings tienen muchos métodos útiles.
# Un método es una función que "pertenece" al string.

texto = "  Hola Mundo desde Python  "

print(f"Original: '{texto}'")
print("-" * 40)

# --- Transformar mayúsculas/minúsculas ---
print(f".upper()      → '{texto.upper()}'")
print(f".lower()      → '{texto.lower()}'")
print(f".title()      → '{texto.title()}'")
print(f".capitalize() → '{texto.capitalize()}'")
print(f".swapcase()   → '{texto.swapcase()}'")

print()

# --- Eliminar espacios ---
print(f".strip()  → '{texto.strip()}'")       # ambos lados
print(f".lstrip() → '{texto.lstrip()}'")       # lado izquierdo
print(f".rstrip() → '{texto.rstrip()}'")       # lado derecho

print()

# --- Buscar y reemplazar ---
frase = "Me gusta programar en Python. Python es genial."

print(f"Frase: '{frase}'")
print(f".count('Python')     → {frase.count('Python')}")
print(f".find('Python')      → {frase.find('Python')}")       # posición de la primera aparición
print(f".find('Java')        → {frase.find('Java')}")         # -1 si no existe
print(f".replace('Python', 'JavaScript') → '{frase.replace('Python', 'JavaScript')}'")

print()

# --- Verificar contenido ---
codigo = "ABC123"
print(f"Texto: '{codigo}'")
print(f".isalpha()    → {codigo.isalpha()}")    # ¿solo letras?
print(f".isdigit()    → {codigo.isdigit()}")    # ¿solo números?
print(f".isalnum()    → {codigo.isalnum()}")    # ¿letras y/o números?
print(f".isspace()    → {codigo.isspace()}")    # ¿solo espacios?

print()

# --- Comprobar inicio y fin ---
archivo = "documento.pdf"
print(f"Archivo: '{archivo}'")
print(f".startswith('doc')  → {archivo.startswith('doc')}")
print(f".endswith('.pdf')   → {archivo.endswith('.pdf')}")
print(f".endswith('.txt')   → {archivo.endswith('.txt')}")
