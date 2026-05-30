# Ejercicio 6 — Patente de vehículo en un estacionamiento
# Un sistema de estacionamiento pide la patente del auto. Debe:

# Tener exactamente 6 caracteres
# No contener espacios
# Dato cultural: En Chile existen dos formatos de patente, ambos de 6 caracteres:

# Formato antiguo (hasta 2007): 4 letras + 2 números (ej: BBCR45)
# Formato nuevo (desde 2007): 2 letras + 4 números (ej: AB1234)
# Para este ejercicio solo validaremos largo y ausencia de espacios, no el patrón exacto de letras/números.

# Si no es válida:

# "Patente inválida. Ingresa exactamente 6 caracteres sin espacios."
carros_desde_2007 = []
carros_antes_2007 = []

try:
    patente_ingresada = input("Ingrese su patente \n").upper()

    if len(patente_ingresada) == 6 and " " not in patente_ingresada:

        if patente_ingresada[:4].isalpha() and patente_ingresada[4:].isdigit():
            carros_antes_2007.append(patente_ingresada)
            print(f"Formato antiguo: {carros_antes_2007}")

        elif patente_ingresada[:2].isalpha() and patente_ingresada[2:].isdigit():
            carros_desde_2007.append(patente_ingresada)
            print(f"Formato nuevo: {carros_desde_2007}")

        else:
            print("Patente inválida. No corresponde a ningún formato.")

    else:
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")

except Exception as error_de_escritura:
    print(f"Se ha cometido un error: {error_de_escritura}")
