while True:
    try:
        ingreso_animales = int(input("cuantos animales se ingresaran : "))
        if ingreso_animales > 0 :
            break
        else:
            print("ingresa un numero mayor que 0")
    except:
        print("ingresa un numero valido")

id_animales = []

for id_por_cada_animal in range(ingreso_animales):
    while True:
            try:
                id_animal = input(f"ingrese el id del animal {id_por_cada_animal +1} minimo 6 caracters y sin espacios : ")
                if len(id_animal) >=6 and " " not in id_animal:
                    break
                else:
                    print("ingrese un nombre con los parametros dados")
            except:
                print("ingrese el nombre de manera correcta")
    id_animales.append(id_animal)

for i in range(len(id_animales)):
    pass
print((len(id_animales)) ,(id_animales))
    