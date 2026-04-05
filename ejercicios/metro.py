print("###bienvenido###")
z = 0
y = 250
x = 800
estudiantes = 0
normal = 0
caja = 0
personas = 0
while True :
    respuesta = input("ingrese tipo de pasajero. N = normal, E = estudiante, o corte:")
    if respuesta == "corte" :
        print("cierre")
        print(f"han ingresado {estudiantes} estudiantes")
        print(f"han ingresado {normal} pasajeros normales")
        print(f"han pasado {personas} personas en total")
        print(f"en la caja hay {caja}")
        print("fin")
        break
    elif respuesta == "E" :
        estudiantes = estudiantes + 1
        caja = caja + y
        personas = personas + 1
    elif respuesta == "N" :
        normal = normal + 1
        caja = caja + x
        personas = personas + 1


     