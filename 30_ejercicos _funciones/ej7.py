def calular_propina(total, porcentaje = 10):
    return (total * porcentaje) / 100
resultado = (calular_propina(int(input("ingres el monto total del pedido: "))))
print(resultado)