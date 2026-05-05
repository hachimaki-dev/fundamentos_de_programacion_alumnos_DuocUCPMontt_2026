servido_gb = 16
s_op_gb = 2.5 
programas_gb = 4 * 1.2
total_gasto_gb = programas_gb + s_op_gb
servido_gb -= total_gasto_gb
print(servido_gb * 1024)