#Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.

#Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.

#Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').

#Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.
cliente = "Postpago"
plan_cliente = 15
plan_usado = 18
tipo_cliente = input("que clase de cliente es:")
if cliente == "Postpago":
    if plan_usado <= 18:
        print("se le cobrara 1000$ por giga usado")
        giga_usado = 3 * 1000
        print(f"usted debe pagar{giga_usado}")
elif cliente == "Prepago":
    print("Sin servicio")