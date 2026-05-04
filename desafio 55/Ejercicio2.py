precio_auto = 5000000
ahorros = 1500000
dinero_faltante = 5000000
ahorro_mensual = 150000
meses = 0

print(f"Me quiero comprar un auto el cual sale ${precio_auto}CLP")
dinero_faltante = dinero_faltante - ahorros
print(f"Ya tengo ahorrado ${ahorros}CLP, por ende me faltaria ${dinero_faltante}CLP")

while True:
    meses = meses + 1
    ahorros = ahorros + ahorro_mensual
    dinero_faltante = dinero_faltante - ahorro_mensual
    print(f"En el mes {meses} llevaria un total de ${ahorros}CLP, me faltaria todavia ${dinero_faltante}CLP para comprar el auto")
    if ahorros >= precio_auto:
        break
print(f"En total demoraria {meses} meses")
print(f"En total me sobraria ${ahorros - precio_auto}CLP")