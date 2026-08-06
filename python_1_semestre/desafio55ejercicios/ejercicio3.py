""" Ejercicio 3: Repartiendo la Cuenta en el Bar
Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

Datos Iniciales: Son 5 personas en total. 
Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

Reglas de Negocio: Suma todo el consumo. 
A ese total hay que agregarle un 10% extra por la propina. 
El monto final (consumo + propina) se debe dividir 
en partes iguales entre las 5 personas.

Restricciones: Deja que Python haga todas las multiplicaciones y divisiones.
 Imprime exactamente cuánto debe pagar cada uno."""

persona = 5
pichanga = 15000 * 2 
chop = 3500 * 5


total = pichanga + chop
total = total +(total * 0.10)
persona = total // 5 
print(f"el total es: {total} y total c/u es: {persona}")
