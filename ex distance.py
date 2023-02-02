t=[1,1,3,2,2,2,2,5,0,0,3,4,4,0]
#print(decoder(t))


v=[2,1,1,3,4,2,1,5,2,0,1,3,2,4,1,0]




def decode(c):
    t=[]
    for i in range(len(c)-1):
        if i%2==0:
            for j in range(c[i]):
                t.append(c[i+1])
    return t
print(decode(v))
