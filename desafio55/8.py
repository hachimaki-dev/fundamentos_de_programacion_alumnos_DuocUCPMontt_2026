#Estás revisando cuánta memoria RAM le queda libre a tu servidor.
#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. 
#Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).
#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. 
#Pero ojo, el resultado final debe estar en Megabytes (MB).
#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.8908.8
servidor_gb_total = 16
sistema_operativo = 2.5
programas_corriendo = 4
uso_por_programa = 1.2
gasto_total = sistema_operativo + programas_corriendo * uso_por_programa
gasto_total = gasto_total * 1024
servidor_gb_total = servidor_gb_total * 1024
GB_libres = servidor_gb_total - gasto_total
print(GB_libres)