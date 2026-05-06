#Ejercicio 8: Rendimiento de Servidor (AWS EC2)
#Estás revisando cuánta memoria RAM le queda libre a tu servidor.

#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).

#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).

#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.

#Resultado esperado en consola:
#8908.8


servidor_gb = 16
sistema_operativo_gb = 2.5
megabytes = 1024
programas = 4*1.2



gastos_giga = sistema_operativo_gb + programas


gigas_libres = (servidor_gb - gastos_giga)*megabytes

print(gigas_libres)