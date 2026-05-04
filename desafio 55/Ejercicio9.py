precio_polera = 15000
tela = 4000
estampado = 2500
empaque = 500
fabricacion = tela + estampado + empaque
venta_total = 0
precio_fabricacion = 0
print(f"Vendo poleras a ${precio_polera}CLP, su fabricacion me cuesta ${fabricacion}CLP ")
print(f"La tela cuesta ${tela}CLP, el estampado ${estampado}CLP, y el empaque ${empaque}CLP")
venta_total = precio_polera * 50
precio_fabricacion = fabricacion * 50
print(f"En total vendi 50 poleras lo que seria ${venta_total}CLP, pero hay que descontarles la fabricación")
venta_total = venta_total - precio_fabricacion
print(f"El precio de fabricacion es de ${precio_fabricacion}CLP, la ganancia es de ${venta_total}CLP")