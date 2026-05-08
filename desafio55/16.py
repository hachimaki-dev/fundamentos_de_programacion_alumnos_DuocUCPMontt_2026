"""
🟡 Rango: Cuidado
Ejercicio 16: Plan de Datos WOM con Penalización
Calcula si a un cliente se le debe cobrar por pasarse de sus gigas de internet.

Datos Iniciales: El cliente es tipo 'Postpago'. Su plan le da 15 GB, pero gastó 18 GB.

Reglas de Negocio: A los clientes 'Postpago' se les cobra 1000 pesos por cada giga extra 
que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, solo se le corta el 
internet (mensaje 'Sin saldo').

Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa 
qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas para calcular el cobro. 
Imprime el recargo final.

Resultado esperado en consola:
3000
"""

tipo_cliente = "postpago"
plan = 15
gasto_plan = 18

if tipo_cliente == "postpago":
    if gasto_plan > plan:
        gigas_extra = gasto_plan - plan
        cobro = gigas_extra * 1000
    else:
        cobro = 0

else:
    print("Sin saldo")

print(f"Tu cobro es de: ${cobro}")
