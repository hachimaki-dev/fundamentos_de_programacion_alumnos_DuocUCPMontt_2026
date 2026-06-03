lista_tecnicos = []
conteo_categorias = {
    "tecnico maestro": 0,
    "tecnico optativo": 0
}
while True:
    try:
        registro = int(input("cuantos tecnicos vas a registrar: "))
        if registro < 0:
            print("no puede ser numeros negativos")
        else:
            print(f"vas as registrar {registro} usuarios")
            break
    except:
        print("solo numeros enteros positivos")

for i in range(registro):
    print(f"registro de usuario {i + 1}")

    while True:
        try:
            nombre = input("escribe su nombre/codigo")
            if len(nombre) >= 6 and not " " in nombre:
             break
            else:
                print("error intenta de nuevo")
        except:
            print("error intenta de nuevo")
    
    while True:
        try:
            AñosDeTrabajo = int(input("cuantos años lleva trabajando: "))
            if AñosDeTrabajo < 0:
                print("no puedes poner numeros negativos")
            else:
                break
        except:
            print("error intenta de nuevo")
        
    categoria = ""

    if AñosDeTrabajo > 10:
        categoria = "tecnico maestro"
    else:
        categoria = "tecnico optativo"
    
    conteo_categorias[categoria] += 1
    lista = {
        "nombre": nombre,
        "categoria": categoria,
        "años de servicio": AñosDeTrabajo,
    }
    lista_tecnicos.append(lista)
    print("registro con exito")
maestro = conteo_categorias["tecnico maestro"]
optativo = conteo_categorias["tecnico optativo"]
print(f"hay {maestro} tecnicos maestros y {optativo} tecnicos optativos")
