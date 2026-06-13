# ============================================
# 40 - CICLO FOR (PROFUNDO)
# Tema: itertools, patrones complejos y preparación
#       para listas/funciones/objetos
# Nivel: ⭐⭐⭐⭐⭐⭐⭐ Profundo
# ============================================
# Usamos el módulo itertools y patrones avanzados
# para preparar la transición a listas, funciones y objetos.

import itertools
import random

# --- itertools.count: contador infinito ---
print("=== ITERTOOLS.COUNT ===")
print("Primeros 10 números empezando desde 100, de 5 en 5:")
for num in itertools.islice(itertools.count(100, 5), 10):
    print(num, end=" ")
print()

print()

# --- itertools.chain: encadenar secuencias ---
print("=== ITERTOOLS.CHAIN ===")
letras = "ABC"
numeros = "123"
simbolos = "!@#"

for item in itertools.chain(letras, numeros, simbolos):
    print(item, end=" ")
print()

print()

# --- itertools.product: producto cartesiano ---
print("=== COMBINACIONES DE CARTAS ===")
palos = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Mostrar solo las primeras 10 cartas
print("Primeras 10 cartas del mazo:")
for i, (valor, palo) in enumerate(itertools.product(valores, palos)):
    if i >= 10:
        break
    print(f"  {valor}{palo}", end="")
print(f"\n  ... (total: {len(valores) * len(palos)} cartas)")

print()

# --- Programa integrador: Quiz interactivo ---
print("=" * 50)
print("  🎓 QUIZ DE PYTHON - Preparación Final")
print("=" * 50)

preguntas = [
    ("¿Qué función se usa para imprimir en consola?", "print"),
    ("¿Qué tipo de dato es 3.14?", "float"),
    ("¿Qué operador calcula el resto de una división?", "%"),
    ("¿Cómo se llama un bucle que se repite mientras una condición es True?", "while"),
    ("¿Qué función convierte texto a número entero?", "int"),
]

random.shuffle(preguntas)  # mezclar preguntas

puntos = 0
total = len(preguntas)

for i, (pregunta, respuesta_correcta) in enumerate(preguntas, start=1):
    print(f"\nPregunta {i}/{total}:")
    print(f"  {pregunta}")
    respuesta = input("  Tu respuesta: ").strip().lower()
    
    if respuesta == respuesta_correcta.lower():
        print("  ✅ ¡Correcto!")
        puntos += 1
    else:
        print(f"  ❌ Incorrecto. La respuesta era: {respuesta_correcta}")

# Resultado final
print("\n" + "=" * 50)
porcentaje = (puntos / total) * 100
print(f"  Resultado: {puntos}/{total} ({porcentaje:.0f}%)")

if porcentaje == 100:
    print("  🏆 ¡PERFECTO! Estás listo para listas y funciones")
elif porcentaje >= 60:
    print("  👍 ¡Bien! Repasa los temas que fallaste")
else:
    print("  📚 Necesitas repasar. ¡Vuelve a los ejercicios!")
print("=" * 50)

print()

# --- Vista previa: patrón que parece un "objeto" ---
print("=== PREPARACIÓN PARA OBJETOS ===")
print("(Los diccionarios son la antesala de los objetos)")

# Simulamos "objetos" con diccionarios (siguiente tema)
alumno1 = {"nombre": "Carlos", "nota": 6.5}
alumno2 = {"nombre": "Ana", "nota": 5.2}
alumno3 = {"nombre": "Pedro", "nota": 4.0}

alumnos = [alumno1, alumno2, alumno3]

print(f"\n{'Nombre':<12} {'Nota':>6} {'Estado':<12}")
print("-" * 32)

for alumno in alumnos:
    estado = "Aprobado ✅" if alumno["nota"] >= 4.0 else "Reprobado ❌"
    print(f"{alumno['nombre']:<12} {alumno['nota']:>6.1f} {estado}")

# Resumen estadístico
notas = [a["nota"] for a in alumnos]
print(f"\nPromedio: {sum(notas) / len(notas):.2f}")
print(f"Mejor nota: {max(notas)}")
print(f"Peor nota: {min(notas)}")
print(f"Aprobados: {sum(1 for n in notas if n >= 4.0)}/{len(notas)}")
