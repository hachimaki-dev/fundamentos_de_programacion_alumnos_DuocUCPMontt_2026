# Crear un algoritmo que obligue al usuario a adivinar un número secreto previamente determinado por el sistema (del 1 al 10).
# Si falla, indicarle que falló y solicitarle que vuelva a intentarlo. Si acierta, lo felicitamos y termina el programa.

numero_secreto = 3
numero_introducido = -1

while numero_secreto != numero_introducido:
    numero_introducido = int (input("Ingrese un número del 1 al 10: "))

    if numero_secreto != numero_introducido:
        print("\nxxx Número incorrecto. Intente de nuevo. xxx\n")

print("\n********************************")
print("*** FELICIDADES, HA ACERTADO ***")
print("********************************")