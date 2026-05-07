tarjeta = 10000
pasaje_micro = 730
metro_en_punta = 850 

recarga = 3000

#gasto en trayecto movilixacion = tarjeta + pasaje_micro + metro_en_punta - recarga
gasto_en_trayecto_movilizacion = tarjeta - pasaje_micro - metro_en_punta * 2 + recarga
print(f"El gasto en trayecto movilización es: {gasto_en_trayecto_movilizacion}")    
