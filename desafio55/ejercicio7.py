print("Ejercicio 7: ARmando el PC gamer")

precio_procesador = 250000
precio_motherboard = 120000
precio_tarjeta_video = 450000

print(f"Vas a armar una PC gamer, el procesador que te interesa cuesta {precio_procesador}, la placa madre {precio_motherboard} y la tarjeta de video Nvidia RTX 5090 {precio_tarjeta_video}")
print("Por fortuna la tarjeta de video cuenta con un descuento del 15%, pero solo la tarjeta.")
descuento_tarjeta = precio_tarjeta_video * 0.15
precio_final_tarjeta = precio_tarjeta_video - descuento_tarjeta

print(f"Por lo tanto pagas en total ${precio_final_tarjeta + precio_motherboard + precio_procesador}")