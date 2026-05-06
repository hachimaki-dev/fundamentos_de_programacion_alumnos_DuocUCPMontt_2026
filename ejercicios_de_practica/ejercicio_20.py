saldo = 50000
limited_de_retiro = 200000
dinero_a_retirar = 60000

if dinero_a_retirar >= limited_de_retiro: # Primero revisa si esta sobre el limite
    print("Execede limite diario!")
elif dinero_a_retirar > saldo: # Despues si supera el saldo
    print("Saldo insuficiente")
elif dinero_a_retirar % 1000 != 0: #Finalmente si el resto de la division es 0 para confirmar que no hay monedas
    print("No se aceptan monedas!")
else: # En el caso que sea correcto, funcionara
    print("Retiro exitoso!")