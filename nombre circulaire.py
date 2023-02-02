x="1234"
L=[x]
for i in range(len(x)-1):
               L.append(L[-1][1:]+L[-1][0])

print(L)
