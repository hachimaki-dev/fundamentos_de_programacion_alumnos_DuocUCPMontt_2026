meses = 0 
alcancia = 0 
ahorro_meses = 80000
ps5 = 450000
while True:
    meses = meses + 1
    alcancia = alcancia + ahorro_meses
    print(f"vamos en el mes{meses}")
    print(f"tenemos ahorrado {alcancia}")
    if alcancia >= 450000:
        print("cumpliste con la meta")
        break