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

    try:
        username = input("Ingresa tu nombre de usuario: ")

        if len(username) >= 6 and " " not in username:
            print(f"Usuario creado: {username}")
            break
        else:
            raise ValueError
        
    except ValueError:
        print("Nombre inválido. Debe tener al menos 6 caracteres y no contener espacios.")