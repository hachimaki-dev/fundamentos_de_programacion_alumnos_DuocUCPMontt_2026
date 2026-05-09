boos = {"hp" : 100 , "estado" : "vivo"}

boos["hp"] = boos["hp"] - 150

if boos["hp"] < 0:
    boos["hp"] = 0
    boos["estado"] = "muerto"


print(f"{boos}")