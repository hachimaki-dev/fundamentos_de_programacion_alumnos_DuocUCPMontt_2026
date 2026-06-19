# Administrador de Carga Bip! Avanzado

targeta_Bip = 10000
costo_del_pasaje_micro = 730
costo_del_pasaje_metro = 850
recarga = 3000
día1 = targeta_Bip - (costo_del_pasaje_micro + costo_del_pasaje_metro + costo_del_pasaje_metro )
saldo_nuevo = día1 + recarga
print('Tu salldo final del día es :', saldo_nuevo)