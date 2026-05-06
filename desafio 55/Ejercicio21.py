contador = 10
import time

while True:
    print(f"{contador} segundo/s para el despegue")
    contador = contador - 1
    time.sleep(1)
    if contador == 0:
        print("DESPEGUEEEEE!!!!!")
        break