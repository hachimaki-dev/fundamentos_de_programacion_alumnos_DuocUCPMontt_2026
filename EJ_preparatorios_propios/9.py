solicitudes = 0
aprobados = 0
revision_manual = 0
rechzado = 0

while True:
    try:
        score_cada_participante = int(input("Ingrese el score del Solicitante :   "))
        if score_cada_participante < 0 or score_cada_participante > 1000:
            print("Ingrese una Opcion valida")    
            continue
        else:
            solicitudes += 1
    except ValueError:
        print("Ingrese una Opcion valida") 
        continue   

    
    if score_cada_participante > 750:
        print("Aprobado Automaticamente ")
        aprobados += 1
    elif score_cada_participante >= 500 and score_cada_participante <= 750:
        print("Revision Manual")
        revision_manual += 1    
    elif score_cada_participante < 500:
        print("Rechazado")
        rechzado += 1
    

    if solicitudes == 8 :
        print(f"Aprobados : {aprobados}")
        print(f"Revision Manual : {revision_manual}")
        print(f"Rechazados : {rechzado}")
        break