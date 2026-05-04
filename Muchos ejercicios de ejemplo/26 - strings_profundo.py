# ============================================
# 26 - STRINGS (PROFUNDO)
# Tema: Módulo string, textwrap y manipulación avanzada
# Nivel: ⭐⭐⭐⭐⭐ Profundo
# ============================================
# Python tiene módulos internos para manipulación avanzada de texto.

import string
import textwrap

# --- Módulo string: constantes útiles ---
print("=== MÓDULO STRING ===")
print(f"Letras minúsculas: {string.ascii_lowercase}")
print(f"Letras mayúsculas: {string.ascii_uppercase}")
print(f"Todas las letras:  {string.ascii_letters[:26]}...")
print(f"Dígitos:           {string.digits}")
print(f"Puntuación:        {string.punctuation}")

print()

# --- Generar un código aleatorio (preparación para import random) ---
# Sin random, podemos hacer algo interesante con strings:
print("=== CIFRADO CÉSAR (simple) ===")
mensaje = input("Escribe un mensaje para cifrar: ").lower()
desplazamiento = 3
alfabeto = string.ascii_lowercase

cifrado = ""
for caracter in mensaje:
    if caracter in alfabeto:
        indice = alfabeto.index(caracter)
        nuevo_indice = (indice + desplazamiento) % 26
        cifrado += alfabeto[nuevo_indice]
    else:
        cifrado += caracter  # espacios y puntuación se mantienen

print(f"Original:  {mensaje}")
print(f"Cifrado:   {cifrado}")

# Descifrar
descifrado = ""
for caracter in cifrado:
    if caracter in alfabeto:
        indice = alfabeto.index(caracter)
        nuevo_indice = (indice - desplazamiento) % 26
        descifrado += alfabeto[nuevo_indice]
    else:
        descifrado += caracter

print(f"Descifrado: {descifrado}")

print()

# --- textwrap: formatear texto largo ---
print("=== TEXTWRAP ===")
parrafo = "Python es un lenguaje de programación de alto nivel, interpretado y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. Su filosofía de diseño enfatiza la legibilidad del código."

print("--- Sin formato (una línea larga) ---")
print(parrafo)

print("\n--- Con textwrap.fill (ancho 50) ---")
print(textwrap.fill(parrafo, width=50))

print("\n--- Con textwrap.wrap (lista de líneas) ---")
lineas = textwrap.wrap(parrafo, width=40)
for i, linea in enumerate(lineas, 1):
    print(f"  Línea {i}: {linea}")

print()

# --- Análisis de texto ---
print("=== ANÁLISIS DE TEXTO ===")
texto = input("Escribe un texto para analizar: ")

letras = sum(1 for c in texto if c.isalpha())
numeros = sum(1 for c in texto if c.isdigit())
espacios = sum(1 for c in texto if c.isspace())
especiales = sum(1 for c in texto if c in string.punctuation)

print(f"\n📊 Análisis del texto:")
print(f"  Total caracteres: {len(texto)}")
print(f"  Letras:           {letras}")
print(f"  Números:          {numeros}")
print(f"  Espacios:         {espacios}")
print(f"  Especiales:       {especiales}")
print(f"  Palabras:         {len(texto.split())}")

# Carácter más frecuente
if texto:
    mas_frecuente = max(set(texto.lower()), key=texto.lower().count)
    print(f"  Carácter más frecuente: '{mas_frecuente}' ({texto.lower().count(mas_frecuente)} veces)")
