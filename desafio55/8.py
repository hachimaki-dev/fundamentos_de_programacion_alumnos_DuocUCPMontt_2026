servidor = 16
sistema_operativo = 2.5
programa = 1.2
gb = 1024

gasto_sistema = sistema_operativo + (programa * 4)
gasto = servidor - gasto_sistema
gasto_total = gasto * gb

print(f"Te queda de RAM: {gasto_total}")