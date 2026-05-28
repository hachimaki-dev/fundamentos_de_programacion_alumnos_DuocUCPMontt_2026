valor_mensual_medicamento = 60000
valor_despacho = 8000

try:
    edad_usuario = int(input("Ingrese su edad: "))
    tramo_usuario = input("Ingrese su tramo (A, B, C, D): ").upper()

    if tramo_usuario not in ["A", "B", "C", "D"]:
        raise ValueError("El tramo ingresado no es válido.")

    if edad_usuario < 0:
        raise ValueError("La edad no puede ser negativa.")

    if (edad_usuario <= 30) and (tramo_usuario == "A" or tramo_usuario == "B"):
        valor_mensual_medicamento *= 0.82
        valor_despacho *= 0.9

    elif (edad_usuario <= 30) and (tramo_usuario == "C" or tramo_usuario == "D"):
        valor_mensual_medicamento *= 0.88

    elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "A" or tramo_usuario == "B"):
        if edad_usuario >= 55:
            valor_despacho *= 0.85
        else:
            valor_mensual_medicamento *= 0.88

    elif (edad_usuario >= 31 and edad_usuario <= 60) and (tramo_usuario == "C" or tramo_usuario == "D"):
        valor_mensual_medicamento *= 0.92

    print(f"El valor de medicamentos es: ${valor_mensual_medicamento}")
    print(f"El valor del despacho es: ${valor_despacho}")

except ValueError as error:
    print(f"Error de ingreso: {error}")

except Exception as error:
    print(f"Ocurrió un error inesperado: {error}")

finally:
    print("Programa finalizado.")