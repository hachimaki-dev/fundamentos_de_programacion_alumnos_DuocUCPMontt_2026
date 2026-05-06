Postpago = 18
Giga_extra = 1000
Prepago = 18
Total_postpago = 0
Prepago_corte = ""
if Postpago > 15:
  Total_postpago = Giga_extra * 3
  print(Total_postpago)
  if Prepago > 15:
    Prepago_corte = "Sin saldo"
    print(Prepago_corte)
  
  
