#Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.

#Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).

#Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.

#Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno.
personas_en_total = 5 
pichanga = 2*15000
schops = 5*3500
consumo_total = pichanga + schops
propina = 1.10
monto_final = consumo_total * propina
pagar_cada_persona = monto_final // personas_en_total
print(f"consumo total es: {consumo_total}")
print(f"monto final es : {monto_final}")
print(f"cada persona debe pagar: {pagar_cada_persona}")



