# Ejercicio 6: Extracción de Vocales
# Tienes una cadena llamada palabra.
# Debes recorrerla con un ciclo for y contar cuántas veces aparece la letra 'a' minúscula.
# El resultado debe guardarse en la variable contador_a.
# Ejemplo: Si palabra = 'manzana', entonces contador_a debe ser 3.

contador_a = 0
palabra = "manzana"

for letra in palabra:
    if letra == "a":
        contador_a += 1