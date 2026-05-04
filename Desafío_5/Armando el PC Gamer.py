Valor_de_Procesador = 250000
Valor_de_Placa_Madre = 120000
Valor_de_tajerta_de_video = 450000
precio_original = 450000
Valor_Final = 0
descuento= 0.15

Valor_de_tajerta_de_video = Valor_de_tajerta_de_video * descuento
precio_original = precio_original - Valor_de_tajerta_de_video

Valor_Final = precio_original + Valor_de_Procesador + Valor_de_Placa_Madre

print (Valor_Final)


