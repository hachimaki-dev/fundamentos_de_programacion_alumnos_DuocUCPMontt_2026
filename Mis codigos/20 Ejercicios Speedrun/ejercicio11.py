# Ejercicio 11: Acceso a Diccionarios
# Tienes un diccionario llamado enemigo.
# Debes extraer el valor de la clave 'hp' y guardarlo en una variable llamada salud_actual.
# Ejemplo: Si enemigo = {'nombre': 'Slime', 'hp': 45}, entonces salud_actual = 45.

enemigo = {"nombre":"Slime", "hp":45}
salud_actual = enemigo["hp"]
print(salud_actual)