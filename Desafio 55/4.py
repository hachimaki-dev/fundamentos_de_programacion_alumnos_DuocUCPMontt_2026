costo_notebook=1200000
costo_envio=15000
numero_cuotas=12 #sin intereses

costo_cuota=costo_notebook/numero_cuotas #sin incluir envio

costo_primera_cuota=costo_cuota+costo_envio

print(f"${costo_primera_cuota} es el valor de la primera cuota mas envio")