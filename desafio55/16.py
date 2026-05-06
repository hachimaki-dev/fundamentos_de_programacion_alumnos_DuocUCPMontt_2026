##Ejercicio 16: Plan de Datos WOM con Penalización
#Calcula si a un cliente se le debe c#obrar #por pasa#rse de sus gigas de intern#et.

#Datos Iniciales: El cliente es tipo #'Postp#ago'. Su plan le da #15 GB, pero gastó 18 GB#.

#Reglas de Negocio: A los clientes 'Postpago#' se les cobra 1000 pesos 
# #por cada giga extra que usen. Si el cliente fuera 'Prepago', no se le cobra nada extra, 
# solo s#e le corta el internet (mensaje 'Sin saldo').

#Restricciones: Usa condicionales anidados (un `if` adentro de otro `if`). Primero revisa 
# qué tipo de cliente es, y si es postpago, revisa si se pasó de los gigas 
# par#a calcular el cobro. Impri#me el recargo final.

#Result#ado esperado en cons#ola:
#3000
tipo_de_cliente = "postpago"
plan_cliente_gb = 15
gasto_cliente_gb = 18
cargo_extra_cada_gb = 1000


if tipo_de_cliente == "postpago":
    if gasto_cliente_gb > plan_cliente_gb:
        cargo_extra = (gasto_cliente_gb - plan_cliente_gb)*1000
        print(f"rercago final de ${cargo_extra}")

else:
    print("sin saldo")
