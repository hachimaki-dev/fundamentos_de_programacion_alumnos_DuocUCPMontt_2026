alertas_consecutivas = 0

while True:
    temperatura_actual = int(input("Ingrese Temperatura Actual :  "))
    if temperatura_actual == 0:
        break
    elif temperatura_actual >= 35:
        alertas_consecutivas += 1
    elif temperatura_actual < 35:
        alertas_consecutivas = 0
    if alertas_consecutivas == 3:
        print("!!!"*35)
        print(" A C T I V A N D O   A S P E R S O R E S   D  E    E M E R G E N C I A  ")
        print("!!!"*35)
        break
    
