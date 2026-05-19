
def descuento_menores_30_tramo_a_b (medicamentos_mensual , despacho_domicilio):
    descuento = (medicamentos_mensual * 0.18 - medicamentos_mensual)
    descuento_despacho = (despacho_domicilio * 0.10 - despacho_domicilio)
    return descuento , descuento_despacho
def descuento_menores_30_tramo_c_d (medicamentos_mensual , despacho_domicilio):
    descuento = (medicamentos_mensual * 0.12 - medicamentos_mensual)
    descuento_despacho = (despacho_domicilio * 0.10 - despacho_domicilio)
    return descuento , descuento_despacho
def descuento_igual_31_menores_60_tramo_a_b (medicamentos_mensual , despacho_domicilio):
    descuento = (medicamentos_mensual * 0.12 - medicamentos_mensual)
    descuento_despacho = (despacho_domicilio * 0.10 - descuento_despacho)
    return descuento , descuento_despacho
def descuento_igual_31_menores_60_tramo_c_d (medicamentos_mensual , despacho_domicilio):
    descuento = (medicamentos_mensual * 0.08 - medicamentos_mensual)
    descuento_despacho = (despacho_domicilio * 0.08 - despacho_domicilio) 