#Valores en GB
memoria_servidor= 16
uso_os= 2.5
uso_programas=1.2*4
memoriarestante= memoria_servidor-uso_os-uso_programas
#Transformacion a MB 1GB=1024MB
print(memoriarestante*1024)