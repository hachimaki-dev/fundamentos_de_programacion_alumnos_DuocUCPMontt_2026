#Ejercicio 22: Ahorro Meta Mensual (PS5)

alcancia = 0
ahorro = 80000
meta_consola = 450000
meses = 0

while True:
   
    if alcancia <meta_consola:
        alcancia = alcancia + ahorro
        meses = meses + 1

    else:
        print(meses)
        break