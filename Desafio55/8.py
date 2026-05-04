#Estás revisando cuánta memoria RAM le queda libre a tu servidor.
#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).
#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).
#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.
mem_total = 16
mem_OS = 2.5
mem_programa = 1.2
mem_programas = mem_programa * 4
mem_utilizada = mem_OS + mem_programas
mem_restante = mem_total - mem_utilizada
mem_restante_MB = mem_restante * 1024
print(mem_restante_MB)
