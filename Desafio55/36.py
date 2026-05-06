server1 = ['U1', 'U2']
server2 = ['U2', 'U3']

for user in server2:
    if user not in server1:
        server1.append(user)

print(server1)