# Tomar el ejericio 1 o 2 
# De la prueba
# Y trasformarlo a programacion funciones

def calcular_descuento(edad, tramo):

    if edad <= 30:
        if tramo == "A" or tramo == "B":
            return 0.18
        else:
            return 0.12
    elif edad <= 60:
        if tramo == "A" or tramo == "B":
            return 0.12
        else:
            return 0.08
    else:
        return 0


def calcular_despacho(edad, tramo):

    despacho = 8000
    if tramo == "A" or tramo == "B":
        despacho = despacho - (despacho * 0.10)
    if edad >= 55:
        if tramo == "A" or tramo == "B":
            despacho = despacho - (despacho * 0.05)
    return despacho


print("========================")
print("Bienvenido a la Farmacia")
print("========================")

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C, D): ")

medicamento = 60000

descuento = calcular_descuento(edad, tramo)

medicamento_final = medicamento - (medicamento * descuento)

despacho = calcular_despacho(edad, tramo)

print(f"El valor de medicamentos es: {medicamento_final}")
print(f"El valor del despacho es: {despacho}")