alcancia=0
ahorro_mensual=80000
costo_consola=450000
meses_necesarios=0

while alcancia < costo_consola:
    alcancia=alcancia+ahorro_mensual
    meses_necesarios+=1
    
print(meses_necesarios)
