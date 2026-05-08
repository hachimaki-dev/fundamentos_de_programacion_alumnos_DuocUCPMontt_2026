"""Ejercicio 16: Plan de Datos WOM con Penalización
Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.

Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.

Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen.

 Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').

Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es,
 y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final."""


Cliente = "PostPago"

Pago_Extra_PostPago = 1000

Plan_GB = 15 #GB

Plan_GB_Usado = 18 #GB


if Cliente == "PostPago":
    Extra = 0
    Total = 0

    Extra = Plan_GB_Usado - Plan_GB
    Total = Extra * Pago_Extra_PostPago

    print(f"Pagaras {Total} sobre tu Plan por el uso de {Extra} GB extra")

else:
    
    print("Sin saldo")


