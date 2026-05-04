#🟢 Rango: Inofensivo
#Ejercicio 3: Repartiendo la Cuenta en el Bar
#Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

#Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

#Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

#Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.

gasto_comida =  2 * 15000 + 5 * 3500

print(f"Primero que nada tuvieron un gasto en comida de: ${gasto_comida}")

gasto_total = gasto_comida + gasto_comida / 10

print(f"Y agregando la propina les quedaría pagar: ${gasto_total}")

aporte_dividido =  gasto_total / 5

print(f"Por lo que cada uno de ustedes vagos deberían pagar: ${aporte_dividido}")