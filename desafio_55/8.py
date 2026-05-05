#rendimiento de servidor (Aws Ec2)

servidor = 16
sistema_operativo = 2.5
programas = 4
uso_programa = 1.2

uso_programa  = (programas * uso_programa)
total_gb = (sistema_operativo + uso_programa)
gb = servidor - total_gb
ram = gb * 1024

print(f"le queda libre de memoria ram {ram}")
