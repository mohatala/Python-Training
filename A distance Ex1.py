def decoder(c):
    v=[]
    for i in c:
        a=0
        for j in c:
            if i==j:
                a+=1
                k=a
                z=i
            else:
                a=0
    
        v.append(k)
        v.append(z)
    

    return(v)
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


















def longueurBloc(t, pos): 
    depart = pos
    if pos >= len(t) or pos < 0:
        return None
    while pos < len(t)-1 and t[pos] == t[pos+1]:
        pos += 1
    return pos-depart+1

#print(longueurBloc(t, 4))







            

