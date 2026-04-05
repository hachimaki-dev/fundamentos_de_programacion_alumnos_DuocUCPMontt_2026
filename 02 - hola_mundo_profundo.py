# ============================================
# 02 - HOLA MUNDO (PROFUNDO)
# Tema: print() avanzado y sys.stdout
# Nivel: ⭐⭐⭐ Profundo
# ============================================
# Exploramos formas avanzadas de imprimir en la consola.
# Introducimos sys.stdout que es la salida estándar del sistema.

import sys

# --- Arte ASCII con print ---
print("=" * 40)
print("  ____        _   _                 ")
print(" |  _ \\ _   _| |_| |__   ___  _ __  ")
print(" | |_) | | | | __| '_ \\ / _ \\| '_ \\ ")
print(" |  __/| |_| | |_| | | | (_) | | | |")
print(" |_|    \\__, |\\__|_| |_|\\___/|_| |_|")
print("        |___/                        ")
print("=" * 40)

print()

# --- Multiplicar strings con * ---
print("-" * 30)
print("*" * 30)
print("Hola " * 5)

print()

# --- sys.stdout.write: escritura directa (sin salto de línea automático) ---
sys.stdout.write("Esto se escribe con sys.stdout.write\n")
sys.stdout.write("No agrega salto de línea automático, ")
sys.stdout.write("así que todo queda en la misma línea.\n")

print()

# --- Imprimir caracteres especiales literales con r"" (raw string) ---
print(r"Esto es un raw string: \n no hace salto de línea")
print(r"Ruta de archivo: C:\Users\alumno\documentos")
print("Comparar con ruta normal: C:\\Users\\alumno\\documentos")

print()

# --- Impresión con formato usando .center(), .ljust(), .rjust() ---
titulo = "FUNDAMENTOS DE PYTHON"
print(titulo.center(40, "="))
print("Alumno".ljust(20, ".") + "Carlos")
print("Carrera".ljust(20, ".") + "Informática")
print("Sede".ljust(20, ".") + "Puerto Montt")
print(titulo.center(40, "="))
