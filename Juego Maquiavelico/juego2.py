import sys
import time
def maquina_escribir(texto, velocidad=0.04):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()
maquina_escribir("? = Te despiestas temprano, te encuentras sin emoción alguna")
maquina_escribir("? = Un guardia pasa por tu celda...")
maquina_escribir("? = Se te queda viendo y te pregunta")
maquina_escribir("Guardia = ¿Comó te llamas pedazo de basura?")
maquina_escribir("Ingresa tu nombre")
nombre = input("")
maquina_escribir(f"{nombre} = Me llamo {nombre}")