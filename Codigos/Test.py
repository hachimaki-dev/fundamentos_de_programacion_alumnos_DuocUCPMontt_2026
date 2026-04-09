import time
Rotonda = 0


Vueltas = int(input("Cuantas vueltas quieres hacer?"))
for x in range(Vueltas):
    Rotonda += 1
    time.sleep(Rotonda)
    print(f"Wow, {Rotonda} Vuelta")

print("Eso fue muy divertido")