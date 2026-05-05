#Ejercicio 5: Administrador de Carga Bip! Avanzado
#Vas a hacer un seguimiento del saldo de tu tarjeta Bip! durante el día.

#Datos Iniciales: Tu tarjeta empieza con 10000. El pasaje de micro cuesta 730 y el de metro en punta cuesta 850. Además, harás una recarga de 3000.

#Reglas de Negocio: En el día tomas 1 micro y 2 metros. Después de esos viajes, recargas tu tarjeta.

#Restricciones: Usa una sola variable para el saldo y ve restándole o sumándole el dinero paso a paso. Imprime tu saldo al final del día.

#Resultado esperado en consola:
#10570


saldo_tarjeta = 10000
pasaje_normal_micro = 730
pasaje_punta_metro = 850
saldo = 0

recarga = 3000


viajes = pasaje_normal_micro + (pasaje_punta_metro * 2)
saldo_tarjeta -= viajes 
saldo_tarjeta = saldo_tarjeta + recarga

print(saldo_tarjeta)

