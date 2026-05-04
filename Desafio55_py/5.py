tarjeta_empieza = 10000
pasaje_micro = 730
pasaje_tren = 850
recarga = 3000


en_el_dia = tarjeta_empieza - pasaje_micro - pasaje_tren - pasaje_tren

despues_recargas = en_el_dia + recarga

print(f"Saldo al final del dia :   {despues_recargas}")












