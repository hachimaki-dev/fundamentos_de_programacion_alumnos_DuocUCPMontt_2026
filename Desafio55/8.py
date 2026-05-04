servidor=16
so=2.5
programas_corriendo=1.2*4
gasto=so+programas_corriendo
servidor=(servidor-gasto)*1024
print(servidor)