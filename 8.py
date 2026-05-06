servidor = 16
sistema_operativo = 2.5
programas = 1.2 * 4

lo_que_gasta_el_sistema = sistema_operativo + programas
GB_libres = servidor - lo_que_gasta_el_sistema

resultado_MG = GB_libres * 1024

print(f"te quedan {resultado_MG}")
