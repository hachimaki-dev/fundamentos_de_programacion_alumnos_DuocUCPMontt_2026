codigo = []
maestros = 0
operarios = 0

while True:
    try:
        tecnico = int(input("Cuantos ingenieros quiere ingresar: "))
        if tecnico > 0:
            break
        else:
            print("no puede ingresar numeros negativos")
    except ValueError:
        print("Invalido")
for ingenieros in range(tecnico):
    while True:
        codigo_tecnico = input("ingrese codigo tecnico: ")
        if len (codigo_tecnico) >=6 and not " " in codigo_tecnico:
            codigo.append(codigo_tecnico)
            break
        else:
            print("Codigo invalido")
    while True:
        try:
            años_experiencia = int(input("ingrese años experiencia"))
            if años_experiencia > 0:
                if años_experiencia > 10:
                    maestros += 1
                    break
                else:
                    operarios += 1
                    break
            else:
                print("no puedes ingresar numero menor que 0")
        except ValueError:
            print("solo numeros enteros")
            
print(f"la planta tiene {maestros} Tecnicos maestros y {operarios} Tecnicos operarios")

            
            
        
        