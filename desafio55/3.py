"""
Ejercicio 3: Repartiendo la Cuenta en el Bar
Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.
"""

valor_pichanga = 15000
valor_schops = 3500
personas_en_mesa = 5

total_pichangas = valor_pichanga * 2
total_schops = valor_schops * 5

valor_total = total_pichangas + total_schops
propina = valor_total * 0.1

valor_a_pagar = valor_total + propina

print(f"Cada 1 de los 5 debe pagar ${valor_a_pagar/personas_en_mesa}")