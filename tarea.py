print("Tengo mi cargador lleno con 5 balas")
municion=5
cargador_con_balas=True
while municion<=5:
    print("Disparo una bala, por lo tanto ahora la municion es")
    municion=municion-1
    print(municion)
    if municion==0:
        cargador_con_balas=False
        print("Ya no tengo mas balas, no puedo disparar")
        break

print("Retirada estoy sin municiones")