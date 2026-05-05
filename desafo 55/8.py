servidor = 16
sistema_operativo = 2.5
programas_corriendo = 4 * 1.2

ram_libre = servidor - (sistema_operativo + programas_corriendo)
resultado_mb = ram_libre * 1024
print(resultado_mb)