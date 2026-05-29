# Ejercicio 3: Jardín Infantil
# Desarrolle un programa que calcule el valor final de la mensualidad de un jardín infantil y el valor final del kit de materiales.

# Valores base:

# Mensualidad: $85.000
# Kit de materiales: $18.000
# Reglas de descuento para la mensualidad:

# Edad <= 18 meses:
# Nivel 1 o 2 → 20%
# Nivel 3 o 4 → 13%
# Edad entre 19 y 36 meses:
# Nivel 1 o 2 → 12%
# Nivel 3 o 4 → 7%
# Edad > 36 meses → sin descuento.
# Reglas para el kit:

# Nivel 1 o 2 → 10% descuento.
# Si además la edad <= 12 meses → 5% adicional.
# Debe mostrar ambos valores finales.

# Input Esperado
# 10
# 2

# Output Esperado
# Mensualidad: 68000
# Kit materiales: 15390

edad = int(input("¿Cúal es tu edad?: "))
nivel = int(input("¿Cúal es tu nivel?: "))

# Valores base
mensualidad = 85000
kit = 18000

if edad <= 18:
    if nivel in [1, 2]:
        mensualidad *= 0.80
    elif nivel in [3, 4]:
        mensualidad *= 0.87
elif 19 <= edad <= 36:
    if nivel in [1, 2]:
        mensualidad *= 0.88
    elif nivel in [3, 4]:
        mensualidad *= 0.93

# También aplica para el kit
if nivel in [1, 2]:
    kit *= 0.90
    if edad <= 12:
        kit *= 0.95

print(f"Mensualidad: {int(mensualidad)}")
print(f"Kit materiales: {int(kit)}")