#Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.
#Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.
#Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').
#Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.
tipo_cliente = "Postpago"
plan = 15
gasto_plan = 18
diferencia = plan - gasto_plan
absoluto = abs(diferencia)
cobro_extra = 0
if tipo_cliente == "Postpago":
    if diferencia < 0:
        cobro_extra = absoluto * 1000
        print(f"Cobro extra: {cobro_extra}")
elif tipo_cliente == "Prepago" and diferencia < 0:
    print("Sin saldo")