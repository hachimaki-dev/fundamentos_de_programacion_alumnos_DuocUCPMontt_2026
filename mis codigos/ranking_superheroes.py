# TERMINADO

print("====== RANKING DE SUPERHEROES ======")

print("Buen dia heroe, para calcular tu ranking o categoria, necesitamos pedirte unos datos, por favor dinos")

misiones_exitosas = int(input("Cuantas misiones exitosas has completado?:"))

Daños_civiles = int(input("Daños civiles (en costo monetario):"))

if misiones_exitosas >= 10 and Daños_civiles <= 0:
    print("!GUAU, ERES UN SUPERHEROE CLASE S! BONO MAXIMO :0")
elif misiones_exitosas >= 5:
    print("!GUAU, ERES UN SUPERHEROE CLASE A! CUMPLE PROMEDIO :3")
elif misiones_exitosas < 5 and Daños_civiles >= 10000000:
    print("DESPEDIDO, DEMASIADO CAOS")
else:
    print("Heroe en observacion...")

    