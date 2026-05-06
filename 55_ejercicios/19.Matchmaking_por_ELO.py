ELO_usuario = 1500
ELO_rival = 1570

diferencia_ELO = ELO_rival - ELO_usuario
if diferencia_ELO <= 50:
    print("Partida Perfecta")
elif diferencia_ELO > 100:
    print("Buscando otro rival...")
else:
    print("Partida Justa")