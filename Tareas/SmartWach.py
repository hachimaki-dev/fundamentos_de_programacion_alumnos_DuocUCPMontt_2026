contador = 0
dias = 0
kilometros_totales = 0
bandera = True

print("Bienvenido al SmatWach de Python, el cual guarda tu progreso día a día en cuanto caminatas")

while bandera:
    dias = dias + 1
    kilometros_del_dìa = int(input(f"Cuantos kilometros recorriste en tu dia {dias}"))
    if kilometros_del_dìa >= 1:
        print(f"Felicidades, {kilometros_del_dìa}Km se han sumado a tu dìa, veamos como vas en tu día {dias + 1}")
        kilometros_totales = kilometros_totales + kilometros_del_dìa
        contador = contador + 1
    if kilometros_del_dìa <= 0:
        print("Una lastima, no se ha sumado ningun kilometro a tu dìa")
        print(f"Veamos como rindes en tu día {dias + 1}")
    if dias == 7 and kilometros_totales > 30:
        print("FELICIDADES TU META SEMANAL HA SIDO CUMPLIDAAAA!!!!")
        print(f"Completaste {contador} días de 7, y recorriste un total de {kilometros_totales}")
        bandera = False
        import sys
        sys.exit ()
    if dias == 7 and kilometros_totales < 30:
        print("Lo hiciste muy bien, pero no haz cumplido tu meta semanal")
        print(f"Completaste {contador} días de 7, y recorriste un total de {kilometros_totales}")
        print(f"Te faltaron {30 - kilometros_totales} ")    
        bandera = False
        import sys
        sys.exit ()