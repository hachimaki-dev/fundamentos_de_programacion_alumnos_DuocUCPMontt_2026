costo_del_auto = 5000000
ahorros = 1500000
ahorros_cada_mes = 150000
contador_de_meses = -1

dinero_que_falta = (costo_del_auto - ahorros)



while ahorros < costo_del_auto:
    ahorros = ahorros + ahorros_cada_mes
    contador_de_meses +=1
    
print(f"faltan {dinero_que_falta} para comprar el auto y los meses que falta por ahorrar son {contador_de_meses} meses")
