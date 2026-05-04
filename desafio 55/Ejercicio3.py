personas = 5
pichangas = 15000
schops = 3500
total = 0
propina = 0
print(f"Hay {personas} personas que quieren comprar 2 Pichangas (${pichangas}CLP Cada una), y 5 schoops (${schops}CLP cada uno)")
total = pichangas * 2 + schops * 5
print(f"Su total a pagar es de ${total}CLP (${pichangas * 2}CLP las pinchangas y ${schops}CLP los Schops), esp sin contar la propina que es de un 10%")
propina = total * 0.1
print(f"En total, los chavalines tienen que pagar ${total + propina}CLP, la propina es de {propina}")
total_por_persona = (total + propina) / 5
print(f"El total por persona es de {total_por_persona}")