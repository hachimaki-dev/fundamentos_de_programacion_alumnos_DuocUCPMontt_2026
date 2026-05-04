personas_total = 5
pichangas = 2
schops = 5

valor_pichangas = (pichangas * 15000)
valor_schops = (schops * 3500)

suma_consumo = (valor_pichangas + valor_schops)

propina = (suma_consumo * 0.10)

total_con_propina = (suma_consumo + propina)

monto_por_persona = (total_con_propina / personas_total)



print("Fuiste a un Bar con tus amigos y consumieron lo siguiente:")

print("2 x Pichangas con valor de 15.000$ cada una.")
print("5 x Schops con valor de 3.500$ cada uno.")

input()

print(f"El total de lo que consumieron tu y tus amigos es de {suma_consumo}.")

input()

print("Pero a este total hay que agregarle el 10% extra que pagaron por propina.")

input()

print(f"El total del consumo mas la propina es de: {total_con_propina} ")

input()

print(f"Este total lo dividieron en 5 y les dio el siguiente monto a pagar por persona: {monto_por_persona}")
