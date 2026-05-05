#Estás revisando cuánta memoria RAM le queda libre a tu servidor.

#Datos Iniciales: El servidor tiene 16 GB en total. El sistema operativo siempre usa 2.5 GB. Tienes 4 programas corriendo y cada uno usa 1.2 GB. (Recuerda que 1 GB son 1024 MB).

#Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas. Réstale eso al total para saber cuántos GB quedan libres. Pero ojo, el resultado final debe estar en Megabytes (MB).

#Restricciones: Convierte la RAM restante multiplicándola por 1024 antes de imprimirla. Imprime solo el número.

gb_total = 16
sistema_operativo = 2.5
programa1 = 1.2
programa2 = 1.2
programa3 = 1.2
programa4 = 1.2

gb_restante = gb_total - sistema_operativo - programa1 - programa2 - programa3 - programa4
conversion_a_mg = gb_restante * 1024
print(f"{conversion_a_mg}")