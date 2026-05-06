tipo_cliente="postpago"
plan= 15
gb_usados= 18
gasto_extra= 3 #Gb

if tipo_cliente == "postpago":
    if gb_usados > plan:
        cargo_extra = gasto_extra * 1000
        print(f"Te haz pasado de tus gigas mensuales, tu cargo extra es de {cargo_extra} pesos")
    else:
        print("No te haz pasado del limite")
else:
    print("Sin saldo")