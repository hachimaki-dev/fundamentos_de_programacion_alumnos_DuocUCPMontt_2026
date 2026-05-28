# Una farmacia necesita ingresar la cantidad de unidades disponibles de un medicamento. No puede ser cero ni negativo (una farmacia con stock negativo no tiene sentido).

#Escribe un programa que pida la cantidad de unidades. Si es inválida, muestra:

# "Dato inválido. Ingresa un entero positivo para el stock."
# Cuando sea válido, muestra el valor que el usuario ingresó:

# "Stock registrado: {cantidad} unidades disponibles."
try:
    stock_farmacia = int(input("Ingrese el stock total de la farmacia"))
    if stock_farmacia < 0:
        print("Debe ser positivo el numero")
    else:
        print(f"Stock registrado : {stock_farmacia} unidades disponibles")
except ValueError:
    print("Dato invalido. Ingrese un numero entero positivo para el stock")