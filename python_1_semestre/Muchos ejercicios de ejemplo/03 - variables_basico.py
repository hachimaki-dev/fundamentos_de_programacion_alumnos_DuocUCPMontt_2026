# ============================================
# 03 - VARIABLES Y TIPOS DE DATOS (BÁSICO)
# Tema: Crear variables y conocer los tipos básicos
# Nivel: ⭐ Básico
# ============================================
# Una variable es como una caja donde guardas un dato.
# Python detecta automáticamente el tipo de dato.

# --- Tipos básicos ---
nombre = "Carlos"          # str  (texto/cadena)
edad = 21                  # int  (número entero)
altura = 1.75              # float (número decimal)
es_estudiante = True       # bool (verdadero o falso)

# --- Imprimir variables ---
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)

print()

# --- Verificar el tipo de cada variable con type() ---
print("Tipo de nombre:", type(nombre))
print("Tipo de edad:", type(edad))
print("Tipo de altura:", type(altura))
print("Tipo de es_estudiante:", type(es_estudiante))
