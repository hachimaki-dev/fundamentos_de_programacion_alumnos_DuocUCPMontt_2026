#Ejercicio 6 — Patente de vehículo en un estacionamiento
#Un sistema de estacionamiento pide la patente del auto. Debe:

#Tener exactamente 6 caracteres
#No contener espacios
#Dato cultural: En Chile existen dos formatos de patente, ambos de 6 caracteres:

#Formato antiguo (hasta 2007): 4 letras + 2 números (ej: BBCR45)
#Formato nuevo (desde 2007): 2 letras + 4 números (ej: AB1234)
#Para este ejercicio solo validaremos largo y ausencia de espacios, no el patrón exacto de letras/números.

#Si no es válida:

#"Patente inválida. Ingresa exactamente 6 caracteres sin espacios."
#Válidas: BBCR45, AB1234 Inválidas: BB CR45, AB12, ABCDEFG

while True:

    try:
        patente_auto = input("Ingrese la patente de su auto: ").upper()

        if len(patente_auto) == 6 and " " not in patente_auto:
            print(f"Patente válida: {patente_auto}")
            break
        else:
            raise ValueError
        
    except ValueError:
        print("Patente inválida. Ingresa exactamente 6 caracteres sin espacios.")