score_crediticio = {"Aprobado automaticamente": 0 , "Revisión normal": 0, "Rechazado": 0}
contador = 1
while contador < 9:
    try:
        solicitud_credito = int(input("¿Cuanto score crediticio solicitará?\n"))
        if solicitud_credito < 0 or solicitud_credito > 1000:
            print("Debe ingresar numeros enteros positivos y debe ser menor o igual a 1000.")
            continue
        if solicitud_credito > 750:
            print("Aprobado automaticamente.")
            score_crediticio["Aprobado automaticamente"] += 1
            contador+=1
        elif solicitud_credito >= 500 and solicitud_credito <= 750:
            print("Revisión normal.")
            score_crediticio["Revisión normal"]+=1
            contador+=1
        else:
            print("Rechazado")
            score_crediticio["Rechazado"]+=1
            contador+=1
    except ValueError:
        print("Error, debe ingresar NUMEROS enteros positivos.")
print(score_crediticio)