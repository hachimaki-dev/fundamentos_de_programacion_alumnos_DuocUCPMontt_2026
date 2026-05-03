# Tienes una cadena llamada palabra.

# Debes recorrerla con un ciclo for y contar cuántas veces aparece la letra 'a' minúscula.

# El resultado debe guardarse en la variable contador_a.

palabra = "manazana"
contador_a = 0

for letra in palabra:
    if letra == "a":
        contador_a += 1
        
print(contador_a)