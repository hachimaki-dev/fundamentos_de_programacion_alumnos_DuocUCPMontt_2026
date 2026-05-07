server=["U1","U2"]
server2=["U2","U3"]

for i in server2:
    if i not in server:
        server.append(i)
print(server)