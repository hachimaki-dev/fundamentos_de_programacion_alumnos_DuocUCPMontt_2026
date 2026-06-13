def Edad_y_tramo_user():
    edad = int(input("¿Qué edad tiene?\n"))
    tramo = input("¿Qué tramo es usted? A, B, C o D.\n").upper()
    return edad, tramo

def valor_descuento_medicamentos(edad,tramo):
    if edad > 60:
        return 1
    if edad <= 30:
        return 0.82 if tramo in ("A", "B") else 0.88
    if 31 <= edad <= 60:
        return 0.88 if tramo in ("A", "B") else 0.92
    return 1

def valor_descuento_despacho(edad,tramo):
    if tramo in ("A", "B"):
        return 0.85 if edad >= 55 else 0.9
    return 1

def calcular_total(medicamentos, despacho, edad, tramo):
    descuento_medicamentos = valor_descuento_medicamentos(edad,tramo)
    descuento_despacho = valor_descuento_despacho(edad,tramo)
    return (medicamentos*descuento_medicamentos, despacho*descuento_despacho)

medicamentos = 60000
despacho_a_domicilio = 8000
edad, tramo = Edad_y_tramo_user()
total_medicamentos, total_despacho = calcular_total(medicamentos, despacho_a_domicilio, edad, tramo)
print(f"El valor de los medicamentos es de {total_medicamentos}\n El valor del despacho a domicilio es de {total_despacho}.")