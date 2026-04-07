almuerzo = 0
impresiones = 0
bandera = True
total= 0
print("Bienvenido a tu calculadora de gastos simples de Python")
print("Empecemos por una pregunta simple")

while bandera:
    almuerzo = int(input("¿Cuanto gastas diariamente en el almuerzo?"))
    if almuerzo <= 0:
        respuesta = input(f"¿Estas seguro que gastas {almuerzo} (responde con SI o NO?")
        if respuesta == "SI":
            print("hmmmm, vale")
            break
        if respuesta == "NO":
                print("Vale, entonces te vuelvo a preguntar")
    if almuerzo > 0:
        almuerzo = almuerzo * 7
        print(f"Vale, entonces estarias gastando {almuerzo} semanalmente")
        respuesta = input("¿Estas seguro de tu respuesta (responde con SI o NO)?")
        if respuesta == "SI":
            print("Perfecto, entonces sigamos")
            total = total + almuerzo
            break
        if respuesta == "NO":
            print("Perfecto, entonces te vuelvo a preguntar")


while bandera:
    impresiones = int(input("¿Cuanto impresiones creas diariamente?"))
    if impresiones <= 0:
        respuesta = input(f"¿Estas seguro que imprimes {impresiones} cada dia? (responde con SI o NO?")
        if respuesta == "SI":
            print("hmmmm, vale")
            break
        if respuesta == "NO":
                print("Vale, entonces te vuelvo a preguntar")
    if impresiones > 0:
        impresiones = impresiones * 50 * 7
        print(f"Vale, entonces estarias gastando {impresiones} semanalmente en impresiones")
        respuesta = input("¿Estas seguro de tu respuesta (responde con SI o NO)?")
        if respuesta == "SI":
            print("Perfecto, entonces sigamos")
            total = total + impresiones
            break
        if respuesta == "NO":
            print("Perfecto, entonces te vuelvo a preguntar")

if total > 20000:
    print(f"ALERTA, PRESUPUESTO ALTO, TOTAL DE ${total}CLP")
elif total < 20000:
    print("Presupuesto moderado. Felicidades")