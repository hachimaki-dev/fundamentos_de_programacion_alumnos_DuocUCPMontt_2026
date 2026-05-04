#🟢 Rango: Inofensivo
#Ejercicio 4: Calculadora de Cuotas (MercadoLibre)
#Compraste un notebook por internet y quieres saber cuánto pagarás el primer mes.

#Datos Iniciales: El notebook cuesta 1200000 y lo compraste en 12 cuotas sin interés. El envío a tu casa cuesta 15000.

#Reglas de Negocio: El envío no se paga en cuotas, se cobra completo junto con la primera cuota mensual del notebook.

#Restricciones: Calcula el valor de la cuota y súmale el envío. Imprime solamente el total que deberás pagar ese primer mes.

precio_pc = 1200000
cuota_inicial = precio_pc / 12
precio_envio = 15000

print("El valor de tu primera cuota agregando el precio del envío de tu notebook es de: $", cuota_inicial + precio_envio ," pesos")