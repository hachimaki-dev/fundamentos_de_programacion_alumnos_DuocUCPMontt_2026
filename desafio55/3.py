"""
Ejercicio 3: Repartiendo la Cuenta en el Bar
Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una)
y 5 schops (a 3500 cada uno).

Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. 
El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

Restricciones: Deja que Python haga todas las multiplicaciones y divisiones.
Imprime exactamente cuánto debe pagar cada uno.

Resultado esperado en consola:
10450.0
"""

personas_total = 5
pichangas = 2
valor_pichangas = 15000
schops = 5
valor_schops = 3500 

operacion1 = pichangas * valor_pichangas
operacion2 = schops * valor_schops

total_cuentas = operacion1 + operacion2 #47.500

operacion3 = total_cuentas * 0.10 #4.750
operacion4 = operacion3 + total_cuentas #52.250

operacion5 = operacion4 / personas_total
total_5 = operacion5

print(f"El monto final para cada persona es de: {total_5}")