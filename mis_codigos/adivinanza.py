import random
n = random.randint(1, 11)
if n == 11:
    n -= 1
    #print(n)
elif (n % 2) != 0:
    n += 1
    #print(n)
intentos = 3
while intentos > 0:
    imput = int(input())
    if imput != n:
        intentos -= 1
        print(f"cagaste, te quedan {intentos} intentos")
    else:
        print("Felicidades")
        break