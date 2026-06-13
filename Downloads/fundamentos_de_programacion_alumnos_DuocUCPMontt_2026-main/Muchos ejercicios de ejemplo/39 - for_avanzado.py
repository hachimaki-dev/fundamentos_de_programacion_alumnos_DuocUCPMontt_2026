# ============================================
# 39 - CICLO FOR (AVANZADO)
# Tema: enumerate(), zip(), y comprensiones de vista previa
# Nivel: ⭐⭐⭐⭐⭐ Avanzado
# ============================================
# Python tiene funciones que hacen el for más poderoso.
# Esto es preparación para cuando vean listas en profundidad.

# --- enumerate(): obtener índice y valor ---
print("=== ENUMERATE ===")
frutas = ["manzana", "naranja", "plátano", "uva", "fresa"]

print("Recorrido normal:")
for fruta in frutas:
    print(f"  {fruta}")

print("\nCon enumerate (índice + valor):")
for indice, fruta in enumerate(frutas):
    print(f"  [{indice}] {fruta}")

print("\nCon enumerate empezando en 1:")
for numero, fruta in enumerate(frutas, start=1):
    print(f"  {numero}. {fruta}")

print()

# --- zip(): recorrer dos secuencias en paralelo ---
print("=== ZIP ===")
nombres = ["Carlos", "Ana", "Pedro", "María", "Luis"]
notas = [6.5, 5.8, 4.2, 7.0, 3.9]

print(f"{'Nombre':<12} {'Nota':>5} {'Estado':<12}")
print("-" * 32)

for nombre, nota in zip(nombres, notas):
    estado = "Aprobado ✅" if nota >= 4.0 else "Reprobado ❌"
    print(f"{nombre:<12} {nota:>5.1f} {estado}")

print()

# --- Combinar enumerate y zip ---
print("=== ENUMERATE + ZIP ===")
materias = ["Programación", "Base de Datos", "Redes", "Matemáticas"]
profesores = ["Prof. García", "Prof. López", "Prof. Muñoz", "Prof. Díaz"]

for i, (materia, profesor) in enumerate(zip(materias, profesores), start=1):
    print(f"  {i}. {materia} - {profesor}")

print()

# --- Recorrer un string con enumerate ---
print("=== BUSCAR POSICIONES ===")
texto = input("Escribe un texto: ")
buscar = input("¿Qué carácter buscas? ")

posiciones = []
for i, c in enumerate(texto):
    if c.lower() == buscar.lower():
        posiciones.append(i)

if posiciones:
    print(f"'{buscar}' encontrado en posiciones: {posiciones}")
else:
    print(f"'{buscar}' no se encontró en el texto")

print()

# --- Vista previa: list comprehension ---
print("=== VISTA PREVIA: COMPRENSIONES ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Forma tradicional
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)
print(f"Cuadrados (for):           {cuadrados}")

# List comprehension (una línea)
cuadrados_v2 = [n ** 2 for n in numeros]
print(f"Cuadrados (comprehension): {cuadrados_v2}")

# Con filtro
pares = [n for n in numeros if n % 2 == 0]
print(f"Solo pares:                {pares}")
