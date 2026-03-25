Saldo = 1500
while True:
    Saldo -= 500
    print(f"Saldo: {Saldo}")
    if Saldo <= 1:
        break

if Saldo <= 500:
    print("Saldo bajo")