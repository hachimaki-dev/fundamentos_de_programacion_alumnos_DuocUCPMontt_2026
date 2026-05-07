#Ejercicio 8: Rendimiento de Servidor (AWS EC2)
#Estás revisando cuánta memoria RAM le queda libre a tu servidor.
#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).
#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).
#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.


#sistema usa 2.5 GB
"GIGABYTE = 1024 MEGABYTE"

sistema_operativo = 2.5
total_Gb = 16
programas = 4
consumo_programas = 1.2

consumo_total_programas = programas * consumo_programas
consumo_total = sistema_operativo + consumo_total_programas
ram_libre = total_Gb - consumo_total
ram_libre_mb = ram_libre * 1024
print(int(ram_libre_mb))


