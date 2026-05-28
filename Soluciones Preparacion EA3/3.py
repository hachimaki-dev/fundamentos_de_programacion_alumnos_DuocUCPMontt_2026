#Una farmacia necesita ingresar la cantidad de unidades disponibles de un medicamento. No puede ser cero ni negativo (una farmacia con stock negativo no tiene sentido).

#Escribe un programa que pida la cantidad de unidades. Si es inválida, muestra:

#"Dato inválido. Ingresa un entero positivo para el stock."
#Cuando sea válido, muestra el valor que el usuario ingresó:

#"Stock registrado: {cantidad} unidades disponibles."
#(Ejemplo: si el usuario ingresa 350, se muestra "Stock registrado: 350 unidades disponibles.")

#Piensa: ¿Qué diferencia hay entre capturar ValueError y validar con > 0? ¿Necesitas ambas cosas?

#Capturar ValueError es importante para manejar entradas no numéricas, mientras que validar con > 0 asegura que el número sea positivo. 
#Ambas validaciones son necesarias para garantizar la integridad de los datos.       



try:
    stock_medicamento=int(input("\nIngresa la cantidad de unidades disponibles del medicamento: "))
    if stock_medicamento>0:
        print(f"Stock registrado: {stock_medicamento} unidades disponibles.\n")
    else:
        print("Dato inválido. Ingresa un entero positivo para el stock.\n")
except ValueError:
    print("Dato inválido. Ingresa un entero positivo para el stock.\n")