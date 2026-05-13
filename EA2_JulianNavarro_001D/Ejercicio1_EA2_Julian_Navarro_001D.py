mensual = 60000
despacho = 8000
edad = int(input("Ingrese su edad: "))
tramo = input("Ingrese su tramo (A, B, C o D): ")
if edad <= 30 and (tramo == "A" or tramo == "B"):         mensual -= mensual * 0.18
elif edad <= 30 and (tramo == "C" or tramo == "D"):       mensual -= mensual * 0.12
elif 31 <= edad <= 60 and (tramo == "A" or tramo == "B"): mensual -= mensual * 0.12
elif 31 <= edad <= 60 and (tramo == "C" or tramo == "D"): mensual -= mensual * 0.08
if tramo == "A" or tramo == "B":
    despacho -= despacho * 0.10
    if edad >= 55: despacho -= despacho * 0.05
print(f"El valor de medicamentos es: {mensual}")
print(f"El valor del despacho es: {despacho}")