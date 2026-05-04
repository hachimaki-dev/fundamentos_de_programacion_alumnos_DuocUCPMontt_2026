#Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.

#Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.

#Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').

#Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.
cliente = "postpago"
plan = 15
gasto = 18
cobro= 0
if cliente == "postpago":
    cobro_por_gigas = 1000
    if gasto > plan:
        cobro = cobro_por_gigas * (gasto - plan)
        print(f"recargo final {cobro}")
elif cliente == "prepago":
    print("sin saldo ")
