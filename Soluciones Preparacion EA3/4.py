#Ejercicio 4 — Nombre de usuario para una app bancaria
#Un banco digital pide al usuario crear un nombre de usuario. Las reglas son:

#Mínimo 6 caracteres
#Sin espacios
#Si no cumple, muestra:

#"Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios."
#Ejemplos válidos: juanp23, mariatorres, cliente99 Ejemplos inválidos: juan, maria torres, ok

#Cuando sea válido:

#"Usuario creado: juanp23"

while True:
    nombre_usuario=input("\nIngrese un nombre de usuario: ")
    if len(nombre_usuario)>=6 and " " not in nombre_usuario:
        print(f"Usuario creado: {nombre_usuario}\n")
        break
    else:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.\n")