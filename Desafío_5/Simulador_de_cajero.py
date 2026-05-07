Saldo_de_usuario = 50000 
Limite_de_retiro = 200000
Retiro_deseado = 60000

if Retiro_deseado > Limite_de_retiro:
    print ("ERROR, Límite diario lcanzado.")

elif  Retiro_deseado > Saldo_de_usuario :
    print ("ERROR, Su saldo es insuficiente.")
    
elif Retiro_deseado / 5 :
    print ("ERROR, Monto invalido")

else:
    print ("ERROR")