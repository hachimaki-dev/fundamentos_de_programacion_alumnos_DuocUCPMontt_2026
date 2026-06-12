patentes = []
toneladas = []
camiones_pesados = 0
camioneta_liviano = 0
while True:
    try:
        vehiculos_a_registrar = int(input("ingrese cuantos vehiculos a registrar: "))
        if vehiculos_a_registrar > 0:
            break
    except ValueError:
        print("ERROR: ingrese solo numeros enteros")
for vehiculo in range(vehiculos_a_registrar):
    while True:
        patente_ingresada = input(f"ingrese la patente del vehiculo {vehiculo + 1}: ")
        if len(patente_ingresada) >= 6 and " " not in patente_ingresada:
            patentes.append(patente_ingresada)
            break
        else:
            print("Invalido: ingrese 6 caracter sin espacios")
    while True:
        try:
            tonelada = int(input(f"ingrese las toneladas del vehiculo {vehiculo + 1} : "))
            if tonelada > 0:
                toneladas.append(tonelada)
                break
            else:
                print("Error: ingrese solo numeros positivos")
        except ValueError:
            print("ingrese solo numeros enteros")
    if tonelada > 15 :
        camiones_pesados += 1
    else:
        camioneta_liviano += 1
for vehiculo in range(vehiculos_a_registrar):
    print(f"vehiculo {vehiculo +1} patente {patentes [vehiculo]} con {toneladas[vehiculo]} tonelada")
print(f"La flota cuenta con
      
      
      
      {camiones_pesados} pesados y {camioneta_liviano} livianos. registro completado. ")