saldo = 50000 
maximo_retiro_diario = 200000
retirado = 60000

if retirado > maximo_retiro_diario :
    print("Excede límite diario")
elif retirado > saldo :
    print("Saldo insuficiente")
elif retirado % 5000 != 0 :
    print("Monto inválido")
else :
    print("Retiro exitoso")