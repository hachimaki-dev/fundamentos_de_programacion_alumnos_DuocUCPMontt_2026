print("Ejercicio 3: Repartiendo la cuenta en un bar")

print("Son 5 personas en un bar, compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno)")
pichanga = 15000
schops = 3500
monto_final = 0
monto_a_pagar = pichanga * 2 + schops * 5
monto_final += monto_a_pagar
monto_final += monto_a_pagar * 0.10 
monto_individual = monto_final // 5


print(f"El total de la cuenta es de ${monto_final}, por lo tanto cada uno debe pagar ${monto_individual}")