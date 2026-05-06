GB_total_del_servidor = 16
sistema_operativo = 2.5
programas = 4
uso_por_programa = 1.2

uso_total = sistema_operativo + (programas * uso_por_programa)

ram_restante = GB_total_del_servidor - uso_total

ram_restante_en_mb = ram_restante * 1024

print(f"la ram restande es de {ram_restante_en_mb} MB")


