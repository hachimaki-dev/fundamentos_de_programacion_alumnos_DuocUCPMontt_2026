#Pasar un ejercicio de la prueba a programacion funcional
# Valores base
CUENTA_BASE = 45000
MEDICION_BASE = 6000


# Función para calcular descuento de la cuenta
def calcular_cuenta(consumo, tarifa):
    descuento = 0

    if consumo >= 500:
        if tarifa in ["A", "B"]:
            descuento = 0.20
        elif tarifa in ["C", "D"]:
            descuento = 0.14

    elif 200 <= consumo <= 499:
        if tarifa in ["A", "B"]:
            descuento = 0.12
        elif tarifa in ["C", "D"]:
            descuento = 0.08

    total = CUENTA_BASE - (CUENTA_BASE * descuento)
    return total


# Función para calcular cargo de medición
def calcular_medicion(consumo, tarifa):
    descuento = 0

    if tarifa in ["A", "B"]:
        descuento += 0.10

        if consumo >= 400:
            descuento += 0.05

    total = MEDICION_BASE - (MEDICION_BASE * descuento)
    return total


# Programa principal
def main():
    consumo = int(input("Ingrese el consumo en kWh: "))
    tarifa = input("Ingrese la tarifa (A, B, C o D): ").upper()

    cuenta_final = calcular_cuenta(consumo, tarifa)
    medicion_final = calcular_medicion(consumo, tarifa)

    print("\n--- RESULTADOS ---")
    print("Cuenta mensual final: $", cuenta_final)
    print("Cargo de medición final: $", medicion_final)


# Ejecutar programa
main()