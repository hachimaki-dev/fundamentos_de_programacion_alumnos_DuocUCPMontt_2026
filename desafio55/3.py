#Fuiste a tomar algo con tus amigos y necesitan dividir la cuenta por igual.
#Datos Iniciales: Son 5 personas en total. Compraron 2 pichangas (a 15000 cada una) y 5 schops (a 3500 cada uno).
#Reglas de Negocio: Suma todo el consumo. A ese total hay que agregarle un 10% extra por la propina. 
# El monto final (consumo + propina) se debe dividir en partes iguales entre las 5 personas.
#Restricciones: Deja que Python haga todas las multiplicaciones y divisiones. Imprime exactamente cuánto debe pagar cada uno. RESULTADO 10450.0
personas_total = 5 
propina = 0.10
pichanga = 15000
schops = 3500
monto_final = pichanga * 2 + schops * 5
propina = monto_final * 0.10
monto_final = monto_final + propina
monto_a_cada_uno = monto_final // 5
print(monto_a_cada_uno)