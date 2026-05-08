"""
Ejercicio 16: Plan de Datos WOM con Penalización
Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.

Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.

Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el internet (mensaje 'Sin saldo').

Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. Imprime el recargo final.
"""

tipo_pago = "Postpago"
GB_total = 15
GB_gastados = 18

if tipo_pago == "Postpago":
    if GB_gastados > GB_total:
        cargo_extra = GB_gastados - GB_total
        cargo_extra *= 1000

print(cargo_extra)