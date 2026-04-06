final_boss = 1000

while final_boss > 0 :
    print("ingresar daño")
    daño = int(input())
    if daño <= 0 :
        print(f"daño insuficiente ({daño})")
    elif daño > 0 :
        final_boss -= daño
        if final_boss > 0 :
            print(f"al jefe le queda {final_boss}")
print("el jefe murió")