#Ejercicio 8: Rendimiento de Servidor (AWS EC2)
#Estás revisando cuánta memoria RAM le queda libre a tu servidor.

#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB.
#Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).

#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. 
#Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).

#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.

server=16
os=2.5
programa=1.2
corriendo=4

suma=os+programa*corriendo
total_gb=server-suma
total_mb=total_gb*1024
print(total_mb)