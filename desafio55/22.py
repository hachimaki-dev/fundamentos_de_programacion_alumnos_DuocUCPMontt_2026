Alcancia = 0
Ahorro_mensual = 80000
precio_consola = 450000

contador_meses = 0

while Alcancia <= precio_consola:

    
    Alcancia = Alcancia + Ahorro_mensual
    contador_meses = contador_meses + 1
    
    if Alcancia > precio_consola:
        print(f"Tendras que ahorrar durante {contador_meses} meses")
    