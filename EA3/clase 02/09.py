#Crea celsius_a_fahrenheit(c) que retorne la temperatura en F. Fórmula: (C * 9/5) + 32.

C = int(input("Ingresa grados celsius (°C): "))

def celsius_a_fahrenheit(C):
    F = (C * 9/5) + 32
    return F

fahrenheit = celsius_a_fahrenheit(C)
print(f"{fahrenheit}°F")