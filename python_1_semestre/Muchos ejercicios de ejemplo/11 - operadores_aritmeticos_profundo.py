# ============================================
# 11 - OPERADORES ARITMÉTICOS (PROFUNDO)
# Tema: Módulo math, funciones numéricas y cálculos complejos
# Nivel: ⭐⭐⭐ Profundo
# ============================================
# Python incluye funciones numéricas integradas y el módulo math
# para cálculos más avanzados.

import math

# --- Funciones integradas (built-in) ---
print("=== FUNCIONES INTEGRADAS ===")

numeros = [15, -7, 23, -3, 42, 8]  # una lista de ejemplos
print(f"Números: {numeros}")
print(f"abs(-7)     = {abs(-7)}")           # valor absoluto
print(f"max(...)    = {max(numeros)}")       # máximo
print(f"min(...)    = {min(numeros)}")       # mínimo
print(f"sum(...)    = {sum(numeros)}")       # suma total
print(f"round(3.7)  = {round(3.7)}")        # redondear
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # redondear a 2 decimales

print()

# --- Módulo math ---
print("=== MÓDULO MATH ===")
print(f"math.pi    = {math.pi}")
print(f"math.e     = {math.e}")
print(f"math.sqrt(144)  = {math.sqrt(144)}")      # raíz cuadrada
print(f"math.pow(2, 10) = {math.pow(2, 10)}")     # potencia (retorna float)
print(f"math.floor(3.9) = {math.floor(3.9)}")     # redondear hacia abajo
print(f"math.ceil(3.1)  = {math.ceil(3.1)}")      # redondear hacia arriba
print(f"math.factorial(5) = {math.factorial(5)}")  # 5! = 120

print()

# --- Ejemplo: Teorema de Pitágoras ---
print("=== TEOREMA DE PITÁGORAS ===")
cateto_a = 3
cateto_b = 4
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
print(f"Catetos: {cateto_a} y {cateto_b}")
print(f"Hipotenusa: {hipotenusa}")

print()

# --- Ejemplo: Área y perímetro del círculo ---
print("=== CÍRCULO ===")
radio = 5
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f"Radio: {radio}")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

print()

# --- Ejemplo: Conversión de temperatura ---
print("=== CONVERSIÓN DE TEMPERATURA ===")
celsius = 36.5
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"{celsius}°C = {fahrenheit}°F = {kelvin}K")

# --- divmod(): división y módulo en una sola operación ---
print()
print("=== DIVMOD ===")
segundos_totales = 7523
minutos, segundos = divmod(segundos_totales, 60)
horas, minutos = divmod(minutos, 60)
print(f"{segundos_totales} segundos = {horas}h {minutos}m {segundos}s")
