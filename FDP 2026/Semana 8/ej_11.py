# Tienes un diccionario llamado enemigo.

# Debes extraer el valor de la clave 'hp' y guardarlo en una variable llamada salud_actual.

enemigo = {"nombre": "Peter", "hp": 1000}

salud_actual = enemigo.get("hp")

print(salud_actual)