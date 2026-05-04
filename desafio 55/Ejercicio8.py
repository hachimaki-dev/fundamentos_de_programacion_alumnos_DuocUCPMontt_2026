ram_total = 16
uso_SO = 2.5
uso_programa = 1.2

print(f"Tengo un servidor de AWS que cuenta con {ram_total}GB de ram, pero el Sistema operativo usa {uso_SO}GB y tengo 4 programas que usan {uso_programa}GBs cada uno")
print(f"En total se esta utilizando {uso_SO + uso_programa * 4} GBs")
print(f"En total a mi servidor le queda {ram_total - uso_SO - uso_programa * 4} GBs de ram, unos {(ram_total - uso_SO - uso_programa * 4) * 1024}MB de ram")