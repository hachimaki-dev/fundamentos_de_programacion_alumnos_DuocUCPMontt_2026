# TERMINADO PERO REVISA Y ESTUDIA

print("--- ALARMA INVERNADERO ---")

print("comencemos....")

alertas_consecutivas = 0
temperatura_maxima = 35

while True:

    temperatura = int(input("ingrese temperatura: "))

    if 0 < temperatura < temperatura_maxima:
        print("temperatura normal")
        
        alertas_consecutivas = 0 
        

    elif temperatura >= temperatura_maxima:
        alertas_consecutivas += 1
        print(f"TEMPERATURA MAXIMA EXCEDIDA (Alerta {alertas_consecutivas}/3)")

    elif temperatura <= 0:
        print("hasta luego")
        break 
    if alertas_consecutivas == 3:
        print("¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!")
        break 

    


