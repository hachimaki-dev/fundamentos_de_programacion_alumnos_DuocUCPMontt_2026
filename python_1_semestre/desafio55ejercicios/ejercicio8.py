"""Ejercicio 8: Rendimiento de Servidor (AWS EC2)
Estás revisando cuánta memoria RAM le queda libre a tu servidor.

Datos Iniciales: El servidor tiene 16 GB en total. 
El sistema operativo siempre usa 2.5 GB. 
Tienes 4 programas corriendo y cada uno usa 1.2 GB. 
(Recuerda que 1 GB son 1024 MB).

Reglas de Negocio: Suma lo que gasta el sistema y lo que gastan los programas.
 Réstale eso al total para saber cuántos GB quedan libres.
  Pero ojo, el resultado final debe estar en Megabytes (MB).

Restricciones: Convierte la RAM restante multiplicándola 
por 1024 antes de imprimirla. Imprime solo el número."""

#cuanta ram queda libre 

servidor = 16.0
so = 2.5 
programa = 1.2
# 1 gb es 1024mb
# corriendo 4 programas y cada uno usa 1.2gb

gasto_del_sistema = servidor - so
gasto_del_sistema = gasto_del_sistema - (programa * 4)
gasto_del_sistema = gasto_del_sistema * 1024
print(f"{gasto_del_sistema} en mb ")
