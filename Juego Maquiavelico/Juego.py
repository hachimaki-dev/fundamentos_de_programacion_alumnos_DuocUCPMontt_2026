import sys
import time
def maquina_escribir(texto, velocidad=0.04):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()
def pausa(segundos=1.5):
    time.sleep(segundos)
maquina_escribir("? = Te despiertas en la madrugada. Algo que, para ti, ya se ha vuelto habitual.")
pausa()
maquina_escribir("? = Estás mareado. No sabes cuánto tiempo llevas en esa celda.")
pausa()
maquina_escribir("? = Miras a tu alrededor. Lo único que ilumina el lugar es una pequeña ventana que da al exterior.")
pausa()
maquina_escribir("? = A través de ella ves la luna... fría, distante.")
pausa()
maquina_escribir("? = Piensas en lo mucho que te gustaría volver a ser libre.")
pausa()
maquina_escribir("? = Estar con tu familia: tu madre, tus hermanos... incluso tu mascota.")
pausa()
maquina_escribir("? = Pero sabes que ya es tarde para eso.")
pausa(2)
maquina_escribir("? = Mañana será tu final.")
pausa(2)
maquina_escribir("? = Y, por primera vez en mucho tiempo...")
pausa(2)
maquina_escribir("? = no te queda ninguna esperanza.")
pausa(2)
print("------------------------------------------------------------")
print("------------------------THE LAST DAY------------------------")
print("------------------------------------------------------------")
pausa(2)
progreso = 0
total = 20

while progreso <= total:
    barra = "#" * progreso + "-" * (total - progreso)
    print(f"\r[{barra}] {progreso * 5}%", end="")
    
    time.sleep(0.2)
    progreso += 1

print("\nBarra Completado!")

maquina_escribir("? = Te despiestas temprano, te encuentras sin emoción alguna")
maquina_escribir("? = Un guardia pasa por tu celda...")
maquina_escribir("? = Se te queda viendo y te pregunta")
maquina_escribir("Guardia = ¿Comó te llamas pedazo de basura?")
maquina_escribir("Ingresa tu nombre")
nombre = input("")
maquina_escribir(f"{nombre} = Me llamo {nombre}")