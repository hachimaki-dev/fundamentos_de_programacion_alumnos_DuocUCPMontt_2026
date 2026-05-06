total_gb = 16
sistema_gb = 2.5
programas_gb 4 * 1.2

usado_gb = sistema_gb + programas_gb
libre_gb = total_gb - usado_gb

libre_mb = libre_gb * 1024
print(libre_mb)