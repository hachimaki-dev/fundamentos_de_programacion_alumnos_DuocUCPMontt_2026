#Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

#Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

#Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

#Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.
monto_final = 0
pago_partes = 0
personas_total = 5 
pichangas = 30000
schops = 17500
propina = 0
propina = (pichangas + schops * 10) // 100
monto_final = pichangas + schops + propina
pago_partes = monto_final // 5
print(f"lo que usted debe pagar es : {pago_partes}")  