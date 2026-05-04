#Estás revisando cuánta memoria RAM le queda libre a tu servidor.

#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).

#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).

#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.
servidor = 16 
sistema_operativo = 2.5
programas = 4*1.2
un_giga = 1024 # un giga son 10024 mb 
suma_lo_que_gasta_el_sistema = sistema_operativo + programas
total_restante = servidor - suma_lo_que_gasta_el_sistema
mega_byte = total_restante * un_giga
print(mega_byte)

