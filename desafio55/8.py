servidor = 16  
sistema_operativo = 2.5
programas_corriendo = 1.2 * 4
gigas = 1024 
gasto_total = servidor - sistema_operativo - programas_corriendo
gasto_total_MB = gasto_total * gigas
print("Gasto total en MB: ", gasto_total_MB)