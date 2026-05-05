#Ejercicio 8: Rendimiento de Servidor (AWS EC2)

servidor_gb = 16
sistema_operativo = 2.5
mb = 1024
programas = 1.2 * 4

gasto = sistema_operativo + programas
servidor_gb -= gasto    

servidor_gb = servidor_gb * mb

print(servidor_gb)