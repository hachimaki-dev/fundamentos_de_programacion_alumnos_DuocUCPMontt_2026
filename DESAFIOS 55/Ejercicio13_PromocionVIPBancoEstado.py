sueldocliente=800000
antiguedadcuenta= 6 #en años
deudasactivas=0

if sueldocliente>1000000 or (antiguedadcuenta>=5 and deudasactivas==0):
    print("Cliente VIP")
else:
    print("Cliente Normal")