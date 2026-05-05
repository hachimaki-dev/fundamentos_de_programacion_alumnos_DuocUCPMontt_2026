#Administrador de carga bip

tarjeta_bip = 10000
pasaje_micro = 730
metro_punta = 850
recarga = 3000

gasto_dia = pasaje_micro + (metro_punta * 2) 
tarjeta_bip = tarjeta_bip - gasto_dia + recarga

print(tarjeta_bip)

