"""Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno."""


total_personas = 5
pichangas = 2*15000
schops = 5 * 3500

consumo = pichangas + schops
propina = consumo * 0.10
total = consumo + propina 

por_persona = total/total_personas
print(por_persona)