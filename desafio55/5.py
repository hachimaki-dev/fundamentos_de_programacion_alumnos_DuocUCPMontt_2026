#Vas a hacer un seguimiento del saldo de tu tarjeta Bip! durante el día.
#Datos Iniciales: Tu tarjeta empieza con 10000. El pasaje de micro cuesta 730 y el de metro en punta cuesta 850. Además, harás una recarga de 3000.
#Reglas de Negocio: En el día tomas 1 micro y 2 metros. Después de esos viajes, recargas tu tarjeta.
#Restricciones: Usa una sola variable para el saldo y ve restándole o sumándole el dinero paso a paso. Imprime tu saldo al final del día.
saldo = 10000 
pasaje_micro = 730
pasaje_metro = 850
recarga = 3000
saldo =  saldo - (pasaje_micro + pasaje_metro * 2) + recarga
print(saldo)