print("Ejercicio 9: Costes de producción (Emprendimiento)")
print("Este programa se usa para calcular tus ganancias mensuales en la venta de camisetas.")

coste_tela = 4000
coste_estampando = 2500
coste_empaque = 500
precio_polera = 15000
ganancia = precio_polera - coste_empaque -coste_estampando - coste_tela
print(f"La ganancia por cada polera hecha es de {ganancia}, y como vendiste 50 ganaste {ganancia * 50}")