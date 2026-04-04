bandera = True
Acumalador_de_dinero = 0
Moto = 0
Auto = 0
Camion = 0

print("Bienvenido al PEAJE DE PYTHONNNNN")
print("Soy una maquina un poco olvidadiza asií que tienes que irme diciendo cuales vehiculos van pasando")
print("Tienes que indicarme que si el vehiculo que pasa es una MOTO, AUTO o CAMION (Tienes que escribirlo todo en mayuscula)")
print("Para terminar el conteo tienes que escribir SALIR")
while bandera:
    Vehiculo_Pasando = input("¿Qué vehiculo quiere pasar por el Peaje?")
    if Vehiculo_Pasando == "MOTO":
        print("Perfecto, eso seria $500CLP")
        Acumalador_de_dinero = Acumalador_de_dinero + 500
        Moto = Moto + 1
    if Vehiculo_Pasando == "AUTO":
        print("Perfecto, eso seria $1500CLP")
        Acumalador_de_dinero = Acumalador_de_dinero + 1500
        Auto = Auto + 1
    if Vehiculo_Pasando == "CAMION":
        print("Perfecto, eso seria $3500CLP")
        Acumalador_de_dinero = Acumalador_de_dinero + 3500
        Camion = Camion + 1
    if Vehiculo_Pasando == "SALIR":
        bandera = False
        break
print(f"Perfecto, el total a pagar sera de ${Acumalador_de_dinero}CLP")
print(f"Han pasado {Moto} motos, {Auto} autos y {Camion} camiones")