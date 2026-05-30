# ============================================
# 01 - HOLA MUNDO (MEDIO)
# Tema: print() con parámetros especiales
# Nivel: ⭐⭐ Medio
# ============================================
# print() tiene parámetros como sep (separador) y end (final de línea).
# También puedes usar caracteres especiales como \n (nueva línea) y \t (tabulación).

# --- Caracteres especiales ---
print("Línea 1\nLínea 2\nLínea 3")
print("Nombre:\tCarlos")
print("Edad:\t21")

print()  # línea vacía para separar

# --- Parámetro sep: define qué va entre cada valor ---
print("Python", "es", "genial", sep=" ")       # separado por espacio (por defecto)
print("Python", "es", "genial", sep=" - ")      # separado por guión
print("2026", "03", "30", sep="/")              # como fecha
print("192", "168", "1", "1", sep=".")          # como IP

print()

# --- Parámetro end: define qué va al final del print ---
print("Cargando", end="")
print("...", end="")
print(" ¡Listo!")

print()

# --- Combinando sep y end ---
print("A", "B", "C", sep=" | ", end=" <-- letras\n")
