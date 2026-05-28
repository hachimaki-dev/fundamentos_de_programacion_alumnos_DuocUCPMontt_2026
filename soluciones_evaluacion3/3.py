while True:
    try:
        edad_conductor = int(input("Ingresa el edad del conductor: "))
        if edad_conductor >= 18:
            print(f"Edad registrada {edad_conductor}")
            break   
        elif edad_conductor < 18 or edad_conductor < 0:
            continue
    except:
        continue