saldo = 10000
micro = 730
metro = 850
recarga = 3000

dia_normal = micro +(metro*2)
final_del_dia = saldo-dia_normal
final_del_dia2 = final_del_dia + recarga

print(final_del_dia2)