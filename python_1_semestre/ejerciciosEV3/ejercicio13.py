""" Ejercicio 13 — Inventario de computadores en una empresa TI
Un técnico registra computadores en el sistema de inventario. 
Ingresa cuántos equipos ingresarán. Para cada computador:

Código de activo: mínimo 6 caracteres, sin espacios
Año de fabricación: entero entre 1990 y 2026 (validado)
¿Por qué un rango? Validar solo "entero positivo" 
aceptaría valores absurdos como 3 o 9999. Un rango razonable (1990 a año actual) 
es más realista y te obliga a practicar validación de rango, una habilidad 
muy útil para la evaluación.

Clasifica:

Fabricado antes del año 2018 → Equipo obsoleto
Fabricado en 2018 o después → Equipo vigente
Muestra el resumen al finalizar. """

equipos = int(input("ingresa la cantidad de equipos que entraran: "))
claves = []
for cantidad_equipos in range(equipos):
    while True:
        try: 
            codigo = input(f"ingresa el codigo del equipo numero: {cantidad_equipos +1}")
            if len(codigo) >= 6 and " " not in codigo:
                break
            else:
                print("tiene que ser un codigo de minimo 6 letras y sin espacios")
        except:
            print("ingresa un codigo valido")
    claves.append(codigo)

anos_de_todos_los_equipos = []
equipo_obsoleto = 0
equipo_vigente = 0

for ano_equipos in range(equipos):
    while True:
        try:
            anos_de_cada_equipo = int(input(f"ingresa el ano de fabricacion del equipo n{ano_equipos + 1} :  "))
            if anos_de_cada_equipo > 1990 and anos_de_cada_equipo < 2026:
                break
            else:
                print("ingresa el ano del equipo desde 1990 hasta la actualidad")
        except:
            print("ingresa un numero valido")
    anos_de_todos_los_equipos.append(anos_de_cada_equipo)
    if anos_de_cada_equipo < 2018:
        equipo_obsoleto +=1
    elif anos_de_cada_equipo > 2018 and anos_de_cada_equipo <= 2025:
        equipo_vigente +=1

print(f" cantidad de equipos vigente : {equipo_vigente}\n cantidad de equipos obsoletos:  {equipo_obsoleto}")

