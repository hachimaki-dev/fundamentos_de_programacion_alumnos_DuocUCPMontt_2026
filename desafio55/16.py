#Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.
#Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.
#Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. 
#Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').
#Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). 
#Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.
tipo_cliente = "Postpago"
gigas_plan = 15
gigas_gastados = 18
precio_GB_extra = 1000
if tipo_cliente == "Postpago":
    if gigas_gastados > gigas_plan:
        GB_extras = gigas_gastados- gigas_plan
        recargo = GB_extras * precio_GB_extra
        print(recargo)

    else:
        print("El cliente no supero su plan de GB")
elif tipo_cliente == "Prepago":
    print("Sin saldo, Internet cortado")
else:
    print("cliente no reconocido..")

