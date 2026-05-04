# Ejercicio 3: Repartiendo la Cuenta en el Bar
# Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.
# Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).
# Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) 
# se debe dividir en partes iguales entre las 5 personas.
# Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.

cantidad_personas = 5
valor_pichanga = 15000
valor_schop = 3500

consumo = 2 * valor_pichanga + 5 * valor_schop
monto_final = consumo + (consumo * 0.1)
cada_uno = monto_final/cantidad_personas
print(cada_uno)