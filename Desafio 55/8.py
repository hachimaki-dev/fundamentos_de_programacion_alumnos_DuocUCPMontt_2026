ram_servidor=16 #en GB
uso_sistema_operativo=2.5

uso_Ram_x_programa=1.2

total_consumo=uso_sistema_operativo+(4*uso_Ram_x_programa)

ram_diponible=1024*(ram_servidor-total_consumo) #en MB

print(f"{ram_diponible} tienes de ram disponible en MB")
