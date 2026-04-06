
#Inicio alarma del invernadero
temperatura_actual = 0
contador_alerta = 0

print("*Iniciando Sistema, Espere un momento*")

temperatura_actual = int(input("Ingrese Temperatura actual: "))
while temperatura_actual == 0 :   
    print("Terminando lectura de datos")
    break

while temperatura_actual >= 35 :
    print("Tenga cuidado, la temperatura esta elevada")
    contador_alerta += 1
    temperatura_actual = int(input("Ingrese Temperatura actual: "))

    if temperatura_actual < 35 :
        print("Restableciendo Contador de alertas")
        contador_alerta = 0
        print(f"Nuevo contador: {contador_alerta} ")
        temperatura_actual = int(input("Ingrese Temperatura actual: "))

    if contador_alerta >= 3 :
        print(f"¡¡¡¡¡¡ EMERGENCIA EMERGENCIA POR TEMPERATURA ELEVADA EL CONTADOR DE ALERTA SE ENCUENTRA EN {contador_alerta} ACTIVANDO ASPERSORES DE EMERGENCIA !!!!!!!")
        break
#Fin Alarma del invernadero
   

 









