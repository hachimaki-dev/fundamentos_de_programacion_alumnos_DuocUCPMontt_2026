ram_total = 16
so = 2.5
programas = 4 * 1.2

usado = so + programas
libre_gb = ram_total - usado

libre_mb = libre_gb * 1024

print(libre_mb)
