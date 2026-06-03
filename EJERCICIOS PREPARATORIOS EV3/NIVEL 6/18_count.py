#Ejercicio 18 — Sistema de registro de técnicos en una empresa minera
#Una empresa minera necesita registrar a sus técnicos de mantención. El sistema debe:

#Preguntar cuántos técnicos se registrarán (entero positivo, validado con mensaje de error)
#Para cada técnico pedir:
#Código de técnico: mínimo 6 caracteres, sin espacios (validado)
#Años de experiencia: entero positivo (validado con mensaje de error)
#Clasificar según experiencia:
#Más de 10 años → Técnico Maestro
#10 años o menos → Técnico Operario
#Llevar conteo de cada categoría
#Al finalizar mostrar:
#"La planta cuenta con 4 Técnicos Maestros y 6 Técnicos Operarios. Sistema listo."

tecnicos_operarios = 0
tecnicos_maestros = 0

while True:
    try:
        cant_tecnicos = int(input("Ingrese la cantidad de técncos: "))
        if cant_tecnicos <= 0:
            print("Error: La cantidad de técnicos debe ser mayor a 0.")
        else:
            break
    except ValueError:
        print("Error: Ingresa una cantidad válida, en formato numérico.")

for t in range(cant_tecnicos):
    while True:
        codigo_tecnico = input(f"\nCódigo del técnico {t + 1}: ").strip().upper()
        if len(codigo_tecnico) >= 6 and " " not in codigo_tecnico:
                break
        else:
            print("Error: El código del tecnico debe tener mínimo 6 caracteres, sin espacios.")

    while True:
        try:
            experiencia = int(input(f"\nAños de experiencia técnico {codigo_tecnico}: "))
            if experiencia <= 0:
                print("Error: Los años de experiencia deben ser mayores a 0.")
            else:
                break
        except ValueError:
            print("Error: Los años de experiencia del técnico se ingresan en formato numérico.")

    if experiencia > 10:
        tecnicos_maestros += 1
        
    else:
        tecnicos_operarios += 1

print(f"La planta cuenta con {tecnicos_maestros} Técnicos Maestros y {tecnicos_operarios} Técnicos Operarios. Sistema listo.")