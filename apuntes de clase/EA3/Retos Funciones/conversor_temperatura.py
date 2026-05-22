def celsius_a_fahrenheit(c):
    f = (c * 9/5) + 32
    return print(f"{c}°C son {f}°F")

celsius_a_fahrenheit(int(input("Ingresa la temperatura en Celsius: ")))