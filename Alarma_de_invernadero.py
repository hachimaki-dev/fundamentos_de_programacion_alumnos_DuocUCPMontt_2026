alertas_consecutivas=0

while True:
    temperatura=int(input("Ingrese la temperatura actual: "))
    if temperatura==0:
        break
    if temperatura>=35:
        alertas_consecutivas+=1
    else:
        alertas_consecutivas=0
    if alertas_consecutivas==3:
        print("¡¡¡¡ACTIVANDO ASPERSORES DE EMERGENCIA!!!!")
        break