# Ejercicio 16: Plan de Datos WOM con Penalización

print("===================================")
print("Sistema de cálculo de plan de datos")
print("===================================")

tipo_cliente = "Postpago"
plan_gb = 15
uso_gb = 18
recargo = 0

if tipo_cliente == "Postpago":
    
    if uso_gb > plan_gb:
        gigas_extra = uso_gb - plan_gb
        recargo = gigas_extra * 1000
        print(recargo)
        
else:
    print("Sin saldo")