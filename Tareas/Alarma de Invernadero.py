bandera = True
contador_negativo = 3

print("Este es un programa de invernadero APRUEBA DE INCENDIOSSSS TIOOOOOOOOOO")

while bandera:
    temperatura_ingresada = int(input("Ingrese una temperatura"))
    if temperatura_ingresada == 0:
        print("Ah vale vale...")
        print("Se termino la lectura de datos chavalin bombin")
    if temperatura_ingresada < 35:
        print("El contador de alarmas se reinicio a 0")
    else:
        contador_negativo = contador_negativo - 1
        print("TEN CUIDADO CON LA TEMPERATURA")
        print(f"Si pones una temperatura tan elevada se puede quemar TODO. Te quedan {contador_negativo} oportunidades de salvar el invernadero")

    if contador_negativo == 0:
        print("ACTIVANDO SISTEMA DE REGADERA, SE INCENDIO TODO EL INVERNADERO")
        break
        bandera = False