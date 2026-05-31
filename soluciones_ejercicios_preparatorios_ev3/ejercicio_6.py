
patente_válida = False
while patente_válida == False:
    patente_a_registrar = input("Ingrese la patente del vehículo ingresado: ")
    for caracter in patente_a_registrar:
        if caracter == " ":
            espacios_en_patente = True
        else:
            espacios_en_patente = False
    if len(patente_a_registrar) == 6 and espacios_en_patente == False:
        print(f"patente: {patente_a_registrar} Registrada")
        patente_válida = True
    else:
        print("Patente inválida, ingrese la patente sin espacios, de 6 caractéres")