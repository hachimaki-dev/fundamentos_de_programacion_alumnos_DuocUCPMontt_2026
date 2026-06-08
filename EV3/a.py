codigos = []
maestro = 0
operario = 0

while True:
    try:
        tecnicos = int(input("ingrese el numero de tecnicos"))
        if tecnicos > 0:
            break
        else:
            print("tiene ques er mayor que cero")
    except ValueError:
        print("tiene ques ser un numero")

for i in range(tecnicos):
    while True:
        codigo_tecnico = input("ingrese su codigod etecnico")
        if len(codigo_tecnico) >= 6 and not " " in codigo_tecnico:
            codigos.append(codigo_tecnico)
            break
        else:
            print("codigo no valido tiene que tener 6 caracteres y no espacios")
    while True:
        try:
            años = int(input("ingrese sus años de experiencia"))
            if años > 0:
                if años > 10:
                    maestro += 1
                    break
                else:
                    operario += 1
                    break
            else:
                print("tiene que ser mayor que 0")
        except ValueError:
            print("tiene que ser un numero")

print(f"La planta cuenta con {maestro} Técnicos Maestros y {operario} Técnicos Operarios")