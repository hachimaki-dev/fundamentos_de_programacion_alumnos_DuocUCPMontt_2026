print("bienvenido")
auto = 1500
auto2 = 0
moto = 500
moto2 = 0
camion= 3500
camion2= 0
caja = 0
vehiculos = 0
while  True :
    respuesta = input("ingrese el tipo de vehiculo qur tiene auto, moto, camion o salir")
    if respuesta == "salir" :
        print(f"fin en total pasaron {vehiculos} vehiculos")
        print(f"ganancia total {caja}")
        print(f"han pasado {moto2} motos")
        print(f"han pasado {auto2} autos")
        print(f"han pasado {camion2} camiones")
        print(f"han pasado {vehiculos} vehiculos en total")
        if moto2 > auto2 and moto2 > camion2 :
            print(f"el vehiculo ganador es la moto con {moto2} cantidad de vehiculos")
        elif auto2 > moto2 and auto2 > camion2 :
            print(f"el vehiculo ganador es el auto con {auto2} cantidad de vehiculos")
        elif camion2 > auto2 and camion2 > moto2 :
            print(f"el vehiculo ganador es el camion con {camion2} cantidad de vehiculos")
        print("fin")
        break
    elif respuesta == "auto" :
        print("vehiculo guardado con exito")
        auto2 = auto2 + 1
        vehiculos = vehiculos + 1
        caja = caja + auto
    elif respuesta == "moto" :
        print("vehiculo guardado con exito")
        moto2 = moto2 + 1
        vehiculos = vehiculos + 1
        caja = caja + moto
    elif respuesta == "camion" :
        print("vehiculo guardado con exito")
        camion2 = camion2 + 1
        vehiculos = vehiculos + 1
        caja = caja + camion
    elif respuesta != "camion" and "moto" and "auto" :
        print("error, pon un vehiculo valido")