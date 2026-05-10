transferencia=[15000, 80000, 2000, 150000]
transferenciaaltoperfil=[]
for i in transferencia:
    if i > 50000:
        transferenciaaltoperfil.append(i)
print(transferenciaaltoperfil)        