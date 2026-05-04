bitcoin_t = 0.05
bitcoin_av = 50000
bitcoin_bv = 62000
clp_a_dolar = 900
bitcoin_a = bitcoin_av * bitcoin_t
bitcoin_b = bitcoin_bv * bitcoin_t
bitcoin_c = bitcoin_b - bitcoin_a
bitcoin_a_clp = bitcoin_c * clp_a_dolar

print(bitcoin_a_clp)