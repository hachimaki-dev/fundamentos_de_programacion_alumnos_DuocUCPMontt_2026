print("========================")
print("Bienvenido a la Farmacia")
print("========================")

edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C, D): ").upper()

medicamento = 60000
despacho = 8000

if edad <= 30:
    if tramo == "A" or tramo == "B":
        descuento = 0.18
    else:
        descuento = 0.12

elif edad <= 60:
    if tramo == "A" or tramo == "B":
        descuento = 0.12
    else:
        descuento = 0.08

else:
    descuento = 0

medicamento_final = medicamento - (medicamento * descuento)

if tramo == "A" or tramo == "B":
    despacho = despacho - (despacho * 0.10)

if edad >= 55:
    if tramo == "A" or tramo == "B":
        despacho = despacho - (despacho * 0.05)

print(f"El valor de medicamentos es: {medicamento_final}")
print(f"El valor del despacho es: {despacho}")