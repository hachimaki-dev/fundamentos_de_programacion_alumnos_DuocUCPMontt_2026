cuota=500
dinero=0
estado="Indecente"
mood="neutral"
estatus=[f"tu dinero: {dinero}", estado, mood]
inventario=[]
actividades=[f"1-Cazar bestias -30 monedas + 20 monedas  por monstruo abatido (Tiempo medio)", f"2-Atender de dia a noche la taberna -60 monedas (Todo el dia)",f"3-Limpiar la herreria -20 monedas (Poco tiempo)", f"4-Alimentar a los caballos 10 monedas (Poco tiempo)",f"5-Ayudar al escriba 40 monedas (Tiempo moderado)","6-Meditar (Tiempo moderado)",f"7-Comprar",f"8-Ver inventario"]
for actividad in actividades:
    print(actividad)
print(estatus)
#decision=int(input("Que deberia hacer"))

tienda=[f"1-Abrigo largo: $100", "2-Calzas negras: $50", "3-Botas de piel de huargo: $200","4-Calcetines de lana: $10", "5-Vestido blanco: $300", "6-Aretes de plata: $400", "7-collar de rubi: $500" ]
for objeto in tienda:
    print(objeto)