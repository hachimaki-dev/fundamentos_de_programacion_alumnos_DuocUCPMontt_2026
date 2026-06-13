server_1 = ["U1","U2"]
server_2 = ["U2","U3"]
for u in server_2:
    if u not in server_1:
        server_1.append(u)
print(server_1)