servidor = 16
totalrammega_servidor = servidor  * 1024
sistema_operativo = 2.5
programa = 1.2
programas = programa * 4
programas_mega = programas * 1024
restante = sistema_operativo + programas
restante = servidor - restante
restante_mega = restante * 1024
print(restante_mega)