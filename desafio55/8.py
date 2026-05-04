capacidadgb_servidor = 16
usogb_SO = 2.5
usogb_programa = 1.2 * 4

gasto = usogb_SO + usogb_programa
total = capacidadgb_servidor - gasto
gb_libres = total * 1024
print(gb_libres)
