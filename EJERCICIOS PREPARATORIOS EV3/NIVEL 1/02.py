#Ejercicio 2 — Stock de una farmacia
#Una farmacia necesita ingresar la cantidad de unidades disponibles de un medicamento. No puede ser cero ni negativo (una farmacia con stock negativo no tiene sentido).

#Escribe un programa que pida la cantidad de unidades. Si es inválida, muestra:

#"Dato inválido. Ingresa un entero positivo para el stock."
#Cuando sea válido, muestra el valor que el usuario ingresó:

#"Stock registrado: {cantidad} unidades disponibles."
#(Ejemplo: si el usuario ingresa 350, se muestra "Stock registrado: 350 unidades disponibles.")

#Piensa: ¿Qué diferencia hay entre capturar ValueError y validar con > 0? ¿Necesitas ambas cosas?

while True:
    try:
        stock = int(input("Ingresa la cantidad de unidades diponibles: "))
        if stock > 0:
            print(f"Stock registrado: {stock} unidades disponibles.")
            break
        else:
            print("Dato inválido. Ingresa un entero positivo para el stock.")
    except:
        print("Dato inválido. Ingresa un entero positivo para el stock.")